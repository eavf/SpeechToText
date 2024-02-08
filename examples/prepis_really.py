import torch
import os
from transformers import pipeline


def prepis(audio='1EN.mp3', cesta="E:\\audio", max_n_t=2500):
    audio_path = os.path.join(cesta, audio)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    if 'FR' in audio:
        print('prepis - pouzivam FR! - ', audio)
        # Ak je to french audio
        # Load pipeline
        pipe = pipeline("automatic-speech-recognition", model="bofenghuang/whisper-large-v2-french", device=device)
        # NB: set forced_decoder_ids for generation utils
        pipe.model.config.forced_decoder_ids = pipe.tokenizer.get_decoder_prompt_ids(language="fr", task="transcribe")
        generated_sentences = pipe(audio_path, max_new_tokens=max_n_t)["text"]  # greedy
        print(generated_sentences)
        return generated_sentences
    elif 'NL' in audio:
        print('prepis - pouzivam NL! - ', audio)
        # Ak je to NL audio
    elif 'EN' in audio:
        # Ak je to anglický string
        print('prepis - pouzivam EN! - ', audio)
        # Load pipeline
        pipe = pipeline("automatic-speech-recognition", model="openai/whisper-large", device=device)
        # NB: set forced_decoder_ids for generation utils
        pipe.model.config.forced_decoder_ids = pipe.tokenizer.get_decoder_prompt_ids(language="en", task="transcribe")
        generated_sentences = pipe(audio_path, max_new_tokens=225)["text"]
        return generated_sentences
    else:
        print('Nie je znak jazyka..... exiting')


def vrat_subor(audio='1EN.mp3', cesta="E:\\audio"):
    subor = os.path.join(cesta, audio)
    if os.path.isfile(subor):
        try:
            return prepis(audio=subor, cesta=cesta)
        except Exception as e:
            print(f"Chyba pri transkripcii súboru {subor}: {str(e)}")


print(vrat_subor())
