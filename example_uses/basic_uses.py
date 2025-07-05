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
# Speak the text — playback starts almost instantly
tts.speak_text(demo)
# tts.speak_text(text)


