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

    def common_entry(self):
       common_entry = ctk.CTkEntry(self.main_scrollable_frame,height = 35,width = 800,corner_radius = 5)
       return common_entry

    def Personal_info(self):
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
        
        month_variable = tk.StringVar()
        month_text = "July 30 2024"
        month_variable.set(month_text)
        self.month = ctk.CTkLabel(self.main_scrollable_frame,textvariable = month_variable,text_color = "#273173",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.month.grid(row = 2,column = 0,sticky = "w",padx = 70)
        
        time_variable = tk.StringVar()
        time_text = "6:00 PM-10:00 PM"
        time_variable.set(time_text)
        self.time = ctk.CTkLabel(self.main_scrollable_frame,textvariable = time_variable,text_color = "#11A2E3",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.time.grid(row = 3,column = 0,sticky = "w",padx = (50,0))
        
        location_variable = tk.StringVar()
        location_text = "Chicago"
        location_variable.set(location_text)
        self.location = ctk.CTkLabel(self.main_scrollable_frame,textvariable = location_variable,text_color = "#273173",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.location.grid(row = 2,column = 0,sticky = "e",padx = 70)
        
        place_variable = tk.StringVar()
        place_text = "Chicago, IL"
        place_variable.set(place_text)
        self.place = ctk.CTkLabel(self.main_scrollable_frame,textvariable = place_variable,text_color = "#11A2E3",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.place.grid(row = 3,column = 0,sticky = "e",padx = 50)

        self.line_frame = ctk.CTkFrame(self.main_scrollable_frame,height = 15,width = 800,fg_color = "#D9D9D9",corner_radius = 5)
        self.line_frame.grid(row = 4,column = 0,padx = 20,pady = 20)

        self.personal = ctk.CTkLabel(self.main_scrollable_frame,text = "Personal Information",text_color = "#11A2E3",font = ctk.CTkFont(size = 28,weight = "bold"))
        self.personal.grid(row = 5,column = 0,padx = 60)

        self.mandatory = ctk.CTkLabel(self.main_scrollable_frame,text = "Fill out the Information below,then click Next to continue",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.mandatory.grid(row = 6,column = 0,padx = 30)

        self.first_name = ctk.CTkLabel(self.main_scrollable_frame,text = "* First Name",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.first_name.grid(row = 7,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.first_name_entry = self.common_entry()
        self.first_name_entry.grid(row = 8,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.last_name =  ctk.CTkLabel(self.main_scrollable_frame,text = "* Last Name",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.last_name.grid(row = 9,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.last_name_entry = self.common_entry()
        self.last_name_entry.grid(row = 10,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.email = ctk.CTkLabel(self.main_scrollable_frame,text = "* Email",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.email.grid(row = 11,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.email_entry = self.common_entry()
        self.email_entry.grid(row = 12,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.mobile = ctk.CTkLabel(self.main_scrollable_frame,text = "Mobile",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.mobile.grid(row = 13,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.mobile_entry = self.common_entry()
        self.mobile_entry.grid(row = 14,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.company = ctk.CTkLabel(self.main_scrollable_frame,text = "Company",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.company.grid(row = 15,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.company_entry = self.common_entry()
        self.company_entry.grid(row = 16,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.title = ctk.CTkLabel(self.main_scrollable_frame,text = "Title",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.title.grid(row = 17,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.title_entry = self.common_entry()
        self.title_entry.grid(row = 18,column = 0,sticky = "nw",padx = 30,pady = 0)

        self.cancel = ctk.CTkButton(self.main_scrollable_frame,text = "Cancel",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue")
        self.cancel.grid(row = 19,column = 0,sticky = "w",padx = (345,0),pady = 20)

        self.next = ctk.CTkButton(self.main_scrollable_frame,text = "Next",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue")
        self.next.grid(row = 19,column = 0,sticky = "e",padx = (0,345),pady = 20)

        self.theme_designer = ThemeDesigner(self.right_scrollable_frame, self)
        self.theme_designer.Theme_structure()