import tkinter as tk
import customtkinter as ctk

class EventManagementApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Event Management and Ticketing System")
        self.geometry("800x600")

        # Set appearance mode
        ctk.set_appearance_mode("dark")

        # Set default color theme
        ctk.set_default_color_theme("green")

        self.create_widgets()

    def create_widgets(self):
        # Create a notebook (tabbed interface)
        notebook = ctk.CTkTabview(self, width=700, height=500)
        notebook.pack(padx=20, pady=20, fill="both", expand=True)

        # Dashboard Tab
        dashboard_frame = ctk.CTkFrame(notebook, fg_color="transparent")
        dashboard_tab = notebook.add("Dashboard")
        dashboard_tab.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(dashboard_frame, text="Welcome to the Dashboard!", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        # Event Management Tab
        event_frame = ctk.CTkFrame(notebook, fg_color="transparent")
        event_tab = notebook.add("Event Management")
        event_tab.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(event_frame, text="Manage your events here", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        # Registration and Ticketing Tab
        ticket_frame = ctk.CTkFrame(notebook, fg_color="transparent")
        ticket_tab = notebook.add("Registration and Ticketing")
        ticket_tab.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(ticket_frame, text="Handle registrations and tickets", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        # Reporting and Analytics Tab
        report_frame = ctk.CTkFrame(notebook, fg_color="transparent")
        report_tab = notebook.add("Reporting and Analytics")
        report_tab.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(report_frame, text="View analytics and reports", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        # Survey and Feedback Tab
        survey_frame = ctk.CTkFrame(notebook, fg_color="transparent")
        survey_tab = notebook.add("Survey and Feedback")
        survey_tab.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(survey_frame, text="Create surveys and view responses", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

if __name__ == "__main__":
    app = EventManagementApp()
    app.mainloop()