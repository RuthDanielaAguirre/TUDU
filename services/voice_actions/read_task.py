from utils.output_audio_utils import speak
from utils.voice_responses import get_random_phrase

FRASES_LECTURA = [
    "leer tareas",
    "dime mis tareas",
    "qué tengo que hacer",
    "qué tareas tengo pendientes",
    "qué tengo para hoy",
    "qué tareas tengo",
    "qué me falta"
]

def handle_read_tasks(dashboard, texto):
    if any(frase in texto.lower() for frase in FRASES_LECTURA):
        dashboard.load_tasks_from_db()
        speak(get_random_phrase("leer_tareas"))
        return True
    return False
