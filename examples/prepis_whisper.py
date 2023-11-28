import os
import whisper

audio_path = os.path.join(os.path.dirname(__file__), "../data/EarningsCall.wav")

model = whisper.load_model("base.en")
result = model.transcribe(audio_path)
print(result["text"])