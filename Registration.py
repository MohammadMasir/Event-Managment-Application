import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

class RegistrationPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x700")

        self.three_lines_image = ctk.CTkImage(dark_image = Image.open(r"pics\lines.png"),size = (25,25))
        self.search_widget_image = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (20,20))
        self.preview_button_image = ctk.CTkImage(dark_image = Image.open(r"pics\view.png"),size = (25,25))
        self.build_image = ctk.CTkImage(dark_image = Image.open(r"pics\pending.png"),size = (15,15))

        self.toggle_fullscreen()
        self.bind("<F11>", self.toggle_fullscreen)

        self.registeration_home()

    def toggle_fullscreen(self, event=None):
        # Set the application to fullscreen mode
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", self.exit_fullscreen)

    def exit_fullscreen(self, event=None):
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        # Exit fullscreen mode
        self.attributes('-fullscreen', False)
        self.resizable(width=True, height=True)
        self.geometry(f'{width - 200}x{height-100}')
        self.maxsize(width,height)

    def customize(
                  self, 
                  parent,
                  function, 
                  row=None, 
                  column=None, 
                  sticky=None, 
                  padx=None, 
                  pady=None,  
                  side=None, 
                  anchor=None, 
                  fill=None):

        if row is None:
            customize_button = ctk.CTkButton(parent,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = function)
            customize_button.pack(side=side, anchor=anchor, fill=fill,padx=padx,pady=pady)
        else:
            customize_button = ctk.CTkButton(parent,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = function)
            customize_button.grid(row = row,column = column,sticky = sticky,padx = padx,pady = pady)

    def registeration_home(self):        
        self.top_frame = ctk.CTkFrame(self,height = 55,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
        self.top_frame.pack(pady = (0,0),fill = "x")

        self.three_lines_image_label = ctk.CTkButton(self.top_frame,image = self.three_lines_image,text = "",hover_color = "lightgray",fg_color = "#ffffff",width = 5,command = self.three_lines)
        self.three_lines_image_label.grid(row = 0,column = 0,padx = (5,7),pady = 5)
        
        demeven_bind = tk.StringVar()
        text = "DemEven"
        demeven_bind.set(text)
        self.demeven_label = ctk.CTkLabel(self.top_frame,text_color = "#000000",textvariable = demeven_bind,font = ctk.CTkFont(size = 20,weight = "bold"))
        self.demeven_label.grid(row = 0,column = 1,padx = (0,650),pady = 5)

        self.search_widget = ctk.CTkEntry(self.top_frame,height = 35,width = 250,fg_color = "#ffffff",corner_radius = 20,text_color = "#000000",placeholder_text = "Search this event",placeholder_text_color = "#000000")
        self.search_widget.grid(row = 0,column = 2,padx = (0,35),pady = 5)

        self.search_widget_image_button = ctk.CTkButton(self.search_widget,image = self.search_widget_image,corner_radius = 70,text = "",height = 15,width = 20,hover_color = "lightgray",fg_color = "#ffffff",command = self.search_widget_command)
        self.search_widget_image_button.place(x = 200,y = 3)

        self.preview_button = ctk.CTkButton(self.top_frame,text = "Preview",height = 35,width = 100,hover_color = "#ffffff",text_color = "#0B77E3",corner_radius = 5,fg_color = "#ffffff",border_width = 1,border_color = "#0B77E3",command = self.preview_button_command)
        self.preview_button.grid(row = 0,column = 3,padx = (25,0),pady = (6),ipadx = 25)

        self.preview_button_image_label = ctk.CTkLabel(self.preview_button,image = self.preview_button_image,height = 5,text = "",fg_color = "#ffffff")
        self.preview_button_image_label.place(x = 9,y = 5)

        self.left_frame = ctk.CTkFrame(self,width = 250,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
        self.left_frame.pack(padx = 0,pady = 0,side = "left",fill = "y")

        self.home_label = ctk.CTkLabel(self.left_frame,text = "HOME",width = 10,text_color = "#000000",font = (ctk.CTkFont(size = 20,weight = "normal")))
        self.home_label.place(x = 15,y = 5)

        general_bind = tk.StringVar()
        general_bind.set("General")
        self.general_dropdown = ctk.CTkOptionMenu(self.left_frame,variable = general_bind,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
        self.general_dropdown.grid(row = 1,column = 0,padx = 10,pady = (40,0))
        
        registration_bind = tk.StringVar()
        registration_bind.set("Registration")
        self.registration_dropdown = ctk.CTkOptionMenu(self.left_frame,variable = registration_bind,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
        self.registration_dropdown.grid(row = 2,column = 0,padx = 10,pady = (10,0))
        
        marketing_bind = tk.StringVar()
        marketing_bind.set("Marketing")
        self.marketing_dropdown = ctk.CTkOptionMenu(self.left_frame,variable = marketing_bind,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
        self.marketing_dropdown.grid(row = 3,column = 0,padx = 10,pady = (10,0))
        
        email_bind = tk.StringVar()
        email_bind.set("Email")
        self.email_dropdown = ctk.CTkOptionMenu(self.left_frame,variable = email_bind,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
        self.email_dropdown.grid(row = 3,column = 0,padx = 10,pady = (10,0))
        
        attendees_bind = tk.StringVar()
        attendees_bind.set("Attendees")
        self.attendees_dropdown = ctk.CTkOptionMenu(self.left_frame,variable = attendees_bind,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
        self.attendees_dropdown.grid(row = 4,column = 0,padx = 10,pady = (10,0))
        
        survey_bind = tk.StringVar()
        survey_bind.set("Surveys")
        self.survey_dropdown = ctk.CTkOptionMenu(self.left_frame,variable = survey_bind,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
        self.survey_dropdown.grid(row = 5,column = 0,padx = 10,pady = (10,0))
        
        reports_bind = tk.StringVar()
        reports_bind.set("Reports")
        self.reports_dropdown = ctk.CTkOptionMenu(self.left_frame,variable = reports_bind,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
        self.reports_dropdown.grid(row = 6,column = 0,padx = 10,pady = (10,0))

        self.scrollable_frame = ctk.CTkScrollableFrame(self,height = 1000,fg_color = "#F0F0F0")
        self.scrollable_frame.pack(anchor = "nw",fill = "x")

        self.registration_process_frame = ctk.CTkFrame(self.scrollable_frame,height = 100,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
        self.registration_process_frame.pack(anchor = "nw",fill = "x",padx = 0,pady = 0)

        self.registration_process_label = ctk.CTkLabel(self.registration_process_frame,height = 70,text = "Registration Process",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 25,weight = "normal"))
        self.registration_process_label.pack(side = "left",padx = 30,pady = 10)

        self.build_and_image_frame = ctk.CTkFrame(self.scrollable_frame,height = 50,fg_color = "#F0F0F0")
        self.build_and_image_frame.pack(anchor = "nw",fill = "x")

        self.build_label = ctk.CTkLabel(self.build_and_image_frame,text = "Design & Build Your Registration Process",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.build_label.grid(row = 0,column = 0,padx = (10,0))

        self.build_image_label = ctk.CTkLabel(self.build_and_image_frame,image = self.build_image,text = "",height = 5,width = 2)
        self.build_image_label.grid(row = 0,column = 1,padx = (10,0))

        self.get_started_label = ctk.CTkLabel(self.scrollable_frame,text = "To get started, lauch our new Site Designer, or start customizing one of the pages below.",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
        self.get_started_label.pack(anchor = "nw",padx = 10,pady = 10)

        self.open_site_designer_button = ctk.CTkButton(self.scrollable_frame,text = "Open Site Designer",text_color = "#ffffff",fg_color = "#0B77E3",height = 25,width = 50,hover_color = "blue",corner_radius = 10,command = self.site_designer)
        self.open_site_designer_button.pack(anchor = "nw",padx = 10,pady = 10)

        self.registration_process_pages_frame = ctk.CTkFrame(self.scrollable_frame,fg_color = "#ffffff",width = 800,height = 1000)
        self.registration_process_pages_frame.pack(fill="x",anchor = "nw",padx = (0,100))

        self.registration_process_pages_label = ctk.CTkLabel(self.registration_process_pages_frame,text = "Registration Process Pages",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.registration_process_pages_label.grid(row = 0,column = 0,padx = 10,pady = (20,0))

        self.personal_info_label = ctk.CTkLabel(self.registration_process_pages_frame,text = "Personal Information",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.personal_info_label.grid(row = 1,column = 0,padx = 10,pady = 20)

        self.customize(self.registration_process_pages_frame, self.personal_info, row = 1,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        self.registration_summary = ctk.CTkLabel(self.registration_process_pages_frame,text = "Registration Summary",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.registration_summary.grid(row = 3,column = 0,padx = 10,pady = 20)

        self.customize(self.registration_process_pages_frame, self.registration_summary, row = 3,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        self.post_registration = ctk.CTkLabel(self.registration_process_pages_frame,text = "Post Registration",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.post_registration.grid(row = 4,column = 0,sticky = "nw",padx = 10,pady = (20,0))

        self.confirmation = ctk.CTkLabel(self.registration_process_pages_frame,text = "Confirmation",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.confirmation.grid(row = 5,column = 0,sticky = "nw",padx = 40,pady = 20)

        self.customize(self.registration_process_pages_frame, self.confirmation_button, row = 5,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        self.other = ctk.CTkLabel(self.registration_process_pages_frame,text = "Others",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.other.grid(row = 6,column = 0,sticky = "nw",padx = 10,pady = (20,0))

        self.cancellation = ctk.CTkLabel(self.registration_process_pages_frame,text = "Cancellation Form",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.cancellation.grid(row = 7,column = 0,sticky = "nw",padx = 40,pady = 20)

        self.customize(self.registration_process_pages_frame, self.cancellation_button, row = 7,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        self.decline = ctk.CTkLabel(self.registration_process_pages_frame,text = "Decline Form",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.decline.grid(row = 8,column = 0,sticky = "nw",padx = 40,pady = 20)

        self.customize(self.registration_process_pages_frame, self.cancellation_button, row = 8,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        self.guest = ctk.CTkLabel(self.registration_process_pages_frame,text = "Guest Information",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.guest.grid(row = 9,column = 0,sticky = "nw",padx = 40,pady = 20)

        self.customize(self.registration_process_pages_frame, self.guest_button, row = 9,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))


    def three_lines(self):
        pass

    def search_widget_command(self):
        pass

    def preview_button_command(self):
        pass

    def site_designer(self):
        pass

    def personal_info(self):
        pass

    def registration_summary(self):
        pass

    def confirmation_button(self):
        pass

    def cancellation_button(self):
        pass
    
    def guest_button(self):
        pass

if __name__ == "__main__":
    final_screen = RegistrationPage()
    final_screen.mainloop()
