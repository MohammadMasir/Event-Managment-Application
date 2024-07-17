import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import forms.cancellationform as cancel
import forms.confirmationscreen as confirm
import forms.declineform as decline
import forms.guestinfo as guest
import forms.Personalinfo as info
import forms.Registrationsummary as summary
from commonpages import Page

class RegistrationPage():
    def __init__(self, main_app, event_name=None):
        super().__init__()
        self.main = main_app
        self.parent = self.main.register_tab
        self.event_name = event_name

    def set_screen(self):
        self.main.notebook.set("Registration and Ticketing")
        for widget in self.parent.winfo_children():
            widget.pack_forget()

    def registration_proccess(self):
        for widget in self.parent.winfo_children():
            widget.pack_forget()
        self.process_frame = ctk.CTkFrame(self.parent, fg_color="#F0F0F0")
        self.process_frame.pack(fill="both", expand=True)

        self.process_page = Page(self.main, self.process_frame, self.event_name, "Registration Process")
        self.process_page.title_frame(True)
        self.process_page.content_frame()

        self.build_and_image_frame = ctk.CTkFrame(self.process_page.scrollable_frame,height = 50,fg_color = "#F0F0F0")
        self.build_and_image_frame.pack(anchor = "nw",fill = "x")

        self.build_label = ctk.CTkLabel(self.build_and_image_frame,text = "Design & Build Your Registration Process",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.build_label.grid(row = 0,column = 0,padx = (10,0))

        self.build_image = ctk.CTkImage(dark_image = Image.open(r"pics\pending.png"),size = (15,15))
        self.build_image_label = ctk.CTkLabel(self.build_and_image_frame,image = self.build_image,text = "",height = 5,width = 2)
        self.build_image_label.grid(row = 0,column = 1,padx = (10,0))

        self.get_started_label = ctk.CTkLabel(self.process_page.scrollable_frame,text = "To get started, lauch our new Site Designer, or start customizing one of the pages below.",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
        self.get_started_label.pack(anchor = "nw",padx = 10,pady = 10)

        self.open_site_designer_button = ctk.CTkButton(self.process_page.scrollable_frame,text = "Open Site Designer",text_color = "#ffffff",fg_color = "#0B77E3",height = 25,width = 50,hover_color = "blue",corner_radius = 10,command = self.site_designer)
        self.open_site_designer_button.pack(anchor = "nw",padx = 10,pady = 10)

        self.registration_process_pages_frame = ctk.CTkFrame(self.process_page.scrollable_frame,fg_color = "#ffffff",width = 800,height = 1000)
        self.registration_process_pages_frame.pack(anchor = "nw",padx = 10)

        self.registration_process_pages_label = ctk.CTkLabel(self.registration_process_pages_frame,text = "Registration Process Pages",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.registration_process_pages_label.grid(row = 0,column = 0,padx = 10,pady = (20,0))

        self.personal_info_label = ctk.CTkLabel(self.registration_process_pages_frame,text = "Personal Information",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.personal_info_label.grid(row = 1,column = 0,padx = 10,pady = 20)

        self.personal_info_button = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.personal_info)
        self.personal_info_button.grid(row = 1,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        #self.canvas_line1 = tk.Canvas(self.registration_process_pages_frame,height = 2,width = 1000,bg = "lightgray",relief = tk.SUNKEN)
        #self.canvas_line1.place(x = 60,y = 150)

        self.summary = ctk.CTkLabel(self.registration_process_pages_frame,text = "Registration Summary",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.summary.grid(row = 3,column = 0,padx = 10,pady = 20)

        self.registration_summary_button = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.registration_summary)
        self.registration_summary_button.grid(row = 3,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        #self.canvas_line2 = tk.Canvas(self.registration_process_pages_frame,height = 2,width = 1000,bg = "lightgray",relief = tk.SUNKEN)
        #self.canvas_line2.place(x = 60,y = 250)

        self.post_registration = ctk.CTkLabel(self.registration_process_pages_frame,text = "Post Registration",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.post_registration.grid(row = 4,column = 0,sticky = "nw",padx = 10,pady = (20,0))

        self.confirmation = ctk.CTkLabel(self.registration_process_pages_frame,text = "Confirmation",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.confirmation.grid(row = 5,column = 0,sticky = "nw",padx = 40,pady = 20)

        self.confirmation_butt = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.confirmation_button)
        self.confirmation_butt.grid(row = 5,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        self.other = ctk.CTkLabel(self.registration_process_pages_frame,text = "Others",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.other.grid(row = 6,column = 0,sticky = "nw",padx = 10,pady = (20,0))

        self.cancellation = ctk.CTkLabel(self.registration_process_pages_frame,text = "Cancellation Form",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.cancellation.grid(row = 7,column = 0,sticky = "nw",padx = 40,pady = 20)

        self.cancellation_butt = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.cancellation_button)
        self.cancellation_butt.grid(row = 7,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        self.decline = ctk.CTkLabel(self.registration_process_pages_frame,text = "Decline Form",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.decline.grid(row = 8,column = 0,sticky = "nw",padx = 40,pady = 20)

        self.decline_button = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.cancellation_button)
        self.decline_button.grid(row = 8,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        self.guest = ctk.CTkLabel(self.registration_process_pages_frame,text = "Guest Information",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.guest.grid(row = 9,column = 0,sticky = "nw",padx = 40,pady = 20)

        self.guest_butt = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.guest_button)
        self.guest_butt.grid(row = 9,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

    def registration_settings(self):
        self.set_screen()
        self.settings_frame = ctk.CTkFrame(self.parent)
        self.settings_frame.pack(fill="both", expand=True)
        self.settings_page = Page(self.main, self.settings_frame, self.event_name, "Registration Settings")
        self.settings_page.title_frame(False)
        self.settings_page.content_frame()

    def registration_types(self):
        self.set_screen()
        self.types_frame = ctk.CTkFrame(self.parent)
        self.types_frame.pack(fill="both", expand=True)
        self.types_page = Page(self.main, self.types_frame, self.event_name, "Registration Settings")
        self.types_page.title_frame(False)
        self.types_page.content_frame()

    def search_widget_command(self):
        pass

    def preview_button_command(self):
        pass

    def site_designer(self):
        pass

    def personal_info(self):
        info_form = info.Personal_information(self.main_app,self.process_frame)
        info_form.Personal_info()
        info_form.Theme_design()
        pass

    def registration_summary(self):
        pass

    def confirmation_button(self):
        pass

    def cancellation_button(self):
        pass
    
    def guest_button(self):
        pass