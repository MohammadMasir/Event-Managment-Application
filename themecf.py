import customtkinter as ctk 
import tkinter as tk 
import datetime
from tkinter import messagebox
from PIL import Image

class Theme():
    def __init__(self, parent_frame, main_app=None):
        super().__init()
        self.main_scrollable_frame = ctk.CTkScrollableFrame(parent_frame,width = 900,fg_color = "#ffffff")
        self.main_scrollable_frame.pack(side = "left",fill = "y",padx = (20,20),pady = 20)

        self.right_scrollable_frame = ctk.CTkScrollableFrame(parent_frame,width = 340,fg_color = "#ffffff")
        self.right_scrollable_frame.pack(side = "right",fill = "y")

        self.theme = ctk.CTkLabel(self.right_scrollable_frame,text = "Theme",text_color = "#000000",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.theme.grid(row = 0,column = 0,padx = 100,pady = 10)

    def cancel_command(self):
        pass
    
    def next_command(self):
        pass

    def change_theme_command(self):
        pass 
    
    def add_image_command(self):
        pass

    def edit_image_command(self):
        pass
    
    def finished_command(self):
        pass

    def common_entry(self):
        entry = ctk.CTkEntry(self.main_scrollable_frame,height = 35,width = 800,corner_radius = 5)
        return entry

    def common_line(self):
        canvas = tk.Canvas(self.right_scrollable_frame,height = 1,bg = "lightgray",relief = tk.SUNKEN)
        return canvas

    def start(self):
        self.line1 = self.common_line()
        self.line1.grid(row = 1,column = 0,pady = 10,sticky = "ew")

        self.quick_setup = ctk.CTkLabel(self.right_scrollable_frame,text = "Quick Setup",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.quick_setup.grid(row = 2,column = 0,sticky = "nw",padx = (10,0))

        self.visual_theme = ctk.CTkLabel(self.right_scrollable_frame,text = "Create a visual theme for your website and\nregistration pages.",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.visual_theme.grid(row = 3,column = 0,sticky = "nw",padx = (10,0))

        self.change_theme = ctk.CTkLabel(self.right_scrollable_frame,text = "Theme",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.change_theme.grid(row = 4,column = 0,sticky = "nw",padx = (10,0),pady = 20)

        self.change_theme_button = ctk.CTkButton(self.right_scrollable_frame,text = "Change Theme",height = 30,width = 150,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.change_theme_command)
        self.change_theme_button.grid(row = 4,column = 0,sticky = "ne",padx = (0,10),pady = 20)

        self.line2 = self.common_line()
        self.line2.grid(row = 5,column = 0,sticky = "ew",pady = 10)

        self.logo = ctk.CTkLabel(self.right_scrollable_frame,text = "Logo",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.logo.grid(row = 6,column = 0,sticky = "nw",padx = (10,0))

        self.logo_image_label = ctk.CTkLabel(self.right_scrollable_frame,text = "Logo Image",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.logo_image_label.grid(row = 7,column = 0,sticky = "nw",padx = (10,0),pady = (20,0))

        self.rectangle_frame = ctk.CTkFrame(self.right_scrollable_frame,height = 100,width = 270,border_width = 1,fg_color = "#ffffff",border_color = "lightgray")
        self.rectangle_frame.grid(row = 8,column = 0,sticky = "nw",padx = (10,0),pady = 0)

        self.add_image = ctk.CTkImage(dark_image = Image.open(r"pics\gallery.png"),size = (20,20))
        self.add_image_button = ctk.CTkButton(self.rectangle_frame,image = self.add_image,text = "",height = 10,width = 20,fg_color = "#ffffff",hover_color = "lightgray",command = self.add_image_command)
        self.add_image_button.place(x = 120,y = 30)

        self.add_image_label = ctk.CTkLabel(self.rectangle_frame,text = "Add Image",text_color = "#11A2E3",fg_color = "#ffffff")
        self.add_image_label.place(x = 110, y = 57)

        self.line3 = self.common_line()
        self.line3.grid(row = 9,column = 0,sticky = "ew",pady = 20)

        self.header_background =  ctk.CTkLabel(self.right_scrollable_frame,text = "Header Background Image",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.header_background.grid(row = 10,column = 0,sticky = "nw",padx = (10,0))

        self.header_background_image =  ctk.CTkLabel(self.right_scrollable_frame,text = "Header Background Image",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.header_background_image.grid(row = 11,column = 0,sticky = "nw,",padx = (10,0),pady = (20,0))

        self.header_background_frame = ctk.CTkFrame(self.right_scrollable_frame,height = 200,width = 270,border_width = 1,fg_color = "#000000",border_color = "lightgray")
        self.header_background_frame.grid(row = 12,column = 0,sticky = "nw",padx = (10,0),pady = 0)

        self.edit_image = ctk.CTkButton(self.right_scrollable_frame,text = "Edit Image",height = 30,width = 250,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.edit_image_command)
        self.edit_image.grid(row = 13,column = 0,padx = (10,0),pady = 5)

        self.line4 = self.common_line()
        self.line4.grid(row = 14,column = 0,sticky = "ew",pady = 20)

        self.colors = ctk.CTkLabel(self.right_scrollable_frame,text = "Colors",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.colors.grid(row = 15,column = 0,sticky = "nw",padx = (10,0))

        self.finished = ctk.CTkButton(self.right_scrollable_frame,text = "Finished",height = 30,width = 250,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.finished_command)
        self.finished.grid(row = 16,column = 0,padx = (10,0),pady = 20)
