import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
from utils.ui_utils import create_frame_s, create_button, create_entry_with_label

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - TUDU")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        self.imagen_original = Image.open("assets/HomeVoice.png")
        imagen_tk = CTkImage(light_image=self.imagen_original, size=(screen_width, screen_height))

        self.fondo = ctk.CTkLabel(self, image=imagen_tk, text="")
        self.fondo.image = imagen_tk
        self.fondo.place(x=0, y=0, relwidth=1, relheight=1)

        self.login_frame = create_frame_s(
            self,
            relx=0.35,
            rely=0.2,
            relwidth=0.3,
            relheight=0.6,
            fondo_base="#1F1F1F"
        )

        font_size = int(screen_height * 0.05)
        self.title_label = ctk.CTkLabel(
            self.login_frame,
            text="Login",
            font=("Helvetica", font_size, "bold"),
            text_color="#EAEAEA",
            fg_color="transparent"
        )
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        self.username_entry = create_entry_with_label(self.login_frame, "Username", 0.5, 0.35)
        self.password_entry = create_entry_with_label(self.login_frame, "Password", 0.5, 0.55, is_password=True)

        self.login_button = create_button(self.login_frame, "Submit", self.procesar_login, 0.5, 0.8)

        self.bind("<Configure>", self.resize_image)

    def resize_image(self, event):
        nueva_imagen = CTkImage(light_image=self.imagen_original, size=(event.width, event.height))
        self.fondo.configure(image=nueva_imagen)
        self.fondo.image = nueva_imagen

    def procesar_login(self):
        print("✅ Login enviado")

if __name__ == "__main__":
    app = LoginView()
    app.mainloop()
