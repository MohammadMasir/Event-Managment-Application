import tkinter as tk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from PIL import Image
# from eventcreate import CreateEvent

class Page():
    def __init__(self, main_app, parent=None, event_name=None, heading=None, heading2=None, heading3=None):
        super().__init__()
        self.main = main_app
        self.parent = parent

        self.title = event_name
        self.heading_1 = heading
        self.heading_2 = heading2 # font = ctk.CTkFont(size = 17,weight = "bold")
        self.heading_3 = heading3 # font = ctk.CTkFont(size = 15,weight = "normal")

        self.click_count = 0
        self.sidebar = None

    def switch_tab(self, tab_name, method=None):
        self.main.notebook.set(tab_name)
        return method

    def navigate(self, destination):
        if callable(destination):
            destination()
            print("Navigation is called....")
        else:
            print(f"Navigation destination '{destination}' is not callable")

    def create_sidebar_item(self, label, subitems):
        frame = ctk.CTkFrame(self.sidebar, corner_radius=0)
        frame.pack(fill="x", pady=(0, 1))

        # Create a sub-frame for the button content
        button_frame = ctk.CTkFrame(frame, corner_radius=0, fg_color="#20807f")
        button_frame.pack(fill="x",ipady=5)

        # Label on the left
        label_widget = ctk.CTkButton(button_frame, text=label, anchor="w", font=ctk.CTkFont(family="Segoe UI",size=15, weight="bold"), command=lambda: self.toggle_subitems(frame, subitems), fg_color="#20807f", text_color="white")
        label_widget.pack(side="left")

        # Arrow on the right
        arrow_label = ctk.CTkLabel(button_frame, text="▼", anchor="e")
        arrow_label.pack(side="right", padx=(0, 5))

        # Make the whole frame clickable
        button_frame.bind("<Button-1>", lambda event: self.toggle_subitems(frame, subitems))

        # Create hidden frame for subitems
        subframe = ctk.CTkFrame(frame, corner_radius=20, fg_color="#093838")
        subframe.pack(fill="x")
        subframe.pack_forget()  # Initially hidden

        # Create buttons for subitems
        for item, command in subitems.items():
            sub_button = ctk.CTkButton(subframe, text=f"  • {item}", anchor="w", fg_color="transparent", hover_color="#20605f", text_color="white", font=ctk.CTkFont(size=13, weight="bold"), command=lambda c=command: self.navigate(c))
            sub_button.pack(fill="x")


    def toggle_subitems(self, frame, subitems,event=None):
        subframe = frame.winfo_children()[1]  # The subframe
        arrow_label = frame.winfo_children()[0].winfo_children()[1]  # The arrow label

        if subframe.winfo_viewable():
            subframe.pack_forget()
            arrow_label.configure(text="▼")
        else:
            subframe.pack(fill="x")
            arrow_label.configure(text="▲")

    def fun(self):
        pass

    def menu_animation(self):
        self.click_count += 1
     
        # Conditionally create sidebar on first click
        if self.click_count % 2 != 0 and self.sidebar is None:
            self.sidebar = ctk.CTkScrollableFrame(self.page_frame, width=240, fg_color="#F0F0F0")
            self.sidebar.pack(side="left", fill="y")

            corner_colors = ("white", "white", "#6bceba", "#6bceba")
            # Add the sidebar content here (create_sidebar_item calls)
            self.home_button = ctk.CTkButton(self.sidebar, text="Home", fg_color="#6bceba", text_color="white", background_corner_colors=corner_colors, font=ctk.CTkFont(family="Segoe UI",size=15, weight="bold"), hover_color="#8bceba",command=self.main.events.events_home)
            self.home_button.pack(fill="x", anchor="center")
            self.create_sidebar_item("General", {
                "Event Information" : self.main.events.event_information,
                "Event Features" : self.main.events.event_features, 
                "Registration Types" : self.main.register_page.registration_types, 
                "Event Settings" : self.main.events.event_settings
                })
            self.create_sidebar_item("Registration", {
                "Registration Settings" : self.main.register_page.registration_settings, 
                "Registration Proccess" : lambda : self.switch_tab("Registration and Ticketing", self.main.registertab_widgets())
                })
            self.create_sidebar_item("Email", {
                "Invitation List" : lambda : self.switch_tab("Invitee & Attendee", self.main.invitation_attendee.invitation_list_screen),
                "Event Emails" : self.main.invitation_attendee.event_emails, 
                "Planner Alerts" : self.main.invitation_attendee.planner_alerts
                })
            self.create_sidebar_item("Attendees", {
                "Attendee List" : self.main.invitation_attendee.attendee_list_screen, 
                "Certificates" : self.main.invitation_attendee.certificates_screen
                })
            self.create_sidebar_item("Surveys", {
                "Feedback Surveys" : lambda : self.switch_tab("Survey and Feedback", self.main.survey_response.feedback_surveys_screen), 
                "Responses" : self.main.survey_response.responses_screen
                })
            self.create_sidebar_item("Reports", {
                "Reports" : lambda : self.main.notebook.set("Dashboard"), 
                "Invitee Summary" : lambda : self.main.notebook.set("Dashboard")
                })
            # ... add more sidebar items
            self.scrollable_frame.pack(side="right",fill="both")
        # Show/hide sidebar based on click count
        if self.click_count % 2 != 0:
            self.sidebar.pack(side="left", anchor="ne",fill="y")
            self.scrollable_frame.pack(side="right",fill="both")
        else:
            if self.sidebar is not None:
                self.sidebar.pack_forget()
                self.scrollable_frame.pack(fill = "both")

    def search_widget_command(self):
        pass
    def preview_button_command(self):
        pass    

    def title_frame(self, preview_status):
        self.page_frame = ctk.CTkFrame(self.parent, fg_color="#F0F0F0")
        self.page_frame.pack(fill="both", expand=True)

        weight = "bold"
        if not preview_status:
            weight = "normal"
        else:
            weight = "bold"
        self.top_frame = ctk.CTkFrame(self.page_frame,height = 55,fg_color = "#ffffff",border_width = 1,border_color = "lightgray", corner_radius=0)
        self.top_frame.pack(fill = "x",ipady=5)

        self.three_lines_image = ctk.CTkImage(dark_image = Image.open(r"pics\lines.png"),size = (25,25))
        self.three_lines_image_label = ctk.CTkButton(self.top_frame,image = self.three_lines_image,text = "",hover_color = "lightgray",fg_color = "#ffffff",width = 5,command = self.menu_animation)
        self.three_lines_image_label.pack(side="left")
        
        demeven_bind = tk.StringVar()

        text = self.title
        demeven_bind.set(text)
        self.demeven_label = ctk.CTkLabel(self.top_frame,text_color = "#000000",textvariable = demeven_bind,font = ctk.CTkFont(size = 20,weight = weight))
        self.demeven_label.pack(side="left")

        if preview_status:
            self.preview_button = ctk.CTkButton(self.top_frame,text = "Preview",height = 35,width = 150,hover_color = "#ffffff",text_color = "#0B77E3",corner_radius = 5,fg_color = "#ffffff",border_width = 1,border_color = "#0B77E3",command = self.preview_button_command)
            self.preview_button.pack(side="right", padx=(0,10))

            self.preview_button_image = ctk.CTkImage(dark_image = Image.open(r"pics\view.png"),size = (25,25))
            self.preview_button_image_label = ctk.CTkLabel(self.preview_button,image = self.preview_button_image,height = 5,text = "",fg_color = "#ffffff")
            self.preview_button_image_label.place(x = 9,y = 5)

        self.search_widget = ctk.CTkEntry(self.top_frame,height = 35,width = 250,fg_color = "#ffffff",corner_radius = 20,text_color = "#000000",placeholder_text = "Search this event",placeholder_text_color = "#000000")
        self.search_widget.pack(side="right", padx=(0,10))

        self.search_widget_image = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (20,20))
        self.search_widget_image_button = ctk.CTkButton(self.search_widget,image = self.search_widget_image,corner_radius = 70,text = "",height = 15,width = 20,hover_color = "lightgray",fg_color = "#ffffff",command = self.search_widget_command)
        self.search_widget_image_button.place(x = 200,y = 3)

    def content_frame(self):
        self.scrollable_frame = ctk.CTkScrollableFrame(self.page_frame,fg_color = "#F0F0F0")
        self.scrollable_frame.pack(fill = "both",expand=True)

        self.upper_frame = ctk.CTkFrame(self.scrollable_frame,height = 100,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
        self.upper_frame.pack(anchor = "ne",fill = "both",expand=True,padx = 0,pady = 0)
        self.upper_frame_heading = ctk.CTkLabel(self.upper_frame,height = 70,text = self.heading_1, fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 25,weight = "normal")) #"Registration Process Pages"
        self.upper_frame_heading.pack(side = "top",padx = 30,pady = 10, anchor="nw")

        self.widget_frame = ctk.CTkFrame(self.scrollable_frame,fg_color = "#ffffff",width = 800,height = 1000)
        self.widget_frame.pack(anchor = "nw",padx = 10)

        self.widget_label = ctk.CTkLabel(self.widget_frame,text = self.heading_2,text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.widget_label.pack()