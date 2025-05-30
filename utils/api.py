from dotenv import load_dotenv
import os
import requests

load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL")


def send_audio_get_transcription(audio_path):
    url = f"{BACKEND_URL}/voice/transcribe"

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
            url = f"{BACKEND_URL}/commands/log",
            json={
                "phrase": phrase,
                "action": action,
                "type": tipo
            }
        )
        if response.status_code != 200:
            print("No se pudo guardar el comando:", response.text)
    except Exception as e:
        print("Error al enviar el comando:", e)


def eliminar_tarea_por_descripcion(descripcion, id_user=4):
    try:
        response = requests.delete(
            url=f"{BACKEND_URL}/tasks/delete-by-description",
            json={
                "description": descripcion,
                "id_user": id_user
            }
        )
        if response.status_code == 200:
            print("area eliminada del backend.")
            return True
        else:
            print("Error al eliminar tarea:", response.text)
            return False
    except Exception as e:
        print("Excepción al eliminar tarea:", e)
        return False

def update_task_description(old_desc, new_desc):
    try:
        response = requests.put(
            url=f"{BACKEND_URL}/tasks/update-description",
            json={
                "old_description": old_desc,
                "new_description": new_desc
            }
        )
        return response.status_code == 200
    except Exception as e:
        print("Error actualizando tarea:", e)
        return False


