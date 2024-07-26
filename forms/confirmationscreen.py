import customtkinter as ctk 
#from Personalinfo import Personal_information
import tkinter as tk 
import datetime
from tkinter import messagebox
from PIL import Image
from .theme import ThemeDesigner

class Confirmation():
    def __init__(self, main_app, registration, frame_name):
        super().__init__()
        self.main_app = main_app
        self.frame_name = frame_name
        self.frame_name.pack_forget()
        self.register_page = registration
        self.main_frame = ctk.CTkFrame(self.main_app.register_tab)
        self.main_frame.pack(fill="both", expand=True)

    def logout(self):
        pass
    
    def add_to_calendar(self):
        pass
    
    def modify(self):
        pass
    
    def cancel(self):
        pass

    def confirmation(self):
        self.main_scrollable_frame = ctk.CTkScrollableFrame(self.main_frame,width = 900,fg_color = "#ffffff")
        self.main_scrollable_frame.pack(side = "left",fill = "y",padx = (20,20),pady = 20)

        self.right_scrollable_frame = ctk.CTkScrollableFrame(self.main_frame,width = 340,fg_color = "#ffffff")
        self.right_scrollable_frame.pack(side = "right",fill = "y")

        self.blue_frame = ctk.CTkFrame(self.main_scrollable_frame,height = 80,width = 900,fg_color = "#273173")
        self.blue_frame.grid(row = 0,column = 0,sticky = "ew")

        self.logout_button = ctk.CTkButton(self.blue_frame,text = "Logout",fg_color = "#11A2E3",text_color = "#ffffff",command = self.logout)
        self.logout_button.place(x = 700,y = 30)
        
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

        self.registerr = ctk.CTkLabel(self.main_scrollable_frame,text = "Congratulations, you are now registered!",text_color = "#11A2E3",font = ctk.CTkFont(size = 28,weight = "bold"))
        self.registerr.grid(row = 6,column = 0,padx = 60,pady = 20)

        self.confirmation_number_label = ctk.CTkLabel(self.main_scrollable_frame,text = "Your Confirmation Number is:",text_color = "#273173",font = ctk.CTkFont(size = 20,weight = "bold"))
        self.confirmation_number_label.grid(row = 7,column = 0,padx = 60,pady = 25)

        self.confirmation_number_value = ctk.CTkLabel(self.main_scrollable_frame,text = "G4NABCDEN2Z",text_color = "#11A2E3",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.confirmation_number_value.grid(row = 8,column = 0,padx = 60,pady = 0)

        self.receive_email_label = ctk.CTkLabel(self.main_scrollable_frame,text = "You will receive an email with your registration details. ",text_color = "#11A2E3",font = ctk.CTkFont(size = 28,weight = "bold"))
        self.receive_email_label.grid(row = 9,column = 0,padx = 60,pady = 20)

        self.add_to_calendar_b = ctk.CTkButton(self.main_scrollable_frame,text = "Add to Calendar",fg_color = "#ffffff",border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",hover_color = "lightgray",command = self.add_to_calendar)
        self.add_to_calendar_b.grid(row = 10,column = 0,padx = 60,pady = 15)

        self.see_you_in_label = ctk.CTkLabel(self.main_scrollable_frame,text = "See you in...",text_color = "#273173",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.see_you_in_label.grid(row = 11,column = 0,padx = 60,pady = 20)

        self.modify_registration_button = ctk.CTkButton(self.main_scrollable_frame,text = "Modify Registration",width = 150,text_color = "#ffffff",fg_color = "#11A2E3",hover_color = "lightgray",command = self.modify)
        self.modify_registration_button.grid(row = 12,column = 0,padx = 100,pady = 20,sticky = "w")

        self.cancel_registration_button = ctk.CTkButton(self.main_scrollable_frame,text = "Cancel Registration",text_color = "#ffffff",fg_color = "#11A2E3",hover_color = "lightgray",command = self.cancel)
        self.cancel_registration_button.grid(row = 12,column = 0,padx = 100,pady = 20,sticky = "e")

        self.theme_designer = ThemeDesigner(self.right_scrollable_frame, self, 3)
        self.theme_designer.Theme_structure()

    def method_calling(self):
        pass
