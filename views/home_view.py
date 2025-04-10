import customtkinter as ctk
from PIL import Image, ImageTk
from utils.ui_utils import create_button

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class HomeView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TUDU")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        font_size = int(screen_height * 0.05)

        imagen = Image.open("assets/HomeVoice.png")
        imagen_tk = ImageTk.PhotoImage(imagen)

        self.fondo = ctk.CTkLabel(self, image=imagen_tk, text="")
        self.fondo.image = imagen_tk
        self.fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # Resize
        self.bind("<Configure>", self.resize_image)

        self.title_label =  ctk.CTkLabel(
            self,
            text = "   Welcome to TUDU  ",
            font=("Helvetica", font_size, "bold"),
            text_color="#EAEAEA",
            fg_color="#2E2E2E"
        )

        self.title_label.place(relx=0.2, rely=0.4,anchor="center")

    # Buttons
        self.login_button = create_button(self, "Login", self.login_frame, 0.2, 0.5)
        self.signup_button = create_button(self, "Signup", self.signup_frame, 0.2, 0.6)

    def resize_image(self, event):
        imagen = Image.open("assets/HomeVoice.png")
        imagen = imagen.resize((event.width, event.height))
        imagen_tk = ImageTk.PhotoImage(imagen)

        self.fondo.configure(image=imagen_tk)
        self.fondo.image = imagen_tk

    def login_frame(self):
        print("→ New Login")

    def signup_frame(self):
        print("→ In Signup ")



if __name__ == "__main__":
    app = HomeView()
    app.mainloop()