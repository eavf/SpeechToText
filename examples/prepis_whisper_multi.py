import os
import whisper

model_fr = whisper.load_model("base.fr")
model_nl = whisper.load_model("base.nl")
model_en = whisper.load_model("base.en")

model = whisper.Model()
model.merge(model_fr)
model.merge(model_nl)
model.merge(model_en)

# Cestou k priečinku so zvukovými súbormi.
cesta_k_priecinku = "E:\\audio"

# Získať zoznam súborov v zadanom priečinku.
subory = os.listdir(cesta_k_priecinku)

# Vytvorte zoznam len s audio súbormi (s koncovkou '.wav' alebo inou, ktorú používate).
audio_subory = [subor for subor in subory if subor.endswith((".wav", ".mp3"))]


# Prejdite všetky súbory v priečinku.
for audio_subor in audio_subory:
    # Vytvorte úplnú cestu k aktuálnemu súboru.
    cesta_k_suboru = os.path.join(cesta_k_priecinku, audio_subor)

    # Skontrolujte, či ide o súbor (nie priečinok).
    if os.path.isfile(cesta_k_suboru):
        try:
            # Transkribujte audio zo súboru.
            vysledok = model.transcribe(cesta_k_suboru)

            # Vytvorte názov výstupného súboru s rovnakým menom ako vstupný súbor, ale s príponou '.txt'.
            outfile = os.path.splitext(audio_subor)[0] + ".txt"
            # Vytvorte úplnú cestu k výstupnému súboru.
            outadr = os.path.join(cesta_k_priecinku, outfile)

            # Uložte transkripciu do výstupného súboru.
            with open(outadr, "w", encoding="utf-8") as vystupny_subor:
                vystupny_subor.write(vysledok["text"])

            # Vytlačte výsledok transkripcie.
            print(f"Súbor: {audio_subor}")
            print("Transkripcia:", vysledok["text"])
            print()
        except Exception as e:
            print(f"Chyba pri transkripcii súboru {audio_subor}: {str(e)}")