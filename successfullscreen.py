import customtkinter as ctk
from PIL import Image
import pymysql as pq
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning, showerror

class Success(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.Success_screen()
    
    def done_command(self):
        pass

    def Success_screen(self):
        self.title("Search Page")
        self.geometry("500x500")
        self.configure(fg_color = "#8bceba")
        
        company_name = tk.StringVar()
        company_name_text = "Latoya ebanks"
        company_name.set(company_name_text)
        self.company_label = ctk.CTkLabel(self,textvariable = company_name,text_color = "#ffffff",font = ctk.CTkFont("impact",50,"normal"))
        self.company_label.place(x = 50,y = 50)

        self.complete_label = ctk.CTkLabel(self,text = "Check-In Complete",text_color = "#ffffff",font = ctk.CTkFont("Arial",30,"normal"))
        self.complete_label.place(x = 50,y = 120)

        self.checked_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\checked.png"),size = (250,250))
        self.checked_image_label = ctk.CTkLabel(self,image = self.checked_image,text = "")
        self.checked_image_label.place(x = 500,y = 200)

        self.success_message = ctk.CTkLabel(self,text = "You have successfully checked in.Enjoy the event!",text_color = "#ffffff",font = ctk.CTkFont("Arial",30,"normal"))
        self.success_message.place(x = 270,y = 460)

        self.done_button = ctk.CTkButton(self,text = "Done",corner_radius = 5,anchor = "center",text_color = "#000000",fg_color = "#ffffff",height = 70,width = 200,hover_color = "lightgray",font = ctk.CTkFont("Arial",25,"normal"),command = self.done_command)
        self.done_button.place(x = 520,y = 550)

Success_class_object = Success()
Success_class_object.mainloop()