import customtkinter as ctk
from PIL import Image
import pymysql as pq
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning, showerror

class Survey(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.Survey_class()
    
    def yes_command(self):
        pass
    
    def next_command(self):
        pass

    def Survey_class(self):
        self.title("Search Page")
        self.geometry("500x500")
        self.configure(fg_color = "#8bceba")

        self.question_label = ctk.CTkLabel(self,text = "Have you attend any of our past events?",text_color = "#ffffff",font = ctk.CTkFont("Impact",45,"bold"))
        self.question_label.place(x = 250,y = 50)

        self.yes_button = ctk.CTkButton(self,text = "Yes",text_color = "#000000",anchor = "w",fg_color = "#ffffff",height = 70,width = 750,hover_color = "lightgray",corner_radius = 5,font = ctk.CTkFont("Arial",25,"normal"),command = self.yes_command)
        self.yes_button.place(x = 250,y = 150)

        self.yes_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\checkmark.png"),size = (25,25))
        self.yes_image_label = ctk.CTkLabel(self.yes_button,image = self.yes_image,text = "",fg_color = "#ffffff",corner_radius = 0.5)
        self.yes_image_label.place(x = 700,y = 20)

        self.no_button = ctk.CTkButton(self,text = "No",text_color = "#000000",anchor = "w",fg_color = "#ffffff",height = 70,width = 750,hover_color = "lightgray",corner_radius = 5,font = ctk.CTkFont("Arial",25,"normal"),command = self.yes_command)
        self.no_button.place(x = 250,y = 250)

        self.no_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\no-stopping.png"),size = (25,25))
        self.no_image_label = ctk.CTkLabel(self.no_button,image = self.no_image,text = "",fg_color = "#ffffff",corner_radius = 0.5)
        self.no_image_label.place(x = 700,y = 20)

        self.next_button = ctk.CTkButton(self,text = "Next",text_color = "#000000",font = ctk.CTkFont("Arial",25,"normal"),anchor = "center",fg_color = "#ffffff",hover_color = "lightgray",height = 70,width = 200,command = self.next_command)
        self.next_button.place(x = 530,y = 500)

Survey_class_object = Survey()
Survey_class_object.mainloop()