import whisper

model = whisper.load_model("base")
result = model.transcribe("..//tests//jfk.flac")
print(result["text"])