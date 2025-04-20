import speech_recognition as sr

def listen_to_voice():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Say something")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            return audio
    except sr.WaitTimeoutError:
        print("Time exceeded no voice detected")
    except sr.RequestError as e:
        print(f"{e}")
    except sr.UnknownValueError:
        print("Please try again")
    except Exception as e:
        print(f"Unexpected error {e}")
    return None

if __name__ == "__main__":
    audio_data = listen_to_voice()
    if audio_data:
        print("🎧 Audio capturado correctamente.")
    else:
        print("🚫 No se pudo capturar el audio.")