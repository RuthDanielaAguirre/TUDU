import os
from dotenv import load_dotenv
import requests


load_dotenv()

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
            return response.json()
    except Exception as e:
        print("🚫 Error sending audio:", e)
        return{"error": str(e)}


if __name__ == "__main__":
    send_audio("user_voice.wav")


