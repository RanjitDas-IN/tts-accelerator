import asyncio  #Ultra Optimised code! take 3 sec to generate an audio for 60k+ words (60,000 words)
import edge_tts
import re
import sounddevice as sd
import soundfile as sf
import tempfile
import numpy as np
import resampy
from io import BytesIO
from pydub import AudioSegment
import os
from collections import deque
import spacy
# --- Text splitting & merging ---
nlp = spacy.blank("en")
nlp.add_pipe("sentencizer")

# def split_and_merge(text: str) -> list:
#     doc = nlp(text)
#     return [sent.text.strip() for sent in nlp(text).sents if sent.text.strip()]

def split_and_merge(text: str) -> list:
    words = text.strip().split()
    if len(words) <= 5:
        return [text.strip()]
    
    first_chunk = " ".join(words[:5])
    remaining_text = " ".join(words[5:])

    doc = nlp(remaining_text)
    remaining_chunks = [sent.text.strip() for sent in doc.sents if sent.text.strip()]

    return [first_chunk] + remaining_chunks

# --- Audio generation (via temp file) --- It is for saving the MP3 takes 3 sec to speak ---
async def generate_audio_using_tempfile(fragment, voice):
    tts = edge_tts.Communicate(fragment, voice=voice)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        path = tmp.name
    await tts.save(path)
    data, sr = sf.read(path)
    os.remove(path)
    return data, sr


# full RAM Based and super fast, takes 2 sec to speak
async def generate_audio(fragment, voice):
    # Collect audio from stream into a BytesIO buffer
    stream = edge_tts.Communicate(text=fragment, voice=voice)
    mp3_bytes = BytesIO()

    async for chunk in stream.stream():
        if chunk["type"] == "audio":
            mp3_bytes.write(chunk["data"])

    mp3_bytes.seek(0)  # Reset buffer to start

    # Decode MP3 in memory using pydub
    audio = AudioSegment.from_file(mp3_bytes, format="mp3")
    samples = np.array(audio.get_array_of_samples()).astype(np.float32) / (2 ** 15)
    data = samples.reshape((-1, audio.channels))
    return data, audio.frame_rate


# --- Playback helper (blocking) ---
def play_audio(data, samplerate):
    sd.play(data, samplerate)
    sd.wait()

# --- Producer: split text and enqueue ---
async def producer(text, queue):
    fragments = split_and_merge(text)
    for frag in fragments:
        await queue.put(frag)
    await queue.put(None)

# --- Consumer: generate while playing ---
async def consumer(queue):
    # Get first fragment
    frag = await queue.get()
    if frag is None:
        return

    # Generate and get first audio
    data, sr = await generate_audio(frag, voice)

    # Start playback in background
    playback = asyncio.create_task(asyncio.to_thread(play_audio, data, sr))

    # Prepare next fragment
    frag = await queue.get()
    next_task = None
    if frag is not None:
        next_task = asyncio.create_task(generate_audio(frag,voice))
    else:
        # No more fragments, just await playback
        await playback
        return

    # Loop for subsequent fragments
    while True:
        # Wait for playback of current to finish
        await playback
        # Retrieve generated next
        data, sr = await next_task

        # Start playback for this fragment
        playback = asyncio.create_task(asyncio.to_thread(play_audio, data, sr))

        # Fetch and schedule generation of the following fragment
        frag = await queue.get()
        if frag is None:
            # No more, await this playback and exit
            await playback
            break
        next_task = asyncio.create_task(generate_audio(frag,voice))

    # End of consumer

# --- Main entrypoint ---
def speak_text(text):
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        producer(text, queue),
        consumer(queue)
    ))

# --- Demo ---
if __name__ == "__main__":
    from time import perf_counter
    voice ="en-US-AvaMultilingualNeural"
    t0 = perf_counter()
    # Example long text to demonstrate real-time speech generation.
    demo = (
    """
        Elara traced the faded constellation. on Liam’s forearm with a gentle finger. They lay tangled in the tall grass of the Brahmaputra riverbank, the Guwahati sun painting the sky in hues of mango and rose. The air hummed with the drone of unseen insects and the distant calls of river birds.

        They had met by accident, a spilled cup of chai at a bustling market stall. Elara, a weaver with hands that knew the language of silk, and Liam, a visiting botanist captivated by the region’s vibrant flora. Their initial awkwardness had blossomed into stolen glances, shared cups of sweet lassi, and whispered conversations under the shade of ancient banyan trees.
        
        Liam had only intended to stay for a season, documenting rare orchids. Elara had always known the rhythm of her village, the comforting predictability of the loom and the river. Yet, in each other’s eyes, they found a landscape more compelling than any they had known before.
        
        He would tell her about the intricate veins of a newly discovered leaf, his voice filled with a quiet wonder that mirrored her own fascination with the unfolding patterns of her threads. She would describe the subtle shifts in the river’s current, the way the light danced on its surface, her words weaving tapestries as vibrant as her creations.
        
        Their love was a quiet rebellion against the unspoken boundaries of their different worlds. His temporary stay, her rooted life – these were obstacles they chose to ignore in the intoxicating present. Each shared sunset felt like an eternity, each touch a promise whispered on the humid breeze.
        
        One evening, as the first stars began to prick the darkening sky, Liam took her hand. His gaze was earnest, his voice low. “Elara,” he began, the familiar name a melody on his tongue.
        
        She stilled, her heart a frantic drum against her ribs. She knew this moment was coming, the inevitable edge of his departure drawing closer.
        
        But instead of farewell, he said, “I’ve found a rare species of Vanda near the Kaziranga. It only blooms in this specific microclimate. My research… it will take longer than I anticipated.”
        
        A slow smile spread across Elara’s face, mirroring the soft glow of the fireflies beginning their nightly dance. He hadn’t said forever, hadn’t promised a life unburdened by distance and difference. But in the lengthening of his stay, in the unspoken commitment to the land that held them both, they found a fragile, precious hope.
        
        They lay back in the grass, the vastness of the Indian sky a silent witness to their quiet joy. The river flowed on, carrying its secrets to the sea, and for now, under the watchful gaze of the stars, the lovers had found a little more time. Their story, like the intricate patterns Elara wove, was still unfolding, thread by delicate thread.
    """
    )
    demo1= """    
    "Hey Ranjit, good to hear you again!",
    "Welcome back, boss! Ready for action?",
    "Took you long enough, Ranjit.",
    "I was almost asleep. Finally, you spoke!",
    "Voice match confirmed. Access granted.",
    "Authorization successful. Hello Ranjit.",
    "If this wasn't your voice, I was ready to call the police!",
    "Relax, Ranjit, I know it's you. No need to shout.",
    "Obviously it's you. Who else would dare?",
    "No one else sounds this cool, Ranjit.",
    "Recognized instantly. You're unforgettable.",
    "It's you, Ranjit. Let's roll!"
    """

 
    text = (
        """It seems like the user is asking about the minimum number of words that the medium .onnx model requires to produce output efficiently. They want to know the word fragment size where the model processes the fastest. Shorter fragments (like 5 words) are quicker, but longer ones (30–50 words) take more time, and it seems 16k words take a very long time. I think they’re looking for a good range to test for minimal processing time, around 10–30 words might be a sweet spot."""

    )
    # Call the speak_text function to process and play the audio
    speak_text(text)
    
    print(f"Done in {perf_counter() - t0:.2f} sec")
    # Over all Time take to fully run the script 