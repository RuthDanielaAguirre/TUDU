import requests

def send_audio_get_transcription(audio_path):
    url = "http://localhost:8000/voice/transcribe"

    with open(audio_path, 'rb') as f:
        files = {'file': ('user_voice.wav', f, 'audio/wav')}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            return response.json().get("text", "")
        else:
            return None
