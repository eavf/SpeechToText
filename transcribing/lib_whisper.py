import os
import time, datetime
import whisper
from pydub import AudioSegment
import pandas as pd
import nltk
nltk.download("punkt")

from nltk.tokenize import sent_tokenize


GEN_KWARGS = {
    "task": "transcribe",
    "language": "fr",
    #"without_timestamps": False,
    # decode options
    # "beam_size": 5,
    # "patience": 2,
    # disable fallback
    # "compression_ratio_threshold": None,
    # "logprob_threshold": None,
    # vad threshold
    # "no_speech_threshold": None,
}

def get_audio_length(audio_file_path):
    try:
        audio = AudioSegment.from_file(audio_file_path)
        length_in_seconds = len(audio) / 1000  # Length in seconds (milliseconds to seconds)
        return length_in_seconds
    except Exception as e:
        print(f"Error: {e}")
        return None

def format_timestamp(seconds):
    return str(datetime.timedelta(seconds=round(seconds)))

def infer(model, filename, with_timestamps, return_df=False):
    if with_timestamps:
        # model_outputs = model.transcribe(filename, **GEN_KWARGS)
        model_outputs, _ = model.transcribe(filename, **GEN_KWARGS)
        model_outputs = [segment._asdict() for segment in model_outputs]
        print('modeloutputs in infer()')
        print(model_outputs)
        if return_df:
            # model_outputs_df = pd.DataFrame(model_outputs["segments"])
            model_outputs_df = pd.DataFrame(model_outputs)
            # print(model_outputs)
            # print(model_outputs_df)
            # print(model_outputs_df.info(verbose=True))
            model_outputs_df = model_outputs_df[["start", "end", "text"]]
            model_outputs_df["start"] = model_outputs_df["start"].map(format_timestamp)
            model_outputs_df["end"] = model_outputs_df["end"].map(format_timestamp)
            model_outputs_df["text"] = model_outputs_df["text"].str.strip()
            return model_outputs_df
        else:
            return "\n\n".join(
                [
                    f'Segment {segment["id"]+1} from {segment["start"]:.2f}s to {segment["end"]:.2f}s:\n{segment["text"].strip()}'
                    # for segment in model_outputs["segments"]
                    for segment in model_outputs
                ]
            )
    else:
        # text = model.transcribe(filename, without_timestamps=True, **GEN_KWARGS)["text"]
        model_outputs, _ = model.transcribe(filename, without_timestamps=True, **GEN_KWARGS)
        text = " ".join([segment.text for segment in model_outputs])
        if return_df:
            return pd.DataFrame({"text": sent_tokenize(text)})
        else:
            return text


def prepis(audio = 'HLFR1.mp3', cesta="E:\\audio", max_n_t = 2500):
    audio_path = os.path.join(cesta, audio)
    if 'FR' in audio:
        print('prepis - pouzivam FR! - ', audio)
        # Ak je to french audio
        t0 = time.time()
        model = whisper.load_model("medium")
        with_timestamps = True
        t1 = time.time()
        print(t1)
        result = infer(model, audio_path, with_timestamps, return_df=False)
        #result = model.transcribe(audio_path, **GEN_KWARGS)
        t2 = time.time()
        print(t2)
        #print(result["text"])
        rozdiel_casu1 = t1 - t0
        rozdiel_casu = t2 - t1
        # Rozdiel času v sekundách
        print(f"Rozdiel času: {rozdiel_casu1} a {rozdiel_casu} sekundy")
        print('Dlzka nahravky je (s)', get_audio_length(cesta))
        return result['text']
    elif 'NL' in audio:
        print('prepis - pouzivam NL! - ', audio)
        model = whisper.load_model("medium")
        result = model.transcribe(audio_path)
        #print(result["text"])
        return result['text']
    elif 'EN' in audio:
        # Ak je to anglický string
        print('prepis - pouzivam EN! - ', audio)
        model = whisper.load_model("medium")
        result = model.transcribe(audio_path)
        #print(result["text"])
        return result['text']
    else:
        print('Nie je znak jazyka..... exiting')

def vrat_subor(audio = 'HLFR1.mp3', cesta="E:\\audio"):
    subor = os.path.join(cesta, audio)
    if os.path.isfile(subor):
        return prepis(audio=subor, cesta=cesta)



