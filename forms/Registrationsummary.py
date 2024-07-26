import customtkinter as ctk 
# from Personalinfo import Personal_information
import tkinter as tk 
import datetime
from tkinter import messagebox
from PIL import Image
from .theme import ThemeDesigner

class Registration_summary():
    def __init__(self, main_app, registration, frame_name):
        super().__init__()
        self.main_app = main_app
        self.frame_name = frame_name
        self.frame_name.pack_forget()
        self.register_page = registration
        self.main_frame = ctk.CTkFrame(self.main_app.register_tab)
        self.main_frame.pack(fill="both", expand=True)

    def edit_button_command(self):
        pass

    def item_button_command(self):
        pass  

    def cancel_command(self):
        pass

    def previous_command(self):
        pass

    def submit_command(self):
        pass

    def registration_summary(self):
        self.main_scrollable_frame = ctk.CTkScrollableFrame(self.main_frame,width = 900,fg_color = "#ffffff")
        self.main_scrollable_frame.pack(side = "left",fill = "y",padx = (20,20),pady = 20)

        self.right_scrollable_frame = ctk.CTkScrollableFrame(self.main_frame,width = 340,fg_color = "#ffffff")
        self.right_scrollable_frame.pack(side = "right",fill = "y")

        self.blue_frame = ctk.CTkFrame(self.main_scrollable_frame,height = 20,width = 900,fg_color = "#273173")
        self.blue_frame.grid(row = 0,column = 0,sticky = "ew")
        
        demeven_variable = tk.StringVar()
        event_text = "DemEven"
        demeven_variable.set(event_text)
        self.demeven = ctk.CTkLabel(self.main_scrollable_frame,textvariable = demeven_variable,text_color = "#273173",font = ctk.CTkFont(size = 40,weight = "bold"))
        self.demeven.grid(row = 1,column = 0,padx = 40,pady = 20)
        
        date_variable = tk.StringVar()
        date_text = "July 30 2024"
        date_variable.set(date_text)
        self.date = ctk.CTkLabel(self.main_scrollable_frame,textvariable = date_variable,text_color = "#273173",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.date.grid(row = 2,column = 0,sticky = "w",padx = 70)
        
        time_variable = tk.StringVar()
        time_text = "6:00 PM-10:00 PM"
        time_variable.set(time_text)
        self.time = ctk.CTkLabel(self.main_scrollable_frame,textvariable = time_variable,text_color = "#11A2E3",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.time.grid(row = 3,column = 0,sticky = "w",padx = (50,0))
        
        venue_variable = tk.StringVar()
        venue_text = "Chicago"
        venue_variable.set(venue_text)
        self.venue = ctk.CTkLabel(self.main_scrollable_frame,textvariable = venue_variable,text_color = "#273173",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.venue.grid(row = 2,column = 0,sticky = "e",padx = 70)
        
        location_variable = tk.StringVar()
        location_text = "Chicago, IL"
        location_variable.set(location_text)
        self.location = ctk.CTkLabel(self.main_scrollable_frame,textvariable = location_variable,text_color = "#11A2E3",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.location.grid(row = 3,column = 0,sticky = "e",padx = 50)

        self.slider = ctk.CTkProgressBar(self.main_scrollable_frame,height = 15,corner_radius = 10,width = 800,progress_color = "#273173",fg_color = "#D2D2D2",orientation = "horizontal",determinate_speed = 3)
        self.slider.grid(row = 4,column = 0,padx = 20,pady = 20)

        self.personal = ctk.CTkLabel(self.main_scrollable_frame,text = "Registration Summary",text_color = "#11A2E3",font = ctk.CTkFont(size = 28,weight = "bold"))
        self.personal.grid(row = 5,column = 0,padx = 60)

        self.mandatory = ctk.CTkLabel(self.main_scrollable_frame,text = "Take a moment to review your registration before continuing",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.mandatory.grid(row = 6,column = 0,padx = 30)
        
        name_variable = tk.StringVar()
        name_text = "John Doe"
        name_variable.set(name_text)
        self.name = ctk.CTkLabel(self.main_scrollable_frame,textvariable = name_variable,text_color = "#273173",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.name.grid(row = 7,column = 0,sticky = "nw",padx = 50,pady = (20,0))

        self.email = ctk.CTkLabel(self.main_scrollable_frame,text = "john.doe@gmail.com",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.email.grid(row = 8,column = 0,sticky = "nw",padx = 50,pady = 0)

        self.edit_button = ctk.CTkButton(self.main_scrollable_frame,text = "Edit",height = 15,width = 40,text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.edit_button_command)
        self.edit_button.grid(row = 9,column = 0,sticky = "nw",padx = 40,pady = (10,0))
        
        self.company = ctk.CTkLabel(self.main_scrollable_frame,text = "Company",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.company.grid(row = 10,column = 0,sticky = "nw",padx = 50,pady = (20,0))
        
        company_variable = tk.StringVar()
        company_name = "OrangeCorp"
        company_variable.set(company_name)
        self.company_name = ctk.CTkLabel(self.main_scrollable_frame,textvariable = company_variable,text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.company_name.grid(row = 11,column = 0,sticky = "nw",padx = 50,pady = 0)

        self.title = ctk.CTkLabel(self.main_scrollable_frame,text = "Title",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.title.grid(row = 10,column = 0,sticky = "ne",padx = (0,100),pady = (20,0))
        
        title_variable = tk.StringVar()
        title_name = "Manager"
        title_variable.set(title_name)
        self.title_name = ctk.CTkLabel(self.main_scrollable_frame,textvariable = title_variable,text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.title_name.grid(row = 11,column = 0,sticky = "ne",padx = (0,100),pady = (0,0))

        self.questions =  ctk.CTkLabel(self.main_scrollable_frame,text = "Questions",text_color = "#11A2E3",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.questions.grid(row = 12,column = 0,sticky = "nw",padx = (50,0),pady = 10)

        self.agenda = ctk.CTkLabel(self.main_scrollable_frame,text = "Agenda",text_color = "#11A2E3",font = ctk.CTkFont(size = 20,weight = "bold"))
        self.agenda.grid(row = 13,column = 0,sticky = "nw",padx = (50,0),pady = 10)

        self.item_button = ctk.CTkButton(self.main_scrollable_frame,text = "Item",height = 15,width = 40,text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.item_button_command)
        self.item_button.grid(row = 14,column = 0,sticky = "nw",padx = (50,0),pady = 10)

        self.addmission_item =  ctk.CTkLabel(self.main_scrollable_frame,text = "Addmission Item",text_color = "#11A2E3",font = ctk.CTkFont(size = 20,weight = "bold"))
        self.addmission_item.grid(row = 15,column = 0,sticky = "nw",padx = (50,0),pady = (10,0))

        self.event_registration = ctk.CTkLabel(self.main_scrollable_frame,text = "Event Registration",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.event_registration.grid(row = 16,column = 0,sticky = "nw",padx = (50,0))

        self.previous = ctk.CTkButton(self.main_scrollable_frame,text = "Previous",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.previous_command)
        self.previous.grid(row = 20,column = 0,sticky = "w",padx = (250,0),pady = (50,0))

        self.cancel = ctk.CTkButton(self.main_scrollable_frame,text = "Cancel",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.cancel_command)
        self.cancel.grid(row = 20,column = 0,sticky = "w",padx = (355,0),pady = (50,0))

        self.submit = ctk.CTkButton(self.main_scrollable_frame,text = "Submit",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.submit_command)
        self.submit.grid(row = 20,column = 0,sticky = "w",padx = (460,0),pady = (50,0))

        self.theme_designer = ThemeDesigner(self.right_scrollable_frame, self, 2)
        self.theme_designer.Theme_structure()

    def method_calling(self):
        pass