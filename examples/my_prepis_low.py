import os
import whisper
import math
from porovnaj_TXT import *


#os.environ['CUDA_LAUNCH_BLOCKING'] = "1"

"""
Ešte má muchy, treba sa pohrať s overlaping....

"""

import torch

def chunk_audio(aud, chunk_length_sec=30, overlap_sec=5, sample_rate=16000):
    chunk_size = chunk_length_sec * sample_rate
    overlap_size = overlap_sec * sample_rate
    start = 0
    while start + overlap_size < len(aud):  # Ensure that we have enough audio for the next chunk
        end = min(start + chunk_size, len(aud))
        chunk = aud[start:end]
        if len(chunk) < chunk_size:
            # Pad the last chunk with zeros if it's shorter than the chunk size
            padding_size = chunk_size - len(chunk)
            padding = torch.zeros(padding_size)
            chunk = torch.cat((torch.tensor(chunk), padding))  # Convert chunk to tensor before concatenation
        else:
            chunk = torch.tensor(chunk)  # Convert chunk to tensor
        yield chunk
        start = end - overlap_size
        if end == len(aud):  # Break the loop if we have reached the end of the audio
            break



#model = whisper.load_model("base", device="cpu")
model = whisper.load_model("base")

audio_path = os.path.join(os.path.dirname(__file__), "../data/EarningsCall.wav")
audio = whisper.load_audio(audio_path)
#audio = whisper.pad_or_trim(audio)  # Optional, based on your audio length

full_transcript = ""
for chunk in chunk_audio(audio):
    mel = whisper.log_mel_spectrogram(chunk).to(model.device)

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    #print(result.text)
    full_transcript += result.text + " "

compare_strings(full_transcript, transpis())

print('Low level transcript: /n', full_transcript)
print('Transcript: /n', transpis())