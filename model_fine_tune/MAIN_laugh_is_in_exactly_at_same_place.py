"""Believe me, it takes a lot of sleepless nights. Even Seems Easier 😖😖😖"""

"""
Streaming TTS Accelerator with Laugh Integration
- Greedy split: isolate [add_laugh] at exact position
- Concurrently generate/play fragments for seamless audio
"""
import asyncio
import os
import re
import random
import tempfile
import time 
import threading
import edge_tts     # 2.00 sec (with generator + streaming)
import numpy as np  # 2.50 sec (with old version)
import sounddevice as sd
import soundfile as sf

# --- Configuration ---
LAUGH_TAG = "[add_laugh]"
LAUGH_DIR = "/home/ranjit/TTS-Accelerator/wav_audio"
TARGET_SR = 22050
TTS_VOICE = "en-US-AvaMultilingualNeural"

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


# ---Old Greedy Split & Merge ---
# def split_and_merge(text: str, min_words: int = 5) -> list[str]:
#     """
#     Greedily splits text, isolating LAUGH_TAG at exact position.
#     Emits fragments by walking through text without looking far ahead.
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

#         next_is_laugh = idx + 1 < len(parts) and parts[idx + 1] == LAUGH_TAG
#         if next_is_laugh:
#             fragments.append(chunk)
#             continue

#         chunk2 = re.sub(r"\.(?=[A-Za-z])", ". ", chunk)
#         parts2 = re.split(r'(?<=[,\.!?])\s*', chunk2)
#         buf = []
#         for part in parts2:
#             part = part.strip()
#             if not part:
#                 continue
#             buf.append(part)
#             joined = " ".join(buf)
#             if len(joined.split()) >= min_words:
#                 fragments.append(joined)
#                 buf = []
#         if buf:
#             fragments.append(" ".join(buf))

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
        chunk = re.sub(r'(?<=[,.!?])(?=[^\s])', ' ', chunk)
        fragments = re.split(r'(?<=[.!?…])\s+', chunk)
        buf = []
        for frag in fragments:
            frag = frag.strip()
            if not frag:
                continue
            buf.append(frag)
            joined = ' '.join(buf)
            if len(joined.split()) >= min_words:
                yield joined.strip()
                buf = []
        if buf:
            yield ' '.join(buf).strip()



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

# # ---Old Streaming Speak ---
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


# generator streaming version
async def speak_stream(text: str):
    queue = asyncio.Queue()
    split_iter = iter(split_and_merge(text))

    async def producer():
        try:
            while True:
                frag = next(split_iter)
                print(f"\033[0;34m[DEBUG] Generating → {frag}\033[0m")

                if frag == LAUGH_TAG:
                    data, sr = await load_laugh()
                else:
                    data, sr = await generate_tts(frag)
                await queue.put((data, sr))
        except StopIteration:
            await queue.put(None)  # signal end

    async def consumer():
        while True:
            item = await queue.get()
            if item is None:
                break
            data, sr = item
            sd.play(data, sr)
            sd.wait()

    await asyncio.gather(producer(), consumer())
# --- Public API ---
def speak_text(text: str):
    asyncio.run(speak_stream(text))

def background_speak(text):
    speak_text(text)


# --- Demo ---

if __name__ == '__main__':
    from time import perf_counter
    start_time = perf_counter() 
    demo = (
        "how many of you got very excited after hearing the word AI? [add_laugh] This audio is being generated with laughs seamlessly injected! [add_laugh] so Enjoy!"
    )

    text1 =  "This audio was generated using TTS Accelerator, It delivers natural speech [add_laugh] from extremely long texts within just a few seconds."
  
    text = "You see, it’s not just that he said, “I can fix it,”—it’s how he said it: with a grin, a shrug, and that eerie pause… [add_laugh]Then the lights flickered, the alarms went off, and, without warning—boom!"

    text2 = "Honestly, I wasn’t sure whether to laugh, cry, or just walk away—because, believe me, the moment he said, “Trust me, I’ve done this before,” I knew it was over. [add_laugh]Still, I stayed, maybe out of hope, or maybe just out of habit."
    print("Speaking demo...")






    
    # Start TTS in a new thread
    t = threading.Thread(target=background_speak, args=(text1,))
    t.start()

    print(f"\033[1;32mAccess{text1} Granted!\033[0m")

    t.join()





 # Measure the end time
    end_time = perf_counter()
    # Print the time taken
    print(f"Time taken: {end_time - start_time:.2f} seconds")