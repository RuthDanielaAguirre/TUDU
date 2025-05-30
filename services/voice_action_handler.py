from services.voice_actions.create_task import handle_create_task
from services.voice_actions.read_task import handle_read_tasks
from services.voice_actions.delete_task import handle_delete_task
from services.voice_actions.update_task import handle_update_task

from utils.output_audio_utils import speak
from utils.speech_utils import handle_voice_interaction
from utils.voice_responses import get_random_phrase

def handle_voice_action(response, dashboard):
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        if not isinstance(response, dict):
            speak("No entendí, ¿puedes repetirlo?")
            response = handle_voice_interaction()
            attempts += 1
            continue

        action = response.get("action", "").lower()

        if action in ("create_task", "await_task_type"):
            handle_create_task(dashboard)
            break
        elif action == "read_tasks":
            text = response.get("text", "")
            handle_read_tasks(dashboard, text)
            break
        elif action == "delete_task":
            text = response.get("text", "")
            handle_delete_task(dashboard, text)
            break
        elif action == "update_task":
            text = response.get("text", "")
            handle_update_task(dashboard, text)
            break
        elif "cancelar" in response.get("text", "").lower():
            speak("Vale, cancelamos la acción.")
            break
        else:
            speak(get_random_phrase("accion_no_reconocida"))
            response = handle_voice_interaction()
            attempts += 1

    if attempts == max_attempts:
        speak("Demasiados intentos. Cancelando la acción.")
