import customtkinter as ctk
from utils.speech_utils import handle_voice_interaction
from utils.ui_utils import (
    create_button,
    create_toggle_icon_button,
    create_frame_s
)
from utils.input_audio_utils import toggle_speaker_on, toggle_speaker_off
from utils.output_audio_utils import speak
import random

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(fg_color="#121212")

        # Title
        self.title_label = ctk.CTkLabel(
            self, text="TUDU DASHBOARD",
            font=("Helvetica", 24, "bold"),
            text_color="#EAEAEA",
            fg_color="transparent"
        )
        self.title_label.place(relx=0.5, rely=0.08, anchor="center")

        #Filters
        self.selected_filter = ctk.StringVar(value="Pending")
        self.pending_btn = self.create_filter_button("Pending", 0.3)
        self.completed_btn = self.create_filter_button("Completed", 0.5)
        self.all_btn = self.create_filter_button("All", 0.7)

        self.task_entry = ctk.CTkEntry(
            self,
            placeholder_text="Enter a task",
            width=300,
            height=40,
            corner_radius=10,
            fg_color="#2E2E2E",
            text_color="#EAEAEA",
            border_width=2,
            border_color="#444444"
        )
        self.task_entry.place(relx=0.5, rely=0.24, anchor="center")  # subido un poco

        #muestra las tareas
        self.task_box_left = create_frame_s(self, relx=0.25, rely=0.42, relwidth=0.3, relheight=0.35)
        self.task_box_right = create_frame_s(self, relx=0.75, rely=0.42, relwidth=0.3, relheight=0.35)

        #typesofTask
        create_button(self, "Simple", lambda: print("Tipo: Simple"), 0.3, 0.72)
        create_button(self, "Subtask", lambda: print("Tipo: Subtask"), 0.5, 0.72)
        create_button(self, "Recurring", lambda: print("Tipo: Recurring"), 0.7, 0.72)

        #tareaButton
        self.create_button = ctk.CTkButton(
            self,
            text="Create Task",
            width=150,
            height=40,
            corner_radius=10,
            fg_color="#8C7853",
            hover_color="#A58C63",
            text_color="#EAEAEA",
            command=lambda: print("Crear tarea")
        )
        self.create_button.place(relx=0.5, rely=0.82, anchor="center")

        #microphone
        create_toggle_icon_button(
            master=self,
            image_on_path="assets/mic_on.png",
            image_off_path="assets/mic_off.png",
            command_on=self.handle_voice_with_feedback,
            command_off=lambda: None,
            relx=0.05,
            rely=0.05
        )

        #speaker
        create_toggle_icon_button(
            master=self,
            image_on_path="assets/speaker_on.png",
            image_off_path="assets/speaker_off.png",
            command_on=toggle_speaker_on,
            command_off=toggle_speaker_off,
            relx=0.95,
            rely=0.05
        )

        #recordingIndicator
        self.voice_indicator = ctk.CTkLabel(
            self,
            text="Listening...",
            font=("Helvetica", 12, "bold"),
            text_color="#8C7853",
            fg_color="transparent"
        )
        self.voice_indicator.place(relx=0.5, rely=0.92, anchor="center")
        self.voice_indicator.lower()  

        self.update_filter_styles()

    def create_filter_button(self, text, relx):
        button = ctk.CTkButton(
            self,
            text=text,
            width=100,
            height=40,
            corner_radius=10,
            fg_color="#2E2E2E",
            border_width=2,
            border_color="#EAEAEA",
            text_color="#EAEAEA",
            hover_color="#8C7853",
            command=lambda: self.set_filter(text)
        )
        button.place(relx=relx, rely=0.13, anchor="center")
        return button

    def set_filter(self, value):
        self.selected_filter.set(value)
        self.update_filter_styles()

    def update_filter_styles(self):
        selected = self.selected_filter.get()
        for button, name in [
            (self.pending_btn, "Pending"),
            (self.completed_btn, "Completed"),
            (self.all_btn, "All")
        ]:
            if name == selected:
                button.configure(fg_color="#8C7853")
            else:
                button.configure(fg_color="#2E2E2E")

    def handle_voice_with_feedback(self):
        
        self.voice_indicator.lift()

        frases_inicio = [
            "Hola, ¿qué quieres hacer?",
            "¿Qué necesitas hoy?",
            "Dime, ¿qué hacemos?",
            "¿En qué te puedo ayudar?",
            "Listo, dime qué quieres hacer"
        ]
        speak(random.choice(frases_inicio))

        response = handle_voice_interaction()
        self.voice_indicator.lower()

        if isinstance(response, dict):
            action = response.get("action")

            if action == "await_task_type":
                self.pending_task_text = response["text"]

                frases_tipo = [
                    "¿Qué tipo de tarea es: simple, subtarea o repetitiva?",
                    "¿Cómo clasificarías esta tarea?",
                    "¿Es una tarea normal, una subtarea o una repetitiva?",
                    "Elige el tipo de tarea: simple, subtarea o repetitiva"
                ]
                speak(random.choice(frases_tipo))

                self.voice_indicator.lift()
                follow_up = handle_voice_interaction()
                self.voice_indicator.lower()

                task_type = "Simple"
                if "subtarea" in follow_up.get("text", "").lower():
                    task_type = "Subtask"
                elif "repetitiva" in follow_up.get("text", "").lower():
                    task_type = "Recurring"

                self.add_task_to_panel(self.pending_task_text, task_type)

                frases_confirmacion = [
                    "Tarea registrada",
                    "Tu nota ha sido añadida",
                    "He guardado tu idea",
                    "Tarea añadida",
                    "Perfecto, lo he apuntado"
                ]
                speak(f"{random.choice(frases_confirmacion)}: {self.pending_task_text}")

            elif action == "create_task":
                task_text = response.get("text", "")
                task_type = response.get("type", "Simple")
                self.add_task_to_panel(task_text, task_type)

                frases_confirmacion = [
                    "Tarea registrada",
                    "Tu nota ha sido añadida",
                    "He guardado tu idea",
                    "Tarea añadida",
                    "Perfecto, lo he apuntado"
                ]
                speak(f"{random.choice(frases_confirmacion)}: {task_text}")


    def add_task_to_panel(self,text, task_type="Simple"):
        task_label = ctk.CTkLabel(
            self.task_box_left,
            text=f"{task_type}: {text}",
            font=("Helvetica", 14),
            text_color="#EAEAEA",
            anchor="w"
        )
        task_label.pack(pady=5, anchor="w")
