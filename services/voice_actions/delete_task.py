from utils.output_audio_utils import speak
from utils.speech_utils import handle_voice_interaction
from utils.api import eliminar_tarea_por_descripcion
from utils.voice_responses import get_random_phrase

DELETE_KEYWORDS = [
    "elimina", "borra", "quita", "suprime", "borra la tarea", "elimina la tarea"
]

def handle_delete_task(dashboard, texto):
    descripcion = None

    if texto:
        for frase in DELETE_KEYWORDS:
            if frase in texto.lower():
                descripcion = texto.lower().replace(frase, "").strip()
                break

    if not descripcion:
        speak("¿Qué tarea quieres eliminar?")
        for _ in range(3):
            respuesta = handle_voice_interaction()
            if respuesta and "text" in respuesta:
                descripcion = respuesta["text"]
                break

    if descripcion:
        eliminado = eliminar_tarea_por_descripcion(descripcion)
        if eliminado:
            dashboard.load_tasks_from_db()
            speak(f"Tarea eliminada: {descripcion}")
        else:
            speak("No encontré esa tarea.")
    else:
        speak("No entendí qué tarea eliminar.")
