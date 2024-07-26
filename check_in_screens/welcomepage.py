import customtkinter as ctk
from PIL import Image
import pymysql as pq
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning, showerror

class Welcomepage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.Welcome()

    def CheckedIn(self):
        pass
    
    def register_button(self):
        pass

    def Welcome(self):
        self.title("Welcome Page")
        self.geometry("500x500")
        self.configure(fg_color = "#8bceba")

        self.welcome_label = ctk.CTkLabel(self,text = "Welcome to",text_color = "#ffffff",height = 100,font = ctk.CTkFont(size = 100,weight = "bold"))
        self.welcome_label.place(x = 20,y = 340)
        
        company_name_bind = tk.StringVar()
        company_name_text = "BlueCorp Future Technologies Conference"
        company_name_bind.set(company_name_text)
        self.company_name = ctk.CTkLabel(self,text_color = "#ffffff",font = ctk.CTkFont(size = 30,weight = "bold"),textvariable = company_name_bind)
        self.company_name.place(x = 20,y = 450)

        self.checkin_button = ctk.CTkButton(self,text = "Check In",fg_color = "#ffffff",text_color = "#000000",height = 70,width = 150,corner_radius = 5,hover_color = "lightgray",font = ctk.CTkFont(size = 15,weight = "normal"),anchor = "center",command = self.CheckedIn)
        self.checkin_button.place(x = 20,y = 500)
        
        company_logo_bind = tk.StringVar()
        company_logo_text = "Bluecorp"
        company_logo_bind.set(company_logo_text)
        self.company_logo = ctk.CTkLabel(self,text_color = "#ffffff",font = ctk.CTkFont("Times New Roman",60,"bold"),textvariable = company_logo_bind)
        self.company_logo.place(x = 970,y = 100)

        still_havent_register_label = ctk.CTkLabel(self,text = "Still haven't registered?",text_color = "#ffffff",font = ctk.CTkFont("Comic Sans MS",30,"normal"))
        still_havent_register_label.place(x = 800,y = 500)

        register_button = ctk.CTkButton(self,text = "Register",text_color = "#ffffff",fg_color = "transparent",hover_color = "lightgreen",font = ctk.CTkFont("Comic Sans MS",25,"normal"),command = self.register)
        register_button.place(x = 900,y = 550)

Welcome_class_object = Welcomepage()
Welcome_class_object.mainloop()
