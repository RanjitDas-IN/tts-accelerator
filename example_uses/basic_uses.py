"""Introducing *TTS-Accelerator* — a groundbreaking innovation designed to supercharge text-to-speech generation.  
It delivers *ultra-fast speech synthesis, capable of converting even extremely long texts (up to 16,000+ characters) into natural-sounding audio in just **2–3 seconds*.  
Under the hood, it currently leverages *edge-tts* for processing, but the core design is *library-independent, meaning it can be easily integrated with any TTS system — including external API-based services like **Typecast.ai, **ElevenLabs*, and more.  
This accelerator pushes the limits of real-time TTS generation without sacrificing voice quality, making it ideal for advanced, high-performance applications."""

"""
Developed by Ranjit Das. I've use the best algorithms (producer, consumer pipeline) and the most efficient data structures to achieve fast real-time speech generation.
"""

# Import the library
import tts_accelerator as tts

# Example long text to demonstrate real-time speech generation.
text = (
    "Imagine reading out a 1,000-word story or a chatbot message stream — "
    "normally, you'd wait several seconds or even minutes before hearing anything. "
    "But with tts-accelerator, audio playback begins in just 2–3 seconds, "
    "no matter how long the input is. It streams audio directly from RAM, "
    "without saving to disk, and keeps the voice natural and fluid throughout. "
    "This makes it perfect for assistants, narrators, or any real-time voice-based apps."
)

# Speak the text — playback starts almost instantly
tts.speak_text(text)
# it will generate the audio in less then 3 seconds regardless of number of lines in the 'text variable'


