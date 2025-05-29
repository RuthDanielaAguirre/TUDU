import random

def get_random_phrase(tipo):
    frases = {
        "inicio": [
            "Hola, ¿qué quieres hacer?",
            "¿Qué necesitas hoy?",
            "Dime, ¿qué hacemos?",
            "¿En qué te puedo ayudar?",
            "Listo, dime qué quieres hacer"
        ],
        "tipo_tarea": [
            "¿Qué tipo de tarea es: simple, subtarea o repetitiva?",
            "¿Cómo clasificarías esta tarea simple, subtarea o repetitiva?",
            "¿Es una tarea simple, una subtarea o una repetitiva?",
            "Elige el tipo de tarea: simple, subtarea o repetitiva"
        ],
        "confirmacion": [
            "Tarea registrada",
            "Tu nota ha sido añadida",
            "He guardado tu idea",
            "Tarea añadida",
            "Perfecto, lo he apuntado"
        ],
        "leer_tareas": [
            "Estas son tus tareas pendientes:",
            "Vamos a ver qué te queda por hacer:",
            "Aquí tienes tus tareas:",
            "Esto es lo que tienes anotado:"
        ],
        "eliminar_tarea": [
            "¿Quieres eliminar una tarea o una subtarea?",
            "Dime si vas a eliminar una tarea principal o una subtarea.",
            "¿La tarea que vas a borrar es principal o subtarea?"
        ],
        "eliminar_nombre": [
            "¿Cómo se llama la tarea que quieres eliminar?",
            "Dime el nombre de la tarea que vamos a borrar.",
            "¿Cuál es la tarea que deseas eliminar?"
        ],
        "eliminar_subtarea": [
            "¿De qué tarea depende la subtarea que quieres eliminar?",
            "¿Cuál es la tarea padre de esta subtarea?",
            "Dime la tarea principal a la que pertenece la subtarea."
        ],
        "modificar": [
            "¿Qué tarea o subtarea quieres modificar?",
            "Dime qué quieres cambiar.",
            "¿Qué vas a editar hoy?"
        ],
        "modificar_que": [
            "¿Qué cambio quieres hacer en ella?",
            "¿Qué parte deseas modificar?",
            "Indícame qué debo cambiar."
        ],
        "accion_no_reconocida": [
            "No entendí eso, ¿puedes decirlo de otra forma?",
            "Perdona, no reconocí la acción. ¿Quieres intentarlo de nuevo?",
            "Esa opción no está disponible. Intenta decirlo de otra manera.",
        ]
    }

    return random.choice(frases.get(tipo, ["..."]))