import os
import whisper

def prepis(audio = 'HLFR1.mp3', cesta="E:\\audio", max_n_t = 2500):
    audio_path = os.path.join(cesta, audio)
    if 'FR' in audio:
        print('prepis - pouzivam FR! - ', audio)
        # Ak je to french audio
        model = whisper.load_model("medium")
        result = model.transcribe(audio_path)
        #print(result["text"])
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
        try:
            return prepis(audio=subor, cesta=cesta)
        except Exception as e:
            print(f"Chyba pri transkripcii súboru {subor}: {str(e)}")





