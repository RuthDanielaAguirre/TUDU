import customtkinter as ctk
from views.home_view import HomeFrame
from views.login_view import LoginFrame
from views.signup_view import SignupFrame
from views.dashboard_view import DashboardFrame

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TUDU")

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{self.screen_width}x{self.screen_height}")

        self.current_frame = None
        self.show_home()

    def clear_frame(self):
     if self.current_frame:
        try:
            self.current_frame.pack_forget()
            self.current_frame.place_forget()
            self.current_frame.destroy()  
        except Exception as e:
            print("⚠️ Error destruyendo frame:", e)
        self.current_frame = None

    def show_home(self):
        self.clear_frame()
        self.current_frame = HomeFrame(self, self.show_login, self.show_signup)
        self.current_frame.pack(fill="both", expand=True)

    def show_login(self):
        self.clear_frame()
        self.current_frame = LoginFrame(self, self.show_home)
        self.current_frame.pack(fill="both", expand=True)

    def show_signup(self):
        self.clear_frame()
        self.current_frame = SignupFrame(self, self.show_home)
        self.current_frame.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.clear_frame()  
        self.current_frame = DashboardFrame(self) 
        self.current_frame.pack(fill="both", expand=True)  


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
