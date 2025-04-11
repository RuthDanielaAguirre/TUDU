import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
from utils.ui_utils import create_button

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class HomeView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TUDU")

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width}x{self.screen_height}")

        font_size = int(self.screen_height * 0.05)
        self.imagen_original = Image.open("assets/HomeVoice.png")
        self.imagen_tk = CTkImage(light_image=self.imagen_original, size=(self.screen_width, self.screen_height))

        # Fondo
        self.fondo = ctk.CTkLabel(self, image=self.imagen_tk, text="")
        self.fondo.image = self.imagen_tk
        self.fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # Título
        self.title_label = ctk.CTkLabel(
            self,
            text="   Welcome to TUDU  ",
            font=("Helvetica", font_size, "bold"),
            text_color="#EAEAEA",
            fg_color="#2E2E2E"
        )
        self.title_label.place(relx=0.2, rely=0.4, anchor="center")

        # Botones
        self.login_button = create_button(self, "Login", self.open_login, 0.2, 0.5)
        self.signup_button = create_button(self, "Signup", self.signup_frame, 0.2, 0.6)

        # Hacer la imagen responsive
        self.bind("<Configure>", self.resize_image)

    def resize_image(self, event):
        nueva_img = self.imagen_original.resize((event.width, event.height))
        nueva_tk = CTkImage(light_image=nueva_img, size=(event.width, event.height))
        self.fondo.configure(image=nueva_tk)
        self.fondo.image = nueva_tk

    def open_login(self):
        self.after(100, self._open_safe_login)

    def _open_safe_login(self):
        self.destroy()
        from views.login_view import LoginView
        LoginView().mainloop()

    def signup_frame(self):
        print("→ In Signup")

if __name__ == "__main__":
    app = HomeView()
    app.mainloop()
