import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
from utils.ui_utils import create_frame_s, create_button, create_entry_with_label, show_error_label, create_back_button

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, back_to_home_callback):
        super().__init__(master)
        self.master = master
        self.back_to_home_callback = back_to_home_callback
        self.error_label = None

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.imagen_original = Image.open("assets/HomeVoice.png")
        imagen_tk = CTkImage(light_image=self.imagen_original, size=(screen_width, screen_height))

        self.fondo = ctk.CTkLabel(self, image=imagen_tk, text="")
        self.fondo.image = imagen_tk
        self.fondo.place(x=0, y=0, relwidth=1, relheight=1)

        self.login_frame = create_frame_s(self, relx=0.35, rely=0.2, relwidth=0.3, relheight=0.6)

        font_size = int(screen_height * 0.05)
        self.title_label = ctk.CTkLabel(self.login_frame, text="Login", font=("Helvetica", font_size, "bold"), text_color="#EAEAEA")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        self.username_entry = create_entry_with_label(self.login_frame, "Username", 0.5, 0.35)
        self.password_entry = create_entry_with_label(self.login_frame, "Password", 0.5, 0.55, is_password=True)

        self.login_button = create_button(self.login_frame, "Submit", self.process_login, 0.5, 0.8)

        self.bind("<Configure>", self.resize_image)

        self.back_button = create_back_button(self.login_frame, "←", self.volver_atras, 0.1, 0.08)

    def resize_image(self, event):
        nueva_imagen = CTkImage(light_image=self.imagen_original, size=(event.width, event.height))
        self.fondo.configure(image=nueva_imagen)
        self.fondo.image = nueva_imagen

    def process_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.error_label:
            self.error_label.destroy()
            self.error_label = None

        if username == "" or password == "":
            self.error_label = show_error_label(self.login_frame, "Please enter valid information.")
        else:
            print("✅ Login enviado")
            self.after(10, self.master.show_dashboard)

    def volver_atras(self):
        self.master.show_home()