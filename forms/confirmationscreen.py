import customtkinter as ctk 
#from Personalinfo import Personal_information
import tkinter as tk 
import datetime
from tkinter import messagebox
from PIL import Image

class Confirmation(ctk.CTk):
    def logout(self):
        pass
    
    def add_to_calendar(self):
        pass
    
    def modify(self):
        pass
    
    def cancel(self):
        pass

    def __init__(self):
        super().__init__()
        self.confirmation()
        self.method_calling()

    def confirmation(self):
        self.title("Confirmation Page")
        self.configure(fg_color = "lightgray")
        self.geometry("800x800")

        self.main_scrollable_frame = ctk.CTkScrollableFrame(self,width = 900,fg_color = "#ffffff")
        self.main_scrollable_frame.pack(side = "left",fill = "y",padx = (20,20),pady = 20)

        self.right_scrollable_frame = ctk.CTkScrollableFrame(self,width = 340,fg_color = "#ffffff")
        self.right_scrollable_frame.pack(side = "right",fill = "y")

        self.blue_frame = ctk.CTkFrame(self.main_scrollable_frame,height = 80,width = 900,fg_color = "#273173")
        self.blue_frame.grid(row = 0,column = 0,sticky = "ew")

        self.logout_button = ctk.CTkButton(self.blue_frame,text = "Logout",fg_color = "#11A2E3",text_color = "#ffffff",hover_color = "lightgray",command = self.logout)
        self.logout_button.place(x = 700,y = 30)
        
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

        self.register = ctk.CTkLabel(self.main_scrollable_frame,text = "Congratulations, you are now registered!",text_color = "#11A2E3",font = ctk.CTkFont(size = 28,weight = "bold"))
        self.register.grid(row = 6,column = 0,padx = 60,pady = 20)

        self.confirmation_number_label = ctk.CTkLabel(self.main_scrollable_frame,text = "Your Confirmation Number is:",text_color = "#273173",font = ctk.CTkFont(size = 20,weight = "bold"))
        self.confirmation_number_label.grid(row = 7,column = 0,padx = 60,pady = 25)

        self.confirmation_number_value = ctk.CTkLabel(self.main_scrollable_frame,text = "G4NABCDEN2Z",text_color = "#11A2E3",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.confirmation_number_value.grid(row = 8,column = 0,padx = 60,pady = 0)

        self.receive_email_label = ctk.CTkLabel(self.main_scrollable_frame,text = "You will receive an email with your registration details. ",text_color = "#11A2E3",font = ctk.CTkFont(size = 28,weight = "bold"))
        self.receive_email_label.grid(row = 9,column = 0,padx = 60,pady = 20)

        self.add_to_calendar = ctk.CTkButton(self.main_scrollable_frame,text = "Add to Calendar",fg_color = "#ffffff",border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",hover_color = "lightgray",command = self.add_to_calendar)
        self.add_to_calendar.grid(row = 10,column = 0,padx = 60,pady = 15)

        self.see_you_in_label = ctk.CTkLabel(self.main_scrollable_frame,text = "See you in...",text_color = "#273173",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.see_you_in_label.grid(row = 11,column = 0,padx = 60,pady = 20)

        self.modify_registration_button = ctk.CTkButton(self.main_scrollable_frame,text = "Modify Registration",width = 150,text_color = "#ffffff",fg_color = "#11A2E3",hover_color = "lightgray",command = self.modify)
        self.modify_registration_button.grid(row = 12,column = 0,padx = 100,pady = 20,sticky = "w")

        self.cancel_registration_button = ctk.CTkButton(self.main_scrollable_frame,text = "Cancel Registration",text_color = "#ffffff",fg_color = "#11A2E3",hover_color = "lightgray",command = self.cancel)
        self.cancel_registration_button.grid(row = 12,column = 0,padx = 100,pady = 20,sticky = "e")

    def method_calling(self):
        pass

if __name__ == "__main__":
    confirmation_object = Confirmation()
    confirmation_object.mainloop()
