import customtkinter as ctk
from views.login_view import LoginFrame
from views.signup_view import SignupFrame
from views.home_view import HomeView

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TUDU")
        self.state("zoomed")  # Pantalla completa en Windows
        self.current_frame = None
        self.show_login()

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def show_login(self):
        self.clear_frame()
        self.current_frame = LoginFrame(self, self.show_signup, self.show_home)
        self.current_frame.pack(fill="both", expand=True)

    def show_signup(self):
        self.clear_frame()
        self.current_frame = SignupFrame(self, self.show_login)
        self.current_frame.pack(fill="both", expand=True)

    def show_home(self, username):
        self.clear_frame()
        self.current_frame = HomeView(self, username)
        self.current_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()