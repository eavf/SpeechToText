import os
import whisper


def chunk_audio(audio, chunk_length_sec=30, overlap_sec=5, sample_rate=16000):
    chunk_size = chunk_length_sec * sample_rate
    overlap_size = overlap_sec * sample_rate
    start = 0
    while start < len(audio):
        end = min(start + chunk_size, len(audio))
        yield audio[start:end]
        start = end - overlap_size

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio_path = os.path.join(os.path.dirname(__file__), "../data/EarningsCall.wav")
audio = whisper.load_audio(audio_path)
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)

full_transcript = ""
for chunk in chunk_audio(audio):
    mel = whisper.log_mel_spectrogram(chunk).to(model.device)
    result = model.transcribe(mel)
    full_transcript += result["text"] + " "

print(full_transcript)
