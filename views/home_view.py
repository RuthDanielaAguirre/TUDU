import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
from utils.ui_utils import create_button

class HomeFrame(ctk.CTkFrame):
    def __init__(self, master, login_callback, signup_callback):
        super().__init__(master)
        self.master = master
        self.login_callback = login_callback
        self.signup_callback = signup_callback

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        font_size = int(self.screen_height * 0.05)
        self.imagen_original = Image.open("assets/HomeVoice.png")
        self.imagen_tk = CTkImage(light_image=self.imagen_original, size=(self.screen_width, self.screen_height))

        self.fondo = ctk.CTkLabel(self, image=self.imagen_tk, text="")
        self.fondo.image = self.imagen_tk
        self.fondo.place(x=0, y=0, relwidth=1, relheight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="   Welcome to TUDU  ",
            font=("Helvetica", font_size, "bold"),
            text_color="#EAEAEA",
            fg_color="#2E2E2E"
        )
        self.title_label.place(relx=0.2, rely=0.4, anchor="center")

        self.login_button = create_button(self, "Login", self.login_callback, 0.2, 0.5)
        self.signup_button = create_button(self, "Signup", self.signup_callback, 0.2, 0.6)

        self.bind("<Configure>", self.resize_image)

    def resize_image(self, event):
        nueva_img = self.imagen_original.resize((event.width, event.height))
        nueva_tk = CTkImage(light_image=nueva_img, size=(event.width, event.height))
        self.fondo.configure(image=nueva_tk)
        self.fondo.image = nueva_tk
