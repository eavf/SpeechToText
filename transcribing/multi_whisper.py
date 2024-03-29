import os
from lib_whisper import vrat_subor

path_fold = "E:\\audio"
files = os.listdir(path_fold)


def mult_files():
    audio_files = [subor for subor in files if subor.endswith((".wav", ".mp3"))]
    print(audio_files)

    # Cycle all files in folder
    for audio_subor in audio_files:
        text = vrat_subor(audio_subor)
        outfile = os.path.splitext(audio_subor)[0] + ".txt"
        outadr = os.path.join(path_fold, outfile)
        with open(outadr, "w", encoding="utf-8") as vystupny_subor:
            vystupny_subor.write(text)
        # Vytlačte výsledok transkripcie.
        print(f"Súbor: {audio_subor}")
        print("Transkripcia:", text)
        print()


if __name__ == "__main__":
    print('Premenná name je :', __name__)
    mult_files()
