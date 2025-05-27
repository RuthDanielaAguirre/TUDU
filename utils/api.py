import requests

API_BASE = "http://localhost:8000"

def send_audio_get_transcription(audio_path):
    url = f"{API_BASE}/voice/transcribe"

    with open(audio_path, 'rb') as f:
        files = {'file': ('user_voice.wav', f, 'audio/wav')}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            return response.json().get("text", "")
        else:
            return None

def guardar_comando_en_bbdd(phrase, action=None, tipo=None):
    try:
        response = requests.post(
            url = f"{API_BASE}/voice/log",
            json={
                "phrase": phrase,
                "action": action,
                "type": tipo
            }
        )
        if response.status_code != 200:
            print("⚠️ No se pudo guardar el comando:", response.text)
    except Exception as e:
        print("❌ Error al enviar el comando:", e)
