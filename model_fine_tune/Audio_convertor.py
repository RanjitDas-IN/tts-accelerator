import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment

# Path to the audio file
audio_file = ''
# Convert the AAC file to WAV format using pydub
audio = AudioSegment.from_file(audio_file, format="aac")
wav_file = ''
audio.export(wav_file, format="wav")

# Read the converted WAV file
data, samplerate = sf.read(wav_file)
sf.write(wav_file, data, samplerate)
sd.play(data, samplerate)

# Wait until the audio is finished playing
sd.wait()