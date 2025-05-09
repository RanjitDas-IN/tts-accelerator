## TTS Accelerator

> Real-time natural speech generation — delivers real-time, natural speech from text in as little as 2-3 seconds, handling even extremely long sentences (16,000+ words) with instant voice output—no waiting or file saving.


This library works entirely in RAM to make speech super fast using the Edge-TTS engine. Edge-TTS sounds great, but it slows way down when you ask it to read long sentences—that was a big bottleneck for real-time apps. TTS Accelerator fixes that: it starts talking in just 2–3 seconds, even for thousands of words, by streaming audio straight from memory with no file saves or delays. Whether you’re building a chatbot or powering my AI assistant Nisha, who needs instant replies, this tool makes your app feel quick, smart, and alive.

[![PyPI version](https://badge.fury.io/py/tts-accelerator.svg)](https://pypi.org/project/tts-accelerator/)&emsp;&emsp;
[![Download](https://pepy.tech/badge/tts-accelerator)](https://pepy.tech/project/tts-accelerator)

[![Built by Uday & Ranjit](https://img.shields.io/badge/Built_by-UDAY_&_RANJIT-black?style=rounded&labelColor=blueviolet&color=lightgreen)](https://github.com/RanjitDas-IN/Nisha_rework)



Want to ask questions or share ideas?  
👉&emsp;[![](https://dcbadge.vercel.app/api/server/JVzAfRjyxV?style=flat&compact=True)](https://discord.gg/JVzAfRjyxV)
&emsp;— we're active and friendly!


💡 **Actively Developed & Maintained**: This project is continuously improved with regular updates, bug fixes, and support. You're never alone — the journey keeps moving forward! 🚀🔧
[![GitHub Repo](https://img.shields.io/badge/GitHub__Repo-black?logo=github&style=social)](https://github.com/RanjitDas-IN/tts-accelerator)

Feel free to reach out, open issues, or suggest ideas — we’re building this together. 🤝

## 📧 Ranjit: ranjitdax89@gmail.com
## 📧 Uday: udaysubba2004@gmail.com
---
## What Problem It Solves❓

Most TTS systems force you to wait while they generate the entire audio file — especially for long texts — before playback starts.

That’s slow, frustrating, and unusable for real-time apps.

*TTS Accelerator solves this by streaming audio in real time.*  
It starts playback in just 2–3 seconds, even for huge texts. No disk I/O, no waiting — just seamless, instant voice output.  
Perfect for:
- Voice assistants
- Chatbots
- Narration tools
- Live reading apps
---

## 📖 Quick Index

- [💡 Insight](#insight)
- [✨ Key Features](#key-features)
- [❓ What Problem It Solves](#what-problem-it-solves)
- [🧠Why we Made This Library](#why-we-made-this-library)
- [⬇️ Installation](#installation)
- [📚 Examples](#examples)
- [📦 Requirements](#requirements)
- [📖 Documentation](#documentation)
- [👨‍🎓 Creators](#creator)
- [📝 License (MIT)](#license)


## 💡Insight


TTS Accelerator is designed for ultra-fast playback.
Unlike typical TTS systems that wait for full audio generation, this one begins speaking within 2–3 seconds — even for texts up to 16,000+ words. It streams while generating, offering smooth, natural output with zero delay.


## ✨Key Features

- **Super Fast Speech (Real-Time TTS)**: Begins speaking in just 2–3 seconds, even for extremely long texts — up to 16,000+ words.
- **Highly Compatible**: Seamlessly works with popular TTS engines like Edge-TTS (tested), Coqui TTS etc.. 
- **Streaming Playback**: Audio starts playing instantly while it’s still being generated — no delay, no wait.
- **Minimal API**: Just a single function call to start speaking — `speak_text(text)`.
- **Zero-Delay Playback**: Audio plays with zero delay, It is a smart system that uses fast RAM-based buffering and a separate producer-consumer pipeline to keep things smooth and super quick.


## 🧠Why we Made This Library

While working on our personal AI assistant, Nisha, we (Uday Subba & Ranjit Das) ran into a huge bottleneck:  
Most TTS libraries either sounded robotic or took forever to generate long sentences — especially when trying to keep the voice natural.

We needed something *fast enough for real-time conversation* but still *clear and human-like* — and nothing we found was good enough.  
That’s why we built *TTS Accelerator*.

It streams audio from text in just seconds, even for huge inputs, and it feels natural — exactly what Nisha needed to sound like a confident and responsive AI.

> So yes — this library is not just an experiment, it powers a bigger dream.
---

> Curious about my AI assistant **Nisha**?  
> She's the reason this library was born — and she's coming soon.  
> Stay tuned on [GitHub](https://github.com/RanjitDas-IN) or [Discord](https://discord.gg/JVzAfRjyxV) for updates!


[![Meet Nisha – Your Bold AI Assistant](https://img.shields.io/badge/Nisha-AI_Assistant_in_Progress-purple?style=for-the-badge&logo=voice-over)](https://github.com/RanjitDas-IN/Nisha_rework)&emsp;
[![GitHub Repo](https://img.shields.io/badge/GitHub__Repo-black?logo=github&style=social)](https://github.com/RanjitDas-IN/Nisha_rework)


## 🔧Installation

You can install it from [PyPI](https://pypi.org/project/tts-accelerator/) by running the following command:

```
pip install tts-accelerator
```

Or you can install it from [source](https://github.com/RanjitDas-IN/tts-accelerator): 

```
pip install .
```
or
```bash
git clone https://github.com/RanjitDas-IN/tts-accelerator.git
cd tts-accelerator/example_uses
python basic_uses.py
```
Explore the TTS Accelerator [Source Code](https://github.com/RanjitDas-IN/tts-accelerator)


## 📚Examples

Simple Usage:

```python
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
# it will generate the audio in less than 3 seconds regardless of number of lines in the 'text variable'
```


## 📦Requirements

- Python **_v3.8+_**
- A stable internet connection

## 📖Documentation

https://tts-accelerator.readthedocs.io/



## 🤝 Support & Contribution

Have questions or ideas to improve the project? We’re building this together!

- **Discord Support**: [Join our active community](https://discord.gg/JVzAfRjyxV)
- **Open Issues**: [GitHub Issues Page](https://github.com/RanjitDas-IN/tts-accelerator/issues)
- **Source Code**: [GitHub Repository](https://github.com/RanjitDas-IN/tts-accelerator)
- **Email**: ranjitdax89@gmail.com

We welcome bug reports, feature requests, or maybe a quick hello if you're enjoying the project!
---
## Creators
Built and maintained by 
[**Uday Subba**](https://github.com/kisxo) & [**Ranjit Das**](https://github.com/RanjitDas-IN)

**Made with passion and precision.**

## 📝License

This project is licensed under MIT.
## CTA:
Try it now and tell us what you build!
## 🔮 About Nisha (Coming Soon)

**Nisha** is my personal AI assistant — sassy, smart, and ultra-fast.  
She’s designed to handle real-time conversations with confidence and clarity, and tts-accelerator is one of the core techs that power her voice.

Want to follow her journey or be the first to try her out?

- GitHub Updates: [RanjitDas-IN](https://github.com/RanjitDas-IN/Nisha_rework)
- Chat on Discord: [Join the community](https://discord.gg/JVzAfRjyxV)


