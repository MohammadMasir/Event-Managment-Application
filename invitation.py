import customtkinter as ctk 
from PIL import Image
import tkinter as tk
from commonpages import Page

class InviteeAttendeePage():
    def __init__(self, main_app, event_name=None):
        super().__init__()
        self.main = main_app
        self.parent = self.main.invitee_tab
        self.event_name = event_name

    def set_screen(self):
        self.main.notebook.set("Invitee & Attendee")
        for widget in self.parent.winfo_children():
            widget.pack_forget()

    def invitation_list_screen(self):
        for widget in self.parent.winfo_children():
            widget.pack_forget()
        self.inv_list_frame = ctk.CTkFrame(self.parent)
        self.inv_list_frame.pack(fill="both", expand=True)
        self.invitationpage = Page(main_app=self.main, parent=self.inv_list_frame, heading="Invitation List")
        self.invitationpage.title_frame(False)
        self.invitationpage.content_frame()

    def event_emails(self):
        self.set_screen()
        self.emails_list_frame = ctk.CTkFrame(self.parent)
        self.emails_list_frame.pack(fill="both", expand=True)
        self.emailspage = Page(main_app=self.main, parent=self.emails_list_frame, heading="Event Emails")
        self.emailspage.title_frame(False)
        self.emailspage.content_frame()
    
    def planner_alerts(self):
        self.set_screen()
        self.plannerframe = ctk.CTkFrame(self.parent)
        self.plannerframe.pack(fill="both", expand=True)
        self.plannerpage = Page(main_app=self.main, parent=self.plannerframe, heading="Planner Alerts")
        self.plannerpage.title_frame(False)
        self.plannerpage.content_frame() 

    def attendee_list_screen(self):
        self.set_screen()
        self.attendee_list_frame = ctk.CTkFrame(self.parent)
        self.attendee_list_frame.pack(fill="both", expand=True)
        self.attendeepage = Page(main_app=self.main, parent=self.attendee_list_frame, heading="Attendee List")
        self.attendeepage.title_frame(False)
        self.attendeepage.content_frame() 

    def certificates_screen(self):
        self.set_screen()
        self.certificates_frame = ctk.CTkFrame(self.parent)
        self.certificates_frame.pack(fill="both", expand=True)
        self.certificatespage = Page(main_app=self.main, parent=self.certificates_frame, heading="Certificates")
        self.certificatespage.title_frame(False)
        self.certificatespage.content_frame() 
