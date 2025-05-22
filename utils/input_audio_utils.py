import speech_recognition as sr

is_speaker_on = True

def toggle_speaker_on():
    global is_speaker_on
    is_speaker_on = True
    print("Speaker on.")

def toggle_speaker_off():
    global is_speaker_on
    is_speaker_on = False
    print("Speaker off.")

def speaker_status():
    return is_speaker_on

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
        print(f"Request error: {e}")
    except sr.UnknownValueError:
        print("Could not understand the audio. Please try again.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

def save_audio_to_wav(audio_data, filename="user_voice.wav"):
    with open(filename, "wb") as f:
        f.write(audio_data.get_wav_data())
    print("Audio saved as", filename)
