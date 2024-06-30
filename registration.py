# registration.py
import customtkinter as ctk

class RegistrationPage:
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Create widgets for the registration page
        label = ctk.CTkLabel(self.parent, text="Registration Page", font=("Segoe UI", 20, "bold"), text_color="white")
        label.pack(pady=20)

        # Add more widgets as needed
        entry = ctk.CTkEntry(self.parent, placeholder_text="Enter your name")
        entry.pack(pady=10)

        button = ctk.CTkButton(self.parent, text="Submit", command=self.on_submit)
        button.pack(pady=10)

    def on_submit(self):
        # Handle the submit action
        print("Submitted")
