import os
from dotenv import load_dotenv
import requests

from utils.input_audio_utils import listen_to_voice, save_audio_to_wav
from utils.output_audio_utils import speak


load_dotenv()

def send_audio(filename):
    try:
        with open(filename, "rb") as f:
            files = {
                "file": (filename, f, "audio/wav")
            }
            backend_url = os.getenv("BACKEND_URL")
            endpoint = f"{backend_url}/voice/transcribe"
            response = requests.post(endpoint, files=files)
            print("Audio sent successfully.")
            print("Server response:", response.text)
            return response.json()
    except Exception as e:
        print("Error sending audio:", e)
        return{"error": str(e)}

def handle_voice_interaction():
    audio = listen_to_voice()
    if audio:
        filename = "user_voice.wav"
        save_audio_to_wav(audio, filename)
        response = send_audio(filename)

        if response and "text" in response:
            text =  response["text"]
            speak(text)

            create_keywords = ["crear","crea", "anota", "anotar", "hacer", "haz", "apuntar", "apunta", "escribe", "new"]
            if any(word in text.lower() for word in create_keywords):
                return {
                    "action": "await_task_type",
                    "text":  text,
                }
            return {"text": text}

    return {"error": "No audio"}


if __name__ == "__main__":
    send_audio("user_voice.wav")


