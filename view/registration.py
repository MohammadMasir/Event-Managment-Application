import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from forms.cancellationform import Cancellation
from forms.confirmationscreen import Confirmation
from forms.declineform import Decline
from forms.Personalinfo import Personal_information
from forms.Registrationsummary import Registration_summary
from view.commonpages import Page

class RegistrationPage():
    def __init__(self, main_app, parent,event_name=None):
        super().__init__()
        self.main = main_app
        self.parent = parent
        self.event_name = event_name
        self.count = 0

    def set_screen(self):
        self.main.notebook.set("Registration & Ticketing")
        for widget in self.parent.winfo_children():
            widget.pack_forget()

    def registration_proccess(self):
        self.count += 1
        if self.count <= 1:
            for widget in self.parent.winfo_children():
                widget.pack_forget()
        else:
            self.set_screen()

        print(f"Registration Procces function is called for the {self.count} time")
        self.process_frame = ctk.CTkFrame(self.parent, fg_color="#F0F0F0")
        self.process_frame.pack(fill="both", expand=True)

        self.process_page = Page(main_app=self.main, parent=self.process_frame, event_name=self.event_name, heading="Registration Process")
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

        self.decline_butt = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.decline_button)
        self.decline_butt.grid(row = 8,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

    def registration_settings(self):
        self.set_screen()
        self.settings_frame = ctk.CTkFrame(self.parent)
        self.settings_frame.pack(fill="both", expand=True)
        self.settings_page = Page(main_app=self.main, parent=self.settings_frame, event_name=self.event_name, heading="Registration Settings")
        self.settings_page.title_frame(False)
        self.settings_page.content_frame()

        self.registration_settings_content_frame = ctk.CTkFrame(self.settings_page.scrollable_frame,fg_color = "#ffffff")
        self.registration_settings_content_frame.pack(fill = "both",expand = True, padx=(10,90), pady=20)
        print("Lucky's code is running...")

        inside_frame = ctk.CTkFrame(self.registration_settings_content_frame, fg_color="transparent")
        inside_frame.pack(fill="both", expand=True, padx=(20,0), pady=(20,0))

        self.general_label = ctk.CTkLabel(inside_frame,text = "General",text_color = "#000000",font = ("Segoe UI",21,"bold"))
        self.general_label.pack(anchor = "nw",padx = 5,pady = 5)
        #self.general_label.grid(row = 0,column = 0,padx = 5,pady = 5,sticky = "w")
        
        self.edit_button_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\pen.png"),size = (30,30))
        self.edit_button = ctk.CTkButton(inside_frame,image = self.edit_button_image,text = "",hover_color = "lightgray",fg_color = "#ffffff",width = 35,command = self.edit_button_clicked)
        self.edit_button.place(x = 750,y = 5)

        self.setup_label = ctk.CTkLabel(inside_frame,text = "Set up a few basic registration settings and goals.",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.setup_label.pack(anchor="nw", padx = 5,pady = 7)
        #self.setup_label.grid(row = 1,column = 0,padx = 5,pady = 2,sticky = "w")

        self.registration_deadline_label = ctk.CTkLabel(inside_frame,text = "Registration Deadline",text_color = "#000000",font = ctk.CTkFont(size=15,weight="normal"))
        self.registration_deadline_label.pack(anchor="nw", padx = 5,pady = 5)
        #self.registration_deadline_label.grid(row = 2,column = 0,sticky = "w",padx = 5,pady = 5)
        self.right_image = ctk.CTkImage(dark_image = Image.open(r"pics\question.png"),size = (20,20))
        self.right_image_label = ctk.CTkLabel(inside_frame,image = self.right_image,text = "",fg_color = "#ffffff")
        #self.right_image_label.grid(row = 2,column = 1,padx = 4,pady = 5)
        
        date_time_variable = tk.StringVar()
        date_time_variable.set("30 July 2024 at 9:59 pm")
        self.date_time_value = ctk.CTkLabel(inside_frame,textvariable = date_time_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.date_time_value.pack(anchor="nw", padx = 5,pady = 5)
        #self.date_time_value_label.grid(row = 3,column = 0,sticky = "w",padx = 5,pady = 7)

        self.In_person_capacity_label = ctk.CTkLabel(inside_frame,text = "In-Person Capacity",text_color = "#000000",font = ctk.CTkFont(size=15,weight="normal"))
        self.In_person_capacity_label.pack(anchor="nw", padx = 5,pady = 7)
        #self.In_person_capacity_label.grid(row = 4,column = 0,sticky = "w",padx = 5,pady = 5)

        In_person_capacity_variable = tk.StringVar()
        In_person_capacity_variable.set("Unlimited")
        self.In_person_capacity_value = ctk.CTkLabel(inside_frame,textvariable = In_person_capacity_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.In_person_capacity_value.pack(anchor="nw", padx = 5,pady = 5)

        self.virtual_capacity_label = ctk.CTkLabel(inside_frame,text = "Virtual Capacity",text_color = "#000000",font = ctk.CTkFont(size=15,weight="normal"))
        self.virtual_capacity_label.pack(anchor="nw", padx = 5,pady = 7)
        
        virtual_capacity_variable = tk.StringVar()
        virtual_capacity_variable.set("Unlimited")
        self.virtual_capacity_label_value = ctk.CTkLabel(inside_frame,textvariable = virtual_capacity_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.virtual_capacity_label_value.pack(anchor="nw", padx = 5,pady = 5)

        self.total_attendee_goal_label = ctk.CTkLabel(inside_frame,text = "Total Attendee Goal",text_color = "#000000",font =  ctk.CTkFont(size=15,weight="normal"))
        self.total_attendee_goal_label.pack(anchor="nw", padx = 5,pady = 7)
        
        total_attendee_goal_variable = tk.StringVar()
        total_attendee_goal_variable.set("-")
        self.total_attendee_goal_value = ctk.CTkLabel(inside_frame,textvariable = total_attendee_goal_variable,text_color = "#000000",font =  ctk.CTkFont(size=15,weight="bold"))
        self.total_attendee_goal_value.pack(anchor="nw", padx = 5,pady = 5)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def registration_types(self):
        self.set_screen()
        self.types_frame = ctk.CTkFrame(self.parent)
        self.types_frame.pack(fill="both", expand=True)
        self.types_page = Page(main_app=self.main, parent=self.types_frame, event_name=self.event_name, heading="Registration Settings")
        self.types_page.title_frame(False)
        self.types_page.content_frame()

        self.registration_label = ctk.CTkLabel(self.types_page.scrollable_frame,text = "Registration types let you customize the registration experience for different types of attendees.",text_color = "#000000",font =  ("Segoe UI",18,"bold"))
        self.registration_label.pack(anchor = "nw",padx = 15,pady = 10)

        self.types_content_frame = ctk.CTkFrame(self.types_page.scrollable_frame,fg_color = "#ffffff")
        self.types_content_frame.pack(fill = "both",expand = True, padx=(10,90), pady=20)

        self.filter = ctk.CTkEntry(self.types_content_frame,height = 35,width = 400,corner_radius = 7,fg_color = "#ffffff",text_color = "#000000",placeholder_text = "Filter",placeholder_text_color = "#000000",font = ("Arial",17,"normal"))
        self.filter.pack(anchor = "ne",padx = 15,pady = 10)

        self.filter_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\loupe.png"),size = (25,25))
        self.filter_image_button = ctk.CTkButton(self.filter,image = self.filter_image,text = "",width = 35,fg_color = "#ffffff",hover_color = "lightgray",command = self.filter_command)
        self.filter_image_button.grid(row = 0,column = 0,sticky = "ne",padx = 10,pady = 5)
   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def search_widget_command(self):
        pass

    def preview_button_command(self):
        pass

    def site_designer(self):
        pass

    def personal_info(self):
        info_form = Personal_information(self.main, self, self.process_frame)
        info_form.Personal_info()
        

    def registration_summary(self):
        summary_form = Registration_summary(self.main, self, self.process_frame)
        summary_form.registration_summary()

    def confirmation_button(self):
        confirm_form = Confirmation(self.main, self, self.process_frame)
        confirm_form.confirmation()

    def cancellation_button(self):
        cancellation_form = Cancellation(self.main, self, self.process_frame)
        cancellation_form.cancellation()
    
    def decline_button(self):
        decline_form = Decline(self.main, self, self.process_frame)
        decline_form.decline()
