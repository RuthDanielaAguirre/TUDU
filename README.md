# 🌟 TUDU — Tu asistente de tareas por voz

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-green?logo=fastapi)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue?logo=mysql)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-GUI-purple)
![Figma](https://img.shields.io/badge/Figma-Design-red?logo=figma)
![Whisper](https://img.shields.io/badge/Whisper-Voice%20AI-black)
![gTTS](https://img.shields.io/badge/gTTS-Speech-yellow?logo=google)

---

## 🧠 Proyecto ABP DAM · 1º curso · Monlau FP

---

## ✨ ¿Qué es TUDU?

TUDU no es una simple lista de tareas.  
Es una **experiencia interactiva** que combina diseño, voz e inteligencia para ayudarte a gestionar tu día sin escribir ni una palabra.

> Todo comenzó con una pregunta:  
> _“¿Y si pudiéramos hablar con nuestras tareas?”_

Así nació TUDU: una app de escritorio hecha en Python con **CustomTkinter**, un backend en **FastAPI** y una base de datos **MySQL**, con una fuerte base en diseño UX.

---

## 🎨 Diseño en Figma

Antes de escribir una sola línea de código, trabajamos en Figma para definir:

- 🧱 **Wireframes de baja fidelidad**
- 🎨 Paleta visual: tonos oscuros con acento dorado (#121212, #D4AF37)
- 🧠 Flujo emocional del usuario
- 🗣️ Prototipos con simulación de comandos de voz

<sub>🔽 Aquí puedes insertar una imagen del prototipo:</sub>  
![Prototipo Figma](assets/screenshots/figma_mockup.png)

---

## 🗣️ ¿Qué puede hacer TUDU?

- Escuchar tus comandos con Whisper 
- Crear tareas por voz (simples, recurrentesy proximamente subtareas)
- Consultar y crear tareas solo con hablar
- Detectar prioridad o urgencia automáticamente
- Aprender de tus comandos frecuentes

---

## 🚀 Endpoints del Backend (FastAPI)

### `/tasks`
- `POST /tasks/create` — Crear tarea
- `GET /tasks/by-user/{id_user}` — Obtener tareas
- `PUT /tasks/update/{id_task}` — Editar tarea
- `DELETE /tasks/delete/{id_task}` — Eliminar tarea

### `/voice`
- `POST /voice/transcribe` — Transcribir audio
- `POST /voice/action` — Ejecutar acción

### `/commands`
- `POST /commands/save` — Guardar comando
- `GET /commands/by-user/{id_user}` — Ver historial

---

## ⚙️ Stack tecnológico

| Categoría        | Herramienta                   | Descripción                                         |
|------------------|-------------------------------|-----------------------------------------------------|
| 🎨 UI            | CustomTkinter                 | Interfaz moderna con soporte dark mode              |
| 🎤 Voz           | Whisper / SpeechRecognition   | Procesamiento de comandos hablados                  |
| 🗣️ Voz a texto   | gTTS + pygame                 | Respuestas habladas generadas desde Python          |
| 🚀 Backend       | FastAPI                       | API ligera y rápida en Python                       |
| 🛢 Base de datos | MySQL                          | Almacenamiento estructurado de usuarios y tareas    |
| 🧠 UX            | Figma                         | Diseño visual y flujo emocional del usuario         |

---

## 👥 Equipo

- Ruth Daniela Aguirre
- Alizon Rosales
- Gael Martinez

---

## 🎯 Conclusión

TUDU es más que un proyecto técnico.  
Es una propuesta para una productividad más accesible, emocional e inteligente.

> _“No queremos que solo hagas tareas. Queremos que hables con ellas.”_



