import difflib
import os
import whisper


def compare_strings(string1, string2):
    try:
        # Ensure the strings are in the correct format
        string1 = str(string1)
        string2 = str(string2)

        # Compare the strings
        diff = difflib.ndiff(string1, string2)

        # Print the differences
        print(''.join(diff))
    except Exception as e:
        print(f"An error occurred: {e}")



def transpis (txt="../data/EarningsCall.wav"):
    audio_path = os.path.join(os.path.dirname(__file__), txt)
    model = whisper.load_model("base.en")
    return model.transcribe(audio_path)