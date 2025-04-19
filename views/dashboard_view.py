import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
from utils.ui_utils import (create_entry_with_label, create_button, create_frame_s, create_datepicker_with_label)


class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.configure(fg_color="#121212")

        self.place(relx=0, rely=0, relwidth=1, relheight=1)
