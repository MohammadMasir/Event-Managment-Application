import customtkinter as ctk 
#from Personalinfo import Personal_information
import tkinter as tk 
import datetime
from tkinter import messagebox
from PIL import Image
from .theme import ThemeDesigner

class Decline():
    def __init__(self, main_app, registration, frame_name):
        super().__init__()
        self.main_app = main_app
        self.frame_name = frame_name
        self.frame_name.pack_forget()
        self.register_page = registration
        self.main_frame = ctk.CTkFrame(self.main_app.register_tab)
        self.main_frame.pack(fill="both", expand=True) 
    def cancel(self):
        pass
    
    def submit(self):
        pass

    def decline(self):
        self.main_scrollable_frame = ctk.CTkScrollableFrame(self.main_frame,width = 900,fg_color = "#ffffff")
        self.main_scrollable_frame.pack(side = "left",fill = "y",padx = (20,20),pady = 20)

        self.right_scrollable_frame = ctk.CTkScrollableFrame(self.main_frame,width = 340,fg_color = "#ffffff")
        self.right_scrollable_frame.pack(side = "right",fill = "y")

        self.blue_frame = ctk.CTkFrame(self.main_scrollable_frame,height = 80,width = 900,fg_color = "#273173")
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

        self.sorry_label = ctk.CTkLabel(self.main_scrollable_frame,text = "We're sorry that you can't attend",text_color = "#11A2E3",font = ctk.CTkFont(size = 28,weight = "bold"))
        self.sorry_label.grid(row = 5,column = 0,padx = (80,0),pady = 20)

        self.mandatory_filling = ctk.CTkLabel(self.main_scrollable_frame,text = "Please fill out the following information and click Submit",text_color = "#000000",font = ctk.CTkFont(size = 18,weight = "normal"))
        self.mandatory_filling.grid(row = 6,column = 0,padx = (65,0))

        self.first_name = ctk.CTkLabel(self.main_scrollable_frame,text = "* First Name",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.first_name.grid(row = 7,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.first_name_entry = ctk.CTkEntry(self.main_scrollable_frame,height = 35,width = 650,corner_radius = 5,fg_color = "#ffffff")
        self.first_name_entry.grid(row = 8,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.last_name =  ctk.CTkLabel(self.main_scrollable_frame,text = "* Last Name",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.last_name.grid(row = 9,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.last_name_entry = ctk.CTkEntry(self.main_scrollable_frame,height = 35,width = 650,corner_radius = 5,fg_color = "#ffffff")
        self.last_name_entry.grid(row = 10,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.email = ctk.CTkLabel(self.main_scrollable_frame,text = "* Email",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.email.grid(row = 11,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.email_entry = ctk.CTkEntry(self.main_scrollable_frame,height = 35,width = 650,corner_radius = 5,fg_color = "#ffffff")
        self.email_entry.grid(row = 12,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.mobile = ctk.CTkLabel(self.main_scrollable_frame,text = "Mobile",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.mobile.grid(row = 13,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.mobile_entry = ctk.CTkEntry(self.main_scrollable_frame,height = 35,width = 650,corner_radius = 5,fg_color = "#ffffff")
        self.mobile_entry.grid(row = 14,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.company = ctk.CTkLabel(self.main_scrollable_frame,text = "Company",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.company.grid(row = 15,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.company_entry = ctk.CTkEntry(self.main_scrollable_frame,height = 35,width = 650,corner_radius = 5,fg_color = "#ffffff")
        self.company_entry.grid(row = 16,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.title = ctk.CTkLabel(self.main_scrollable_frame,text = "Title",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.title.grid(row = 17,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.title_entry = ctk.CTkEntry(self.main_scrollable_frame,height = 35,width = 650,corner_radius = 5,fg_color = "#ffffff")
        self.title_entry.grid(row = 18,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.reason_label = ctk.CTkLabel(self.main_scrollable_frame,text = "Let us know why you can't attend",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.reason_label.grid(row = 19,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.reason_input_box = ctk.CTkTextbox(self.main_scrollable_frame,width = 68,height = 5,fg_color = "#ffffff",font = ctk.CTkFont(family="Arial",size=19),border_width = 1)

        self.cancel_button = ctk.CTkButton(self.main_scrollable_frame,text = "Cancel",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.cancel)
        self.cancel_button.grid(row = 21,column = 0,sticky = "w",padx = (345,0),pady = 20)

        self.submit_button = ctk.CTkButton(self.main_scrollable_frame,text = "Submit",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.submit)
        self.submit_button.grid(row = 21,column = 0,sticky = "e",padx = (0,345),pady = 20)

        self.theme_designer = ThemeDesigner(self.right_scrollable_frame, self, 5)
        self.theme_designer.Theme_structure()

    def method_calling(self):
        pass

