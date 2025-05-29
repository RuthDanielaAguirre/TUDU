from utils.speech_utils import handle_voice_interaction
from utils.output_audio_utils import speak
from services.task_service import sendToBackend
from utils.api import guardar_comando_en_bbdd
from utils.voice_responses import get_random_phrase


URGENCIA_CLAVE = [
    "urgente", "muy urgente", "muy importante", "prioridad alta", "prioritario",
    "urgentisimo", "lo más importante", "crucial", "esencial", "importante", "vital"
]
FRECUENCIAS = ["diaria", "semanal", "mensual", "cada día", "cada semana", "cada mes"]

def detectar_urgencia(texto):
    return any(palabra in texto.lower() for palabra in URGENCIA_CLAVE)

def detectar_repeticion(texto):
    return next((f for f in FRECUENCIAS if f in texto.lower()), None)

def limpiar_descripcion(texto):
    texto = texto.lower()
    for inicio in [
        "crear tarea de", "quiero crear una tarea de", "añadir tarea de",
        "crear", "añadir", "quiero crear una tarea"
    ]:
        if inicio in texto:
            return texto.split(inicio)[-1].strip()
    return texto.strip()

def handle_create_task(dashboard):
    # Paso 1: Pedir la descripción
    speak(get_random_phrase("descripcion_tarea"))

    initial_response = None
    for _ in range(3):
        initial_response = handle_voice_interaction()
        if initial_response and "text" in initial_response and initial_response["text"].strip():

            break
        speak("No entendí la tarea, intenta de nuevo.")
    else:
        speak("No se pudo entender la tarea. Cancelando.")
        return

    texto_original = initial_response["text"].strip()

    # Paso 2: Preguntar por tipo
    speak("¿Qué tipo de tarea es: simple, subtarea o repetitiva?")

    tipo_response = None
    for _ in range(3):
        tipo_response = handle_voice_interaction()
        if tipo_response and "text" in tipo_response:
            break
        speak("No entendí el tipo, intenta de nuevo.")
    else:
        speak("No se pudo entender el tipo. Cancelando.")
        return

    tipo_texto = tipo_response["text"].lower()

    # Detectar tipo
    tipo = "Simple"
    if "subtarea" in tipo_texto:
        tipo = "Subtask"
    elif "repetitiva" in tipo_texto or "recurrente" in tipo_texto:
        tipo = "Recurring"

    # Detectar urgencia y repetición desde la frase original
    urgente = detectar_urgencia(texto_original)
    prioridad = "Alta" if urgente else "Media"
    repeticion = detectar_repeticion(texto_original)
    descripcion = limpiar_descripcion(texto_original)

    print("Descripción:", descripcion)
    print("Tipo:", tipo)
    print("Prioridad:", prioridad)
    print("Repetición:", repeticion)

    #  Validar descripción
    if descripcion.strip().lower() in ["simple", "subtarea", "repetitiva", "", "simple.", "subtarea.", "repetitiva."]:
        speak("No entendí bien la descripción de la tarea. Intenta decirlo más claro.")
        return

    sendToBackend(
        description=descripcion,
        task_type=tipo,
        prioridad=prioridad,
        repeat_interval=repeticion
    )

    guardar_comando_en_bbdd(texto_original, "create_task", tipo)
    dashboard.add_task_to_panel(descripcion, tipo)
    speak(get_random_phrase("confirmacion") + f": {descripcion}")
