import speech_recognition as sr

def listen_to_voice():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Please speak now...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            return audio
    except sr.WaitTimeoutError:
        print("⏱️ Timeout: no voice detected.")
    except sr.RequestError as e:
        print(f"🔌 Request error: {e}")
    except sr.UnknownValueError:
        print("❓ Could not understand the audio. Please try again.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
    return None

def save_audio_to_wav(audio_data, filename="user_voice.wav"):
    with open(filename, "wb") as f:
        f.write(audio_data.get_wav_data())
    print("💾 Audio saved as", filename)
