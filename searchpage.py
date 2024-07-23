import customtkinter as ctk
from PIL import Image
import pymysql as pq
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning, showerror

class SearchPage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.Search()
    
    def search_data(self):
        pass

    def Search(self):
        self.title("Search Page")
        self.geometry("500x500")
        self.configure(fg_color = "#8bceba")

        self.search_label = ctk.CTkLabel(self,text = "Search by : Full Name,Email,Confirmation Number",text_color = "#ffffff",font = ctk.CTkFont("Impact",45,"bold"))
        self.search_label.place(x = 180,y = 200)
        
        search_entry_data = tk.StringVar()
        self.search_entry = ctk.CTkEntry(self,height = 70,width = 690,textvariable = search_entry_data,corner_radius = 5,fg_color = "#ffffff",font = ctk.CTkFont("Arial",20))
        self.search_entry.place(x = 270,y = 260)

        self.search_image = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\loupe.png"),size = (25,25))
        self.search_image_button = ctk.CTkButton(self.search_entry,image = self.search_image,text = "",width = 20,fg_color = "#ffffff",hover_color = "lightgray",command = self.search_data)
        self.search_image_button.place(x = 630,y = 20)

SearchPage_class_object = SearchPage()
SearchPage_class_object.mainloop()