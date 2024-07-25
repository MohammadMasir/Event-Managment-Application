import customtkinter as ctk 
import tkinter as tk 
import datetime
from tkinter import messagebox
from PIL import Image
from .theme import ThemeDesigner

class Personal_information():
    def __init__(self, main_app,frame_name):
        super().__init__()
        self.main_app = main_app
        self.frame_name = frame_name
        self.frame_name.pack_forget()
        self.main_frame = ctk.CTkFrame(self.main_app.register_tab)
        self.main_frame.pack(fill="both", expand=True)
        self.entry = None    

    def Personal_info(self):
        self.main_scrollable_frame = ctk.CTkScrollableFrame(self.main_frame,width = 900,fg_color = "#ffffff")
        self.main_scrollable_frame.pack(side = "left",fill = "y",padx = (20,20))

        self.right_scrollable_frame = ctk.CTkScrollableFrame(self.main_frame,width = 340,fg_color = "#ffffff")
        self.right_scrollable_frame.pack(side = "right",fill = "y")

        self.blue_frame = ctk.CTkFrame(self.main_scrollable_frame,height = 40,width = 900,fg_color = "#273173", corner_radius=0)
        self.blue_frame.grid(row = 0,column = 0,sticky = "ew")

        self.upper_frame = ctk.CTkFrame(self.main_scrollable_frame, fg_color="transparent")
        self.upper_frame.grid(row=1,column=0, sticky="ew")
        
        demeven_variable = tk.StringVar()
        event_text = "DemEven"
        demeven_variable.set(event_text)
        self.demeven = ctk.CTkLabel(self.upper_frame,textvariable = demeven_variable,text_color = "#273173",font = ctk.CTkFont(size = 40,weight = "bold"),pady=20)
        self.demeven.pack(anchor="center")

        data_frame = ctk.CTkFrame(self.upper_frame, fg_color="transparent")
        data_frame.pack(fill="x", expand=True)
        
        date_frame = ctk.CTkFrame(data_frame, fg_color="transparent")
        date_frame.pack(side="left", padx=(50,0))

        place_frame = ctk.CTkFrame(data_frame, fg_color="transparent")
        place_frame.pack(side="right", padx=(0,50))

        date_variable = tk.StringVar()
        date_text = "July 30 2024"
        date_variable.set(date_text)
        self.date = ctk.CTkLabel(date_frame,textvariable = date_variable,text_color = "#273173",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.date.pack()
        
        time_variable = tk.StringVar()
        time_text = "6:00 PM-10:00 PM"
        time_variable.set(time_text)
        self.time = ctk.CTkLabel(date_frame,textvariable = time_variable,text_color = "#11A2E3",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.time.pack()
        
        venue_variable = tk.StringVar()
        venue_text = "Chicago"
        venue_variable.set(venue_text)
        self.venue = ctk.CTkLabel(place_frame,textvariable = venue_variable,text_color = "#273173",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.venue.pack()
        
        location_variable = tk.StringVar()
        location_text = "Chicago, IL"
        location_variable.set(location_text)
        self.location = ctk.CTkLabel(place_frame,textvariable = location_variable,text_color = "#11A2E3",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.location.pack()

        self.lower_frame = ctk.CTkFrame(self.main_scrollable_frame, fg_color="transparent")
        self.lower_frame.grid(row=3, column=0, sticky="ew", pady=(10,0))

        self.personal = ctk.CTkLabel(self.lower_frame,text = "Personal Information",text_color = "#11A2E3",font = ctk.CTkFont(size = 28,weight = "bold"))
        self.personal.grid(row = 5,column = 0,padx = 60)

        self.mandatory = ctk.CTkLabel(self.lower_frame,text = "Fill out the Information below,then click Next to continue",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.mandatory.grid(row = 6,column = 0,padx = 30)

        self.first_name = ctk.CTkLabel(self.lower_frame,text = "* First Name",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.first_name.grid(row = 7,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.first_name_entry = ctk.CTkEntry(self.lower_frame,height = 35,width = 800,corner_radius = 5)
        self.first_name_entry.grid(row = 8,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.last_name =  ctk.CTkLabel(self.lower_frame,text = "* Last Name",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.last_name.grid(row = 9,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.last_name_entry = ctk.CTkEntry(self.lower_frame,height = 35,width = 800,corner_radius = 5)
        self.last_name_entry.grid(row = 10,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.email = ctk.CTkLabel(self.lower_frame,text = "* Email",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.email.grid(row = 11,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.email_entry = ctk.CTkEntry(self.lower_frame,height = 35,width = 800,corner_radius = 5)
        self.email_entry.grid(row = 12,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.mobile = ctk.CTkLabel(self.lower_frame,text = "Mobile",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.mobile.grid(row = 13,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.mobile_entry = ctk.CTkEntry(self.lower_frame,height = 35,width = 800,corner_radius = 5)
        self.mobile_entry.grid(row = 14,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.company = ctk.CTkLabel(self.lower_frame,text = "Company",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.company.grid(row = 15,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.company_entry = ctk.CTkEntry(self.lower_frame,height = 35,width = 800,corner_radius = 5)
        self.company_entry.grid(row = 16,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.title = ctk.CTkLabel(self.lower_frame,text = "Title",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.title.grid(row = 17,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.title_entry = ctk.CTkEntry(self.lower_frame,height = 35,width = 800,corner_radius = 5)
        self.title_entry.grid(row = 18,column = 0,sticky = "nw",padx = 30,pady = 0)

        buttons_frame = ctk.CTkFrame(self.lower_frame, fg_color="transparent")
        buttons_frame.grid(row=19,column=0, sticky="ew", pady=20)

        inside_button_fr = ctk.CTkFrame(buttons_frame, fg_color="transparent")
        inside_button_fr.pack(anchor="center")

        self.cancel = ctk.CTkButton(inside_button_fr,text = "Cancel",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue")
        self.cancel.pack(side="left", padx=(0,10))

        self.next = ctk.CTkButton(inside_button_fr,text = "Next",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue")
        self.next.pack(side="right")

        self.theme_designer = ThemeDesigner(self.right_scrollable_frame, self)
        self.theme_designer.Theme_structure()