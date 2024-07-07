import customtkinter as ctk 
#from Personalinfo import Personal_information
import tkinter as tk 
import datetime
from tkinter import messagebox
from PIL import Image

class Cancellation(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.cancellation()
        self.method_calling()

    def logout(self):
        pass
    
    def cancel(self):
        pass
    
    def submit(self):
        pass

    def common_entry(self):
       common_entry = ctk.CTkEntry(self.main_scrollable_frame,height = 35,width = 800,corner_radius = 5)
       return common_entry

    def cancellation(self):
        self.title("Personal Information")
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

        self.sorry_label = ctk.CTkLabel(self.main_scrollable_frame,text = "We're sorry that you can't attend",text_color = "#11A2E3",font = ctk.CTkFont(size = 28,weight = "bold"))
        self.sorry_label.grid(row = 5,column = 0,padx = (80,0),pady = 20)

        self.mandatory_filling = ctk.CTkLabel(self.main_scrollable_frame,text = "Please fill out the following information and click Submit",text_color = "#000000",font = ctk.CTkFont(size = 18,weight = "normal"))
        self.mandatory_filling.grid(row = 6,column = 0,padx = (65,0))

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

        self.reason_label = ctk.CTkLabel(self.main_scrollable_frame,text = "Let us know why you can't attend",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.reason_label.grid(row = 19,column = 0,sticky = "nw",padx = 30,pady = (20,0))

        self.reason_input_box = tk.Text(self.main_scrollable_frame,width = 88 ,highlightthickness=1,highlightcolor="#000000",height = 5,bg = "#ffffff",fg = "#000000",font = ("Arial",19),bd = 3,relief = tk.SUNKEN)
        self.reason_input_box.grid(row = 20,column = 0,padx = (0,10),pady = 0)

        self.cancel_button = ctk.CTkButton(self.main_scrollable_frame,text = "Cancel",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.cancel)
        self.cancel_button.grid(row = 21,column = 0,sticky = "w",padx = (345,0),pady = 20)

        self.submit_button = ctk.CTkButton(self.main_scrollable_frame,text = "Submit",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.submit)
        self.submit_button.grid(row = 21,column = 0,sticky = "e",padx = (0,345),pady = 20)

    def method_calling(self):
        pass

if __name__ == "__main__":
    cancellation_object = Cancellation()
    cancellation_object.mainloop()



