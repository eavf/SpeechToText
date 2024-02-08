import os
import whisper


audio_path = os.path.join(os.path.dirname(__file__), "..\\data\\1EN.mp3")

#model = whisper.load_model("base.en")
model = whisper.load_model("medium")
result = model.transcribe(audio_path)
print(result["text"])

with open('..\\data\\1EN.txt', 'w', encoding="utf-8") as f:
    f.write(result["text"])