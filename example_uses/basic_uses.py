"""Introducing *TTS-Accelerator* — a groundbreaking innovation designed to supercharge text-to-speech generation.  
It delivers *ultra-fast speech synthesis, capable of converting even extremely long texts (up to 16,000+ characters) into natural-sounding audio in just **2–3 seconds*.  
Under the hood, it currently leverages *edge-tts* for processing, but the core design is *library-independent, meaning it can be easily integrated with any TTS system — including external API-based services like **Typecast.ai, **ElevenLabs*, and more.  
This accelerator pushes the limits of real-time TTS generation without sacrificing voice quality, making it ideal for advanced, high-performance applications."""

"""
Developed by Ranjit Das. I've use the best algorithms and the most efficient data structures to achieve fast real-time speech generation.
"""

import tts_accelarator as tts
from time import perf_counter


if __name__ == "__main__":
# ────────────────────────────────────────────────────  Measure the time taken ────────────────────────────────────────────────────────────────────── 
    # Measure the time taken for the entire process
    start_time = perf_counter()

#──────────────────────────────────────────────────── Initialize the TTS Accelerator ────────────────────────────────────────────────────────────────
    # Define the text to be spoken
    text = "Hello, 'TTS-Accelerator' achieves near-instant speech generation. converting extremely long texts (up to 16 thousand + characters) into natural voices, high-quality audio within just 2–3 seconds, delivering breakthrough real-time performance without sacrificing voice clarity."

    # Call the speak_text function to process and play the audio
    tts.speak_text(text)

# ──────────────────────────────────────────────────────  Measure the time taken ────────────────────────────────────────────────────────────────────
    # Measure the end time
    end_time = perf_counter()
    # Print the time taken
    print(f"Time taken: {end_time - start_time:.2f} seconds")
# ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


import tts_accelarator as tts
from time import perf_counter

if __name__ == "__main__":
    start_time = perf_counter()

    # Define the text to be spoken
    text = "Hello, 'TTS-Accelerator' achieves near-instant speech generation. converting extremely long texts (up to 16 thousand + characters) into natural voices, high-quality audio within just 2–3 seconds, delivering breakthrough real-time performance without sacrificing voice clarity."

    # Call the speak_text function to process and play the audio
    tts.speak_text(text)

    # Measure the end time
    end_time = perf_counter()
    # Print the time taken
    print(f"Time taken: {end_time - start_time:.2f} seconds")


