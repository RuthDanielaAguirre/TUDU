import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
from services.task_service import sendToBackend
from services.voice_action_handler import handle_voice_action
from utils.speech_utils import handle_voice_interaction
from utils.ui_utils import (
    create_toggle_icon_button,
    create_frame_s, create_icon_button
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

        self.title_label = ctk.CTkLabel(
            self, text="TUDU DASHBOARD",
            font=("Helvetica", 24, "bold"),
            text_color="#EAEAEA",
            fg_color="transparent"
        )
        self.title_label.place(relx=0.5, rely=0.08, anchor="center")

        self.task_entry = ctk.CTkEntry(
            self,
            placeholder_text="Enter a task",
            width=500,
            height=55,
            corner_radius=10,
            fg_color="#2E2E2E",
            text_color="#EAEAEA",
            border_width=2,
            border_color="#444444"
        )
        self.task_entry.place(relx=0.5, rely=0.18, anchor="center")

        icon_buttons = [
            ("assets/newTask.png", self.create_manual_task, 0.3, "Add Task"),
            ("assets/subtask.png", self.create_subtask, 0.4, "Add Subtask"),
            ("assets/cycle.png", self.create_recurring_task, 0.5, "Recurring Task"),
            ("assets/edit.png", self.edit_task, 0.6, "Edit Task"),
            ("assets/trash.png", self.delete_task, 0.7, "Delete Task"),
            ("assets/task.png", self.load_tasks_from_db, 0.8, "View Tasks")
        ]
        for path, command, relx, tooltip in icon_buttons:
            create_icon_button(self, command, path, relx, 0.28, tooltip_text=tooltip)

        self.task_box_left = create_frame_s(self, relx=0.425, rely=0.58, relwidth=0.27, relheight=0.35)
        self.task_box_right = create_frame_s(self, relx=0.725, rely=0.58, relwidth=0.27, relheight=0.35)

        self.mic_button = create_toggle_icon_button(
            master=self,
            image_on_path="assets/mic_on.png",
            image_off_path="assets/mic_off.png",
            command_on=self.handle_voice_with_feedback,
            command_off=lambda: None,
            relx=0.05,
            rely=0.05
        )

        create_toggle_icon_button(
            master=self,
            image_on_path="assets/speaker_on.png",
            image_off_path="assets/speaker_off.png",
            command_on=toggle_speaker_on,
            command_off=toggle_speaker_off,
            relx=0.95,
            rely=0.05
        )

        self.voice_indicator = ctk.CTkLabel(
            self,
            text="Listening...",
            font=("Helvetica", 12, "bold"),
            text_color="#8C7853",
            fg_color="transparent"
        )
        self.voice_indicator.place(relx=0.5, rely=0.92, anchor="center")
        self.voice_indicator.lower()

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

    def add_task_to_panel(self, text, task_type="Simple", panel="left",  task_id=None):
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

        parent_panel = self.task_box_right if panel == "right" else self.task_box_left

        label = ctk.CTkLabel(
            parent_panel,
            text=f"  {text}",
            image=icon,
            compound="left",
            font=("Helvetica", 14),
            text_color=color,
            anchor="w",
            padx=8
        )
        label.pack(pady=5, anchor="w")

        if panel == "right":
            label.bind("<Button-1>", lambda e, tid=task_id, desc=text: self.handle_task_click(tid, desc))

        label.pack(pady=5, anchor="w")

    def handle_task_click(self, task_id, description):
        popup = ctk.CTkToplevel(self)
        popup.title("Manage Task")
        popup.geometry("300x150")
        popup.grab_set()

        label = ctk.CTkLabel(popup, text=description, font=("Helvetica", 14))
        label.pack(pady=10)

        btn_edit = ctk.CTkButton(popup, text="Edit", command=lambda: self.edit_task_popup(task_id, popup))
        btn_edit.pack(pady=5)

        btn_delete = ctk.CTkButton(popup, text="Delete", command=lambda: self.delete_task(task_id, popup))
        btn_delete.pack(pady=5)

    def start_mic_animation(self):
        self.mic_blinking = True
        self.blink_mic_icon()

    def blink_mic_icon(self):
        if not self.mic_blinking:
            return
        current = self.mic_button.cget("image")
        new_image = self.mic_off_img if current == self.mic_on_img else self.mic_on_img
        self.mic_button.configure(image=new_image)
        self.after(500, self.blink_mic_icon)

    def stop_mic_animation(self):
        self.mic_blinking = False
        self.mic_button.configure(image=self.mic_on_img)

    def load_tasks_from_db(self):
        try:
            response = requests.get(f"{BACKEND_URL}/tasks/by-user/4")
            if response.status_code == 200:
                tasks = response.json()
                for widget in self.task_box_right.winfo_children():
                    widget.destroy()

                for task in tasks:
                    self.add_task_to_panel(task["description"],panel="right",task_id=task["id_task"])
        except Exception as e:
                print(f"No se pudieron cargar las tareas: {e}")

    def create_manual_task(self):
        description = self.task_entry.get()
        if description:
            sendToBackend(description=description, task_type="Simple")
            guardar_comando_en_bbdd(description, "create_task", "Simple")
            self.add_task_to_panel(description, "Simple")
            speak(get_random_phrase("confirmacion") + f": {description}")
            self.task_entry.delete(0, "end")

    def create_subtask(self):
        description = self.task_entry.get()
        if description:
            sendToBackend(description=description, task_type="Subtask")
            guardar_comando_en_bbdd(description, "create_task", "Subtask")
            self.add_task_to_panel(description, "Subtask")
            speak(get_random_phrase("confirmacion") + f": {description}")
            self.task_entry.delete(0, "end")

    def create_recurring_task(self):
        description = self.task_entry.get()
        if description:
            sendToBackend(description=description, task_type="Recurring", repeat_interval="weekly")
            guardar_comando_en_bbdd(description, "create_task", "Recurring")
            self.add_task_to_panel(description, "Recurring")
            speak(get_random_phrase("confirmacion") + f": {description}")
            self.task_entry.delete(0, "end")

    def edit_task(self, task_id, new_description, popup):
        try:
            response = requests.put(f"{BACKEND_URL}/tasks/update/{task_id}", json={"description": new_description})
            if response.status_code == 200:
                speak("Tarea actualizada.")
                popup.destroy()
                self.load_tasks_from_db()
            else:
                speak("No se pudo actualizar la tarea.")
        except Exception as e:
            print(f"Error editando tarea: {e}")

    def delete_task(self):
        speak("Tarea eliminada.")
        print("The task was successfully deleted")

    def edit_task_popup(self, task_id, popup):
        popup.destroy()

        edit_popup = ctk.CTkToplevel(self)
        edit_popup.title("Edit Task")
        edit_popup.geometry("350x200")
        edit_popup.grab_set()

        label = ctk.CTkLabel(edit_popup, text="New Description", font=("Helvetica", 14))
        label.pack(pady=10)

        entry = ctk.CTkEntry(edit_popup, width=300)
        entry.pack(pady=5)

        submit_btn = ctk.CTkButton(
            edit_popup,
            text="Save Changes",
            command=lambda: self.edit_task(task_id, entry.get(), edit_popup)
        )
        submit_btn.pack(pady=10)
