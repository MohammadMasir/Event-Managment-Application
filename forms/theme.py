import customtkinter as ctk 
from PIL import Image
import tkinter as tk 

class ThemeDesigner():
    def __init__(self, parent_frame, form):
        super().__init__()
        self.form = form
        self.parent = parent_frame

    def theme_color_palette(self, theme_name, color_names, primary, secondary, bg_color, text_color, hover_color, font):
        ctk.CTkLabel(self.parent, text=theme_name, font=(15, "Segoue UI")).pack(side="left", pady=(10,0))
        theme_frame = tk.Frame(self.parent, relief="raised", borderwidth=1, bg="white")
        theme_frame.pack(fill="x", padx=20, pady=(10,0))

        color_frame = ctk.CTkFrame(theme_frame, fg_color=color_names[0])
        color_frame.pack(fill="both")

        options_frame = ctk.CTkFrame(theme_frame, fg_color="transparent")
        options_frame.pack(fill="both")

        for colors in color_names:
            ctk.CTkButton(options_frame, text="", fg_color=colors, width=10, height=10).pack(side="left", padx=(5,0))

        ctk.CTkLabel(options_frame, text="AaBbCc 123", font=(15, font)).pack(side="left", padx=5)

    def change_theme_command(self):
        for widget in self.parent.winfo_children():
            widget.pack_forget()

        ctk.CTkLabel(self.parent, text="Standard Themes", font=(17, "Segoue UI", "bold")).pack(side="left")


    def add_image_command(self):
        pass

    def edit_image_command(self):
        pass
    
    def finished_command(self):
        pass

    def common_line(self):
        canvas = tk.Canvas(self.parent,height = 1,bg = "lightgray",relief = tk.SUNKEN)
        return canvas

    def Theme_structure(self):
        self.theme = ctk.CTkLabel(self.parent,text = "Theme",text_color = "#000000",font = ctk.CTkFont(size = 25,weight = "bold"), compound="center")
        self.theme.grid(row = 0,column = 0,padx = 100,pady = 10)

        self.line1 = self.common_line()
        self.line1.grid(row = 1,column = 0,pady = 10,sticky = "ew")

        self.quick_setup = ctk.CTkLabel(self.parent,text = "Quick Setup",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.quick_setup.grid(row = 2,column = 0,sticky = "nw",padx = (10,0))

        label_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        label_frame.grid(row = 3,column = 0, sticky="nsew")

        self.visual_theme = ctk.CTkLabel(label_frame,text = "Create a visual theme for your website and\nregistration pages.",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.visual_theme.pack(side="left", padx=10)

        self.theme_button_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.theme_button_frame.grid(row=4, column=0, sticky="nsew",pady=10)

        self.change_theme = ctk.CTkLabel(self.theme_button_frame,text = "Theme",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.change_theme.pack(side="left", padx=(10,0))

        self.change_theme_button = ctk.CTkButton(self.theme_button_frame,text = "Change Theme",height = 30,width = 110,corner_radius = 12,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.change_theme_command)
        self.change_theme_button.pack(side="right", padx=(0,50))

        self.line2 = self.common_line()
        self.line2.grid(row = 5,column = 0,sticky = "ew",pady = 10)

        self.logo = ctk.CTkLabel(self.parent,text = "Logo",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.logo.grid(row = 6,column = 0,sticky = "nw",padx = (10,0))

        self.logo_image_label = ctk.CTkLabel(self.parent,text = "Logo Image",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.logo_image_label.grid(row = 7,column = 0,sticky = "nw",padx = (10,0),pady = (20,0))

        self.rectangle_frame = ctk.CTkFrame(self.parent,height = 100,width = 270,border_width = 1,fg_color = "#ffffff",border_color = "lightgray")
        self.rectangle_frame.grid(row = 8,column = 0,sticky = "nw",padx = (10,0),pady = 0)

        self.add_image = ctk.CTkImage(dark_image = Image.open(r"pics\gallery.png"),size = (20,20))
        self.add_image_button = ctk.CTkButton(self.rectangle_frame,image = self.add_image,text = "",height = 10,width = 20,fg_color = "#ffffff",hover_color = "lightgray",command = self.add_image_command)
        self.add_image_button.place(x = 120,y = 30)

        self.add_image_label = ctk.CTkLabel(self.rectangle_frame,text = "Add Image",text_color = "#11A2E3",fg_color = "#ffffff")
        self.add_image_label.place(x = 110, y = 57)

        self.line3 = self.common_line()
        self.line3.grid(row = 9,column = 0,sticky = "ew",pady = 20)

        self.header_background =  ctk.CTkLabel(self.parent,text = "Header Background Image",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.header_background.grid(row = 10,column = 0,sticky = "nw",padx = (10,0))

        self.header_background_image =  ctk.CTkLabel(self.parent,text = "Header Background Image",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.header_background_image.grid(row = 11,column = 0,sticky = "nw,",padx = (10,0),pady = (20,0))

        self.header_background_frame = ctk.CTkFrame(self.parent,height = 200,width = 270,border_width = 1,fg_color = "#000000",border_color = "lightgray")
        self.header_background_frame.grid(row = 12,column = 0,sticky = "nw",padx = (10,0),pady = 0)

        self.edit_image = ctk.CTkButton(self.parent,text = "Edit Image",height = 30,width = 250,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.edit_image_command)
        self.edit_image.grid(row = 13,column = 0,padx = (10,0),pady = 5)

        self.line4 = self.common_line()
        self.line4.grid(row = 14,column = 0,sticky = "ew",pady = 20)

        self.colors = ctk.CTkLabel(self.parent,text = "Colors",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.colors.grid(row = 15,column = 0,sticky = "nw",padx = (10,0))

        self.finished = ctk.CTkButton(self.parent,text = "Finished",height = 30,width = 250,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.finished_command)
        self.finished.grid(row = 16,column = 0,padx = (10,0),pady = 20)

