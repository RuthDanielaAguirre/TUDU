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
    master.configure(fg_color=fondo_base)

    # Frame
    frame = ctk.CTkFrame(
        master,
        corner_radius=20,
        fg_color=color_frame,
        border_width=2,
        border_color="#8C7853"
    )
    frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
    frame.lift()
    return frame


def create_button(master, texto, comando, relx, rely):
    button = ctk.CTkButton(
        master,
        text=texto,
        command=comando,
        width=160,
        height=42,
        corner_radius=12,
        fg_color="#2E2E2E",
        border_width=2,
        border_color="#EAEAEA",
        text_color="#EAEAEA",
        hover_color="#8C7853"
    )
    button.place(relx=relx, rely=rely, anchor="center")
    return button

def create_entry_with_label(master, label_text, relx, rely, is_password=False):
    font_label = ("Helvetica", 14)
    font_entry = ("Helvetica", 13)

    normal_color = "#444444"
    focus_color = "#8C7853"

    label = ctk.CTkLabel(
        master,
        text=label_text,
        font=font_label,
        text_color="#EAEAEA",
        fg_color="transparent"
    )
    label.place(relx=relx, rely=rely - 0.07, anchor="center")

    entry = ctk.CTkEntry(
        master,
        placeholder_text=label_text,
        font=font_entry,
        width=220,
        height=40,
        corner_radius=16,
        text_color="#EAEAEA",
        fg_color="#2E2E2E",
        border_width=2,
        border_color="#444444",
        show="*" if is_password else ""
    )
    entry.place(relx=relx, rely=rely, anchor="center")

    def on_focus_in(event):
        entry.configure(border_color=focus_color)

    def on_focus_out(event):
        entry.configure(border_color=normal_color)

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

    return entry

def show_error_label(master, text):
    error_label = ctk.CTkLabel(
        master,
        text=text,
        font=("Helvetica", 14),
        text_color="red",
        fg_color="transparent"
    )
    error_label.place(relx=0.5, rely=0.7, anchor="center")
    return error_label





