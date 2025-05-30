from utils.output_audio_utils import speak
from utils.speech_utils import handle_voice_interaction
from utils.api import update_task_description


UPDATE_KEYWORDS = [
    "modifica", "actualiza","actualizar", "cambia", "cambiar", "edita", "modificar", "editar"
]

def handle_update_task(dashboard, texto):
    descripcion_original = None

    if texto:
        for frase in UPDATE_KEYWORDS:
            if frase in texto.lower():
                descripcion_original = texto.lower().replace(frase, "").strip()
                break

    if not descripcion_original:
        speak("¿Qué tarea quieres modificar?")
        for _ in range(3):
            respuesta = handle_voice_interaction()
            if respuesta and "text" in respuesta:
                descripcion_original = respuesta["text"]
                break

    if not descripcion_original:
        speak("No entendí qué tarea modificar.")
        return

    speak("¿Cuál es la nueva descripción?")
    nueva_descripcion = None
    for _ in range(3):
        respuesta = handle_voice_interaction()
        if respuesta and "text" in respuesta:
            nueva_descripcion = respuesta["text"]
            break

    if nueva_descripcion:
        actualizado = update_task_description(descripcion_original, nueva_descripcion)
        if actualizado:
            dashboard.load_tasks_from_db()
            speak(f"Tarea actualizada: {nueva_descripcion}")
        else:
            speak("No encontré esa tarea para modificar.")
    else:
        speak("No entendí la nueva descripción.")
