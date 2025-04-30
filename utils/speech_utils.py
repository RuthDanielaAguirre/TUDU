import os
from dotenv import load_dotenv
import requests
import speech_recognition as sr

load_dotenv()

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
    print("💾 Audio saved as user_voice.wav")

def send_audio(filename):
    try:
        with open(filename, "rb") as f:
            files = {
                "file": (filename, f, "audio/wav")
            }
            backend_url = os.getenv("BACKEND_URL")
            endpoint = f"{backend_url}/upload-audio"
            response = requests.post(endpoint, files=files)
            print("✅ Audio sent successfully.")
            print("📨 Server response:", response.text)
    except Exception as e:
        print("🚫 Error sending audio:", e)

if __name__ == "__main__":
    recorded_audio = listen_to_voice()
    if recorded_audio:
        print("🎧 Audio successfully captured.")
        save_audio_to_wav(recorded_audio)
        send_audio("user_voice.wav")
    else:
        print("🚫 Audio capture failed.")
