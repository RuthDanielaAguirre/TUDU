import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
from services.task_service import sendToBackend
from services.voice_action_handler import handle_voice_action
from utils.speech_utils import handle_voice_interaction
from utils.ui_utils import (
    create_button,
    create_toggle_icon_button,
    create_frame_s
)
from utils.input_audio_utils import toggle_speaker_on, toggle_speaker_off
from utils.output_audio_utils import speak
from utils.api import guardar_comando_en_bbdd
from utils.voice_responses import get_random_phrase
import requests
from utils.api import BACKEND_URL


class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(fg_color="#121212")

        self.mic_on_img = CTkImage(Image.open("assets/mic_on.png"), size=(24, 24))
        self.mic_off_img = CTkImage(Image.open("assets/mic_off.png"), size=(24, 24))

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
        self.mic_button = create_toggle_icon_button(
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
        self.start_mic_animation()

        response = handle_voice_interaction()

        start = get_random_phrase("inicio")
        speak(start)

        response = handle_voice_interaction()

        self.stop_mic_animation()
        self.voice_indicator.lower()

        if response:
            handle_voice_action(response, self)

    def handle_create_task(dashboard):
        speak(get_random_phrase("tipo_tarea"))
        response = handle_voice_interaction()

        if not response or "text" not in response:
            speak("No entendí el tipo de tarea")
            return

        tipo = "Simple"
        if "subtarea" in response["text"].lower():
            tipo = "Subtask"
        elif "repetitiva" in response["text"].lower():
            tipo = "Recurring"

        texto = dashboard.pending_task_text if hasattr(dashboard, 'pending_task_text') else response["text"]

        # Guardar en BBDD
        sendToBackend(texto, tipo)
        guardar_comando_en_bbdd(texto, "create_task", tipo)

        dashboard.add_task_to_panel(texto, tipo)

        speak(get_random_phrase("confirmacion") + f": {texto}")

    def add_task_to_panel(self, text, task_type="Simple"):
        color = "#8C7853"
        icon_path = "assets/default.png"

        if task_type == "Simple":
            color = "#4A90E2"
            icon_path = "assets/task.png"
        elif task_type == "Subtask":
            color = "#50E3C2"
            icon_path = "assets/subtask.png"
        elif task_type == "Recurring":
            color = "#F5A623"
            icon_path = "assets/cycle.png"

        icon = CTkImage(Image.open(icon_path), size=(20, 20))

        label = ctk.CTkLabel(
            self.task_box_left,
            text=f" {text}",
            image=icon,
            compound="left",
            font=("Helvetica", 14),
            text_color=color,
            anchor="w"
        )
        label.pack(pady=5, anchor="w")

    def start_mic_animation(self):
        self.mic_blinking = True
        self.blink_mic_icon()

    def blink_mic_icon(self):
        if not self.mic_blinking:
            return
        current = self.mic_button.cget("image")
        new_image = self.mic_off_img if current == self.mic_on_img else self.mic_on_img
        self.mic_button.configure(image = new_image)
        self.after(500, self.blink_mic_icon)

    def stop_mic_animation(self):
        self.mic_blinking = False
        self.mic_button.configure(image = self.mic_on_img)

    def load_tasks_from_db(self):
        try:
            response = requests.get(f"{BACKEND_URL}/tasks/by-user/1")
            if response.status_code == 200:
                tasks = response.json()
                for task in tasks:
                    self.add_task_to_panel(task["description"], "Simple")
        except:
            print("No se pudieron cargar las tareas.")
