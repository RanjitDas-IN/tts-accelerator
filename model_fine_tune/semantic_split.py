"""Take 3 sec but fully grammertically correct each split"""
"""No metters how many line in the paregragh (upto 16k lines) """




"""Believe me, it takes a lot of sleepless nights. Even Seems Easier 😖😖😖

Streaming TTS Accelerator with Laugh Integration
- Greedy split: isolate [add_laugh] at exact position
- Concurrently generate/play fragments for seamless audio

"""
import asyncio
import os
import re
import random
import tempfile
import spacy        #time 2.5 sec
import edge_tts
import numpy as np
import sounddevice as sd
import soundfile as sf

# --- Configuration ---

# PAUSE_TAG = """   —  \n  \n  """
LAUGH_TAG = "[add_laugh]"
LAUGH_DIR = "/home/ranjit/TTS-Accelerator/wav_audio"
TARGET_SR = 22050
TTS_VOICE = "en-US-AvaMultilingualNeural"
nlp = spacy.load("en_core_web_sm")


# Preload pre-converted mono WAV laugh files
try:
    LAUGH_FILES = [
        os.path.join(LAUGH_DIR, f)
        for f in os.listdir(LAUGH_DIR)
        if f.lower().startswith("laugh") and f.lower().endswith(".wav")
    ]
    if not LAUGH_FILES:
        raise FileNotFoundError
except Exception as e:
    raise RuntimeError("❌ No laugh audio files found in the directory!") from e


# --- Greedy Split & Merge ---

# def split_and_merge(text: str, min_words: int = 5) -> list[str]:
#     """
#     Splits text intelligently while preserving [add_laugh] tags.
#     Uses spaCy to ensure fragments are grammatically sound.
#     Short fragments are merged if needed.
#     """
#     parts = re.split(rf"({re.escape(LAUGH_TAG)})", text)
#     fragments: list[str] = []

#     for idx, chunk in enumerate(parts):
#         chunk = chunk.strip()
#         if not chunk:
#             continue

#         if chunk == LAUGH_TAG:
#             fragments.append(chunk)
#             continue

#         # Use spaCy to parse and split into sentences/phrases
#         doc = nlp(chunk)
#         buffer = []

#         for sent in doc.sents:
#             sentence = sent.text.strip()
#             if not sentence:
#                 continue
#             buffer.append(sentence)
#             joined = " ".join(buffer).strip()

#             # Emit when sufficient words collected
#             if len(joined.split()) >= min_words:
#                 fragments.append(joined)
#                 buffer = []

#         # Handle remaining short buffer (if any)
#         if buffer:
#             fragments.append(" ".join(buffer).strip())

#     return fragments

# generator verson
def split_and_merge(text: str, min_words: int = 5):
    parts = re.split(rf"({re.escape(LAUGH_TAG)})", text)
    for chunk in parts:
        chunk = chunk.strip()
        if not chunk:
            continue
        if chunk == LAUGH_TAG:
            yield chunk
            continue
        doc = nlp(chunk)
        buf = []
        for sent in doc.sents:
            s = sent.text.strip()
            if not s:
                continue
            buf.append(s)
            merged = " ".join(buf)
            if len(merged.split()) >= min_words:
                yield merged
                buf = []
        if buf:
            yield " ".join(buf).strip()



# --- TTS Generation ---
async def generate_tts(text: str) -> tuple[np.ndarray, int]:
    tts = edge_tts.Communicate(text, voice=TTS_VOICE)
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp:
        path = tmp.name
    await tts.save(path)
    data, sr = sf.read(path)
    os.remove(path)
    if data.ndim > 1:
        data = data.mean(axis=1)
    if sr != TARGET_SR:
        length = int(len(data) * TARGET_SR / sr)
        data = np.interp(
            np.linspace(0, len(data), length),
            np.arange(len(data)), data
        )
        sr = TARGET_SR
    return data, sr

# --- Laugh Loader ---
async def load_laugh() -> tuple[np.ndarray, int]:

    path = random.choice(LAUGH_FILES)
    print("Imported Audio:\t",path)

    data, sr = await asyncio.to_thread(sf.read, path)
    if data.ndim > 1:
        data = data.mean(axis=1)
    if sr != TARGET_SR:
        length = int(len(data) * TARGET_SR / sr)
        data = np.interp(
            np.linspace(0, len(data), length),
            np.arange(len(data)), data
        )
        sr = TARGET_SR
    return data, sr 

# --- Streaming Speak ---
# async def speak_stream(text: str):
#     fragments = split_and_merge(text)
#     tasks: list[asyncio.Task] = []

#     for frag in fragments:
#         print(f"[DEBUG] Fragment → '{frag}'")
#         if frag == LAUGH_TAG:
#             tasks.append(asyncio.create_task(load_laugh()))
#         else:
#             tasks.append(asyncio.create_task(generate_tts(frag)))

#     for task in tasks:
#         data, sr = await task
#         sd.play(data, sr)
#         sd.wait()


#generator streaming version
async def speak_stream(text: str):
    for frag in split_and_merge(text):
        print(f"[DEBUG] Fragment → '{frag}'")
        if frag == LAUGH_TAG:
            data, sr = await load_laugh()
        else:
            data, sr= await generate_tts(frag)
        sd.play(data, sr)
        sd.wait()

# --- Public API ---
def speak_text(text: str):
    asyncio.run(speak_stream(text))

# --- Demo ---

if __name__ == '__main__':
    from time import perf_counter
    start_time = perf_counter() 

    text1 =  "This audio was generated using TTS Accelerator, It delivers natural speech [add_laugh] from extremely long texts within just a few seconds."
    
    text3 = "Well, I told him not to touch it—but he did, anyway. [add_laugh] And guess what? It exploded, just like in the movies... totally unexpected!"
    
    text2 = "Honestly, I wasn’t sure whether to laugh, cry, or just walk away—because, believe me, the moment he said, “Trust me, I’ve done this before,” I knew it was over. [add_laugh]Still, I stayed... maybe out of hope, or maybe just out of habit."
    print("Speaking demo...")
    speak_text(text1)
    print("Demo complete.")
 # Measure the end time
    end_time = perf_counter()
    # Print the time taken
    print(f"Time taken: {end_time - start_time:.2f} seconds")