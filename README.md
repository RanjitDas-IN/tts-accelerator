# TTS-Accelarator

> *Real-time speech generation in seconds, even for extremely long sentences up to 16k words.*

---
## Demo

Listen the sample output to listen to the sample MP3 output

   
<details open>


<audio controls>
  <source src="wav_audio/Laugh1.wav" type=mp3>
Your browser does not support the audio element.
</audio>


</details>


---
TTS-Accelerator is a revolutionary text-to-speech acceleration framework that allows real-time audio generation and playback — even for extremely long texts (up to 16,000 characters) — in just a few seconds.  
Unlike traditional TTS systems which wait for full generation before playback, TTS-Accelerator *splits, **generates, and **plays* audio simultaneously — ensuring ultra-fast startup and continuous natural speech.

---

## Key Features

- *Real-Time TTS*: Speak extremely long texts within 2–3 seconds startup.
- *Compatible with Any Library*: Works with local TTS engines (like Edge-TTS) and even API-based services (like ElevenLabs, Typecast.ai, etc.).
- *Streaming Playback*: **Audio starts playing while it is still being generated.**
- *Library-Independent Core*: Easily pluggable with your preferred TTS backend.
- *Minimal API*: Just one function call to start speaking — speak_text(text).

---

## How It Works

Internally, TTS-Accelerator:

1. Comming Soon
2. Comming Soon
3. Comming Soon

---

## Installation

For now, clone the GitHub repository:

1. Clone the repository:
```bash
git clone https://github.com/RanjitDas-IN/TTS-Accelerator.git
cd tts_accelarator  # the actual path

pip install -r requirements.txt

python3 tts_accelarator.py #adjust this
```

> Note: PyPI is also available

## Example Uses



2. Install required dependencies:

```bash
pip install tts_accelarator
```

3. Example Code:

```python
import tts_accelarator as tts
from time import perf_counter


def main():



if _name_ == "_main_":
    text = (
        """Hello, 'TTS-Accelerator' achieves near-instant speech generation. 
        converting extremely long texts (up to 16 thousand + characters)
        into natural voices, high-quality audio within just 2–3 seconds,
        delivering breakthrough real-time performance without sacrificing
        voice clarity. Thank you!!"""

    )
    tts.speak_text(text)
    # it will generate the audio in less then 3 seconds regardless of number of lines in the 'text'

```


---

License

This project is licensed under a custom license created by the author(Ranjit).
Please refer to the attached [LICENSE file](LICENSE) for more details.


---

Credits

Made with passion and precision.