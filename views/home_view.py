import customtkinter as ctk
from PIL import Image, ImageTk
from utils.ui_utils import create_frame_s

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class HomeView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TUDU")



        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        imagen = Image.open("assets/HomeVoice.png")
        imagen_tk = ImageTk.PhotoImage(imagen)

        self.fondo = ctk.CTkLabel(self, image=imagen_tk, text="")
        self.fondo.image = imagen_tk
        self.fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # Resize
        self.bind("<Configure>", self.resize_image)

        #LoginFrame
        self.login_frame = create_frame_s(
            self,
            relx=0.05,
            rely=0.2,
            relwidth=0.25,
            relheight=0.6
        )

    def resize_image(self, event):
        imagen = Image.open("assets/HomeVoice.png")
        imagen = imagen.resize((event.width, event.height))
        imagen_tk = ImageTk.PhotoImage(imagen)

        self.fondo.configure(image=imagen_tk)
        self.fondo.image = imagen_tk



if __name__ == "__main__":
    app = HomeView()
    app.mainloop()