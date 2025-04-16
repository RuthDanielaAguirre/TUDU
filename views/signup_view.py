import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage, CTkComboBox
from utils.ui_utils import (
    create_entry_with_label,
    create_button,
    create_frame_s,
    create_back_button,
    create_datepicker_with_label
)

class SignupFrame(ctk.CTkFrame):
    def __init__(self, master, back_to_home_callback):
        super().__init__(master)
        self.master = master
        self.back_to_home_callback = back_to_home_callback
        self.error_label = None

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.imagen_original = Image.open("assets/HomeVoice.png")
        self.imagen_tk = CTkImage(light_image=self.imagen_original, size=(screen_width, screen_height))

        self.fondo = ctk.CTkLabel(self, image=self.imagen_tk, text="")
        self.fondo.image = self.imagen_tk
        self.fondo.place(x=0, y=0, relwidth=1, relheight=1)

        self.signup_frame = create_frame_s(
            self,
            relx=0.35,
            rely=0.1,
            relwidth=0.3,
            relheight=0.75,
            fondo_base="transparent"
        )

        self.scrollable = ctk.CTkScrollableFrame(self.signup_frame, fg_color="transparent")
        self.scrollable.pack(expand=True, fill="both", padx=10, pady=10)

        self.title_label = ctk.CTkLabel(
            self.scrollable,
            text="Signup",
            font=("Helvetica", 28, "bold"),
            text_color="#EAEAEA",
            fg_color="transparent"
        )
        self.title_label.pack(pady=(0, 20))

        font_label = ("Helvetica", 14)

        self.profile_label = ctk.CTkLabel(self.scrollable, text="Select a profile type", font=font_label, text_color="#EAEAEA")
        self.profile_label.pack(pady=(0, 5))
        self.profile_combo = CTkComboBox(self.scrollable, values=["Student", "Work", "Both"], width=220, state="readonly")
        self.profile_combo.pack(pady=(0, 15))

        self.gender_label = ctk.CTkLabel(self.scrollable, text="Select a gender", font=font_label, text_color="#EAEAEA")
        self.gender_label.pack(pady=(0, 5))
        self.gender_combo = CTkComboBox(self.scrollable, values=["Male", "Female"], width=220, state="readonly")
        self.gender_combo.pack(pady=(0, 15))

        self.birthdate = create_datepicker_with_label(self.scrollable, "Birthdate", 0.5, 0.0)
        self.birthdate.pack(pady=(10, 20), anchor="center")

        self.email_entry = create_entry_with_label(self.scrollable, "Email", 0.5, 0.0)
        self.email_entry.pack(pady=(10, 10))
        self.username_entry = create_entry_with_label(self.scrollable, "Username", 0.5, 0.0)
        self.username_entry.pack(pady=(10, 10))
        self.password_entry = create_entry_with_label(self.scrollable, "Password", 0.5, 0.0, is_password=True)
        self.password_entry.pack(pady=(10, 10))

        self.signup_button = create_button(self.scrollable, "Signup", self.process_signup, 0.5, 0.0)
        self.signup_button.pack(pady=(10, 20))

        self.back_button = create_back_button(self.signup_frame, "←", self.back_to_home_callback, 0.10, 0.08)

        self.bind("<Configure>", self.resize_image)
        self.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.lift()

    def resize_image(self, event):
        nueva_img = self.imagen_original.resize((event.width, event.height))
        nueva_tk = CTkImage(light_image=nueva_img, size=(event.width, event.height))
        self.fondo.configure(image=nueva_tk)
        self.fondo.image = nueva_tk

    def process_signup(self):
        if self.error_label:
            self.error_label.destroy()
            self.error_label = None

        profile = self.profile_combo.get()
        gender = self.gender_combo.get()
        birthdate = self.birthdate.get()
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if (profile == "" or profile == "Select a profile type" or
                gender == "" or gender == "Select a gender" or
                birthdate == "" or
                email.strip() == "" or
                username.strip() == "" or
                password.strip() == ""):

            print("Empty information")
        else:
            print("✅ Signup completed (fake success for now)")