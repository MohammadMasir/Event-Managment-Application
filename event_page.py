import customtkinter as ctk
import tkinter as tk
from PIL import Image

class EventManagement():
    def __init__(self):
        super().__init__()

        self.primary_color = "#093838"
        self.secondary_color = "#8bceba"
        self.bg = "gainsboro"
        self.text_color = "#092928"
        self.hovercolor_bg = "#20807f"
        self.hovercolor_txt = "white"

    def topbar(self, parent):
        self.top_frame = ctk.CTkFrame(parent, fg_color="white")
        self.top_frame.pack(side="top",fill="x", ipady=5)
#-----------------------
        # Logo and title
        logo_frame = ctk.CTkFrame(self.top_frame, fg_color="white")
        logo_frame.pack(side="left", padx=10)

        label1 = ctk.CTkLabel(logo_frame, text="cvent", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), bg_color="white")
        label1.pack(side="left")

        label2 = ctk.CTkLabel(logo_frame, text="|", font=ctk.CTkFont(size=19, weight="bold"),text_color="black", bg_color="white")
        label2.pack(side="left", padx=10)

        label3 = ctk.CTkLabel(logo_frame, text="EVENTS", text_color="#3fa6fb", font=ctk.CTkFont(size=17, weight="bold"), bg_color="white")
        label3.pack(side="left")
#-----------------------
        # Options
        options_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        options_frame.pack(side="left", expand=True, fill="x")

        another_frame = ctk.CTkFrame(options_frame, fg_color="white", bg_color="white")
        another_frame.pack(anchor="center")

        label4 = ctk.CTkLabel(another_frame, text="All Events", text_color="black", font=ctk.CTkFont(size=17, weight="normal"))
        label4.pack(side="left", padx=10)

        x1 = ctk.StringVar(value="Calendar")
        opt1 = ctk.CTkComboBox(another_frame, variable=x1, width=100, values=["2020", "2021", "2022", "2023"], fg_color="white", button_color=self.secondary_color, bg_color="white")
        opt1.pack(side="left")

        x2 = ctk.StringVar(value="More")
        opt2 = ctk.CTkComboBox(another_frame, variable=x2, width=90, values=["", "", "", ""], fg_color="white", button_color=self.secondary_color, bg_color="white")
        opt2.pack(side="left", padx=10)
#-----------------------
        # Icons
        icons_frame = ctk.CTkFrame(self.top_frame, fg_color="white")
        icons_frame.pack(side="right", padx=10)

        for icon_path in ["loupe.png", "file.png", "question.png", "user (1).png", "menu.png"]:
            img = ctk.CTkImage(dark_image=Image.open(f"pics/{icon_path}"), size=(20, 20))
            button = ctk.CTkButton(icons_frame, image=img, text="", width=20, fg_color="white", bg_color="white", hover_color="#3fa6fb")
            button.pack(side="left", padx=2)
