import customtkinter as ctk

def create_frame_s(
    master,
    relx=0.05,
    rely=0.2,
    relwidth=0.25,
    relheight=0.6,
    fondo_base="#1F1F1F",
    color_frame="#2E2E2E"
):
    # Background
    master.configure(fg_color=fondo_base)

    # Frame
    frame = ctk.CTkFrame(
        master,
        corner_radius=20,
        fg_color=color_frame,
        border_width=2,
        border_color="#444444"
    )
    frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
    frame.lift()
    return frame






