import os
import whisper

audio_path = os.path.join(os.path.dirname(__file__), "../data/ADC1.mp3")

model = whisper.load_model("base.en")
result = model.transcribe(audio_path)
print(result["text"])

with open('../data/ADC1.txt', 'w') as f:
    f.write(result["text"])