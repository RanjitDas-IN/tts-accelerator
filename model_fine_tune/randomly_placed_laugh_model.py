"""Take 2sec but not grammertically correct each split"""
"""No metters how many line in the paregragh (upto 16k lines) """


import asyncio  # Ultra Optimised code! takes ~2 sec to generate 60k+ words 
import edge_tts #Randomly placed the laught but keep the naturalness
import re
import sounddevice as sd
import soundfile as sf      # 1.5 sec
import tempfile
import os
import random
import sys

# Path to your laugh dataset
LAUGH_DIR = "/home/ranjit/TTS-Accelerator/Laugh_audio_dataset"
# Preload all laugh file paths
LAUGH_FILES = [os.path.join(LAUGH_DIR, f)
               for f in os.listdir(LAUGH_DIR)
               if f.lower().startswith('laugh') and f.lower().endswith(('.mp3'))]

# --- Text splitting & merging ---
def split_and_merge(text, min_words=5):
    LAUGH_TAG = "__LAUGH__"
    # Isolate the laugh token
    text = text.replace("[add_laugh]", f" {LAUGH_TAG} ")
    # Ensure punctuation spaced
    text = re.sub(r"\.([A-Za-z])", r". \1", text)
    parts = re.split(r'(?<=[,\.!?])\s*', text)
    fragments = []
    buf = ""
    for part in parts:
        if LAUGH_TAG in part:
            # flush buffer
            if buf:
                fragments.append(buf.strip())
                buf = ""
            fragments.append("[add_laugh]")
            # keep any trailing text
            remain = part.replace(LAUGH_TAG, "").strip()
            if remain:
                buf = remain
        else:
            buf = (buf + " " + part.strip()).strip()
            if len(buf.split()) >= min_words:
                fragments.append(buf)
                buf = ""
    if buf:
        fragments.append(buf)
    return fragments

# --- Generate TTS audio via edge-tts ---
async def generate_tts(fragment, voice="en-US-AvaMultilingualNeural"):
    tts = edge_tts.Communicate(fragment, voice=voice)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        path = tmp.name
    await tts.save(path)
    data, sr = sf.read(path)
    os.remove(path)
    return data, sr

# --- Generate a random laugh clip ---
async def generate_laugh(_tag="[add_laugh]"):
    # Pick a random laugh file
    path = random.choice(LAUGH_FILES)
    print(f"[LAUGH] Selected file: {path}")
    sys.stdout.flush()

    # Read file in thread to avoid blocking
    data, sr = await asyncio.to_thread(sf.read, path)
    print(f"[LAUGH] Loaded SR: {sr}")
    sys.stdout.flush()

    # Optional: resample if needed (uncomment if scipy is available)
    # target_sr = 44100
    # if sr != target_sr:
    #     from scipy.signal import resample
    #     num_samples = int(len(data) * target_sr / sr)
    #     data = resample(data, num_samples)
    #     sr = target_sr

    return data, sr

# --- Playback helper (blocking) ---
def play_audio(data, samplerate):
    sd.play(data, samplerate)
    sd.wait()

# --- Producer: enqueue fragments ---
async def producer(text, queue):
    fragments = split_and_merge(text)
    for frag in fragments:
        print(f"Enqueueing fragment: {frag}")
        if frag.strip().lower() == "[add_laugh]":
            await queue.put("[add_laugh]")
        else:
            await queue.put(frag)
    await queue.put(None)

# --- Consumer: generate & play in sequence ---
async def consumer(queue):
    frag = await queue.get()
    if frag is None:
        return

    # First fragment
    if frag == "[add_laugh]":
        data, sr = await generate_laugh()
    else:
        data, sr = await generate_tts(frag)
    playback = asyncio.create_task(asyncio.to_thread(play_audio, data, sr))

    # Prepare next
    frag = await queue.get()
    next_task = None
    if frag is not None:
        if frag == "[add_laugh]":
            next_task = asyncio.create_task(generate_laugh())
        else:
            next_task = asyncio.create_task(generate_tts(frag))
    else:
        await playback
        return

    # Loop through remaining
    while True:
        await playback
        data, sr = await next_task
        playback = asyncio.create_task(asyncio.to_thread(play_audio, data, sr))

        frag = await queue.get()
        if frag is None:
            await playback
            break
        if frag == "[add_laugh]":
            next_task = asyncio.create_task(generate_laugh())
        else:
            next_task = asyncio.create_task(generate_tts(frag))

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
    t0 = perf_counter()
    demo1 =  "This audio was generated using TTS Accelerator, It delivers natural speech [add_laugh] from extremely long texts within just a few seconds."
    demo2 = "Oh, you should have seen the look on his face! [add_laugh] He was completely surprised.[add_laugh]"
    print(demo1)
    text = "Oh, you should have seen the look on his face! [add_laugh]He was completely surprised."
    text2 = "Honestly, I wasn’t sure whether to laugh, cry, or just walk away—because, believe me, the moment he said, “Trust me, I’ve done this before,” I knew it was over. [add_laugh]Still, I stayed... maybe out of hope, or maybe just out of habit."
    text3 = "Well, I told him not to touch it—but he did, anyway. And guess what? It exploded, [add_laugh] just like in the movies. It's totally unexpected!"
    text4 = """
     Hello, my name is[add_laugh]Nisha. And, uh — and I like pizza.
"""


    print("Speaking demo...")
    speak_text(text4)
    print(demo2)
    print(f"Done in {perf_counter() - t0:.2f} sec")




