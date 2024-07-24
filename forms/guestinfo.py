import customtkinter as ctk 
import tkinter as tk 
import datetime
from tkinter import messagebox
from PIL import Image

class Guest_info(ctk.CTk):
    def cancel_guest(self):
        pass
    
    def add_guest(self):
        pass

    def __init__(self):
        super().__init__()
        self.guestinfo()
        self.method_calling()
    
    def common_entry(self):
       common_entry = ctk.CTkEntry(self.main_frame,height = 35,width = 650,corner_radius = 5,fg_color = "#ffffff")
       return common_entry

    def guestinfo(self):
        self.title("Personal Information")
        self.configure(fg_color = "lightgray")
        self.geometry("800x800")

        self.main_frame = ctk.CTkFrame(self,height = 500,width = 800,fg_color = "#ffffff")
        self.main_frame.pack(side = "left",padx = (20,0),pady = 10)

        self.right_scrollable_frame = ctk.CTkScrollableFrame(self,width = 340,fg_color = "#ffffff")
        self.right_scrollable_frame.pack(side = "right",fill = "y")

        self.add_guest_label = ctk.CTkLabel(self.main_frame,text = "Add a guest",text_color = "#11A2E3",font = ctk.CTkFont(size = 30,weight = "bold"))
        self.add_guest_label.place(x = 315,y = 10)

        self.enter_info_label = ctk.CTkLabel(self.main_frame,text = "Enter your guest's information below",text_color = "#000000",font = ctk.CTkFont(size = 19,weight = "normal"))
        self.enter_info_label.place(x = 250,y = 53)

        self.first_name = ctk.CTkLabel(self.main_frame,text = "* First  Name",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.first_name.place(x = 100,y = 100)

        self.first_name_entry = self.common_entry()
        self.first_name_entry.place(x = 100,y = 130)

        self.last_name = ctk.CTkLabel(self.main_frame,text = "* Last  Name",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.last_name.place(x = 100,y = 200)

        self.last_name_entry = self.common_entry()
        self.last_name_entry.place(x = 100,y = 230)

        self.email_address = ctk.CTkLabel(self.main_frame,text = "Email  Address",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.email_address.place(x = 100,y = 300)

        self.email_address_entry = self.common_entry()
        self.email_address_entry.place(x = 100,y = 330)

        self.cancel = ctk.CTkButton(self.main_frame,text = "Cancel",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "lightgray",command = self.cancel_guest)
        self.cancel.place(x = 300,y = 400)

        self.add = ctk.CTkButton(self.main_frame,text = "Add",height = 30,width = 100,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "lightgray",command = self.add_guest)
        self.add.place(x = 410,y = 400)

    def method_calling(self):
        pass

if __name__ == "__main__":
    guest_info_object = Guest_info()
    guest_info_object.mainloop()