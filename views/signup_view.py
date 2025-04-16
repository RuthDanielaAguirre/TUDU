import customtkinter as ctk

class SignupFrame(ctk.CTkFrame):
    def __init__(self, master, back_callback):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="Signup Screen (en construcción)", font=("Helvetica", 20))
        self.label.pack(pady=40)
        self.back_btn = ctk.CTkButton(self, text="Back", command=back_callback)
        self.back_btn.pack()
