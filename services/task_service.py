import os
import requests
from dotenv import load_dotenv
from utils.output_audio_utils import speak

load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL")

# Mapeo de tipo de tarea a ID
TYPE_MAP = {
    "Simple": 1,
    "Subtask": 2,
    "Recurring": 3
}

# Mapeo de prioridad a ID
PRIORITY_MAP = {
    "Baja": 1,
    "Media": 2,
    "Alta": 3
}

def sendToBackend(description, task_type="Simple", prioridad="Media", repeat_interval=None):
    id_type_task = TYPE_MAP.get(task_type)
    id_tag_task = PRIORITY_MAP.get(prioridad)

    if not id_type_task:
        error_message = "Tipo de tarea inválido."
        print(error_message)
        speak("No reconocí el tipo de tarea, intenta de nuevo.")
        return False

    if not id_tag_task:
        id_tag_task = 2

    data = {
        "description": description,
        "id_user": 4,  # ← usuario fijo de prueba
        "id_type_task": id_type_task,
        "id_tag_task": id_tag_task,
        "repeat_interval": repeat_interval
    }

    print("Sending al backend:", data)

    try:
        response = requests.post(f"{BACKEND_URL}/tasks/create", json=data)
        response.raise_for_status()
        print("Task saved")
        return True
    except requests.RequestException as e:
        print(f"Error saving task: {e}")
        speak("Ocurrió un error al guardar la tarea, por favor intenta otra vez.")
        return False
