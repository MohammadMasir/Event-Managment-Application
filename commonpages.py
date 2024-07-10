import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

class Page1():
    def __init__(self, main_app, title):
        super().__init__()
        self.main_app = main_app
        self.page_frame = ctk.CTkFrame(self.main_app.register_tab)
        self.page_frame.pack(fill="both", expand=True)

        self.title = title

        self.click_count = 0
        self.sidebar = None

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
        for item in subitems:
            sub_button = ctk.CTkButton(subframe, text=f"  • {item}", anchor="w", fg_color="transparent", hover_color=("gray70", "gray30"), text_color="white", font=ctk.CTkFont(size=13, weight="bold"))
            sub_button.pack(fill="x")

    def toggle_subitems(self, frame, subitems):
        subframe = frame.winfo_children()[1]  # The subframe
        arrow_label = frame.winfo_children()[0].winfo_children()[1]  # The arrow label

        if subframe.winfo_viewable():
            subframe.pack_forget()
            arrow_label.configure(text="▼")
        else:
            subframe.pack(fill="x")
            arrow_label.configure(text="▲")

    def menu_animation(self):
        self.click_count += 1

        # Conditionally create sidebar on first click
        if self.click_count % 2 != 0 and self.sidebar is None:
            self.sidebar = ctk.CTkScrollableFrame(self.page_frame, width=240, fg_color="#F0F0F0")
            self.sidebar.pack(side="left", fill="y")

            # Add the sidebar content here (create_sidebar_item calls)
            self.create_sidebar_item("General", ["Option 1", "Option 2"])
            self.create_sidebar_item("Registration", ["Register", "Unregister"])
            self.create_sidebar_item("Marketing", ["Campaigns", "Analytics"])
            self.create_sidebar_item("Email", ["Compose", "Inbox", "Sent"])
            self.create_sidebar_item("Attendees", ["List", "Groups"])
            self.create_sidebar_item("Surveys", ["Feedback Surveys", "Responses"])
            self.create_sidebar_item("Reports", ["Generate", "View"])
            self.create_sidebar_item("Integrations", ["Connect", "Manage"])
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

    def register_initial(self):
        self.top_frame = ctk.CTkFrame(self.page_frame,height = 55,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
        self.top_frame.pack(fill = "x")

        self.three_lines_image = ctk.CTkImage(dark_image = Image.open(r"pics\lines.png"),size = (25,25))
        self.three_lines_image_label = ctk.CTkButton(self.top_frame,image = self.three_lines_image,text = "",hover_color = "lightgray",fg_color = "#ffffff",width = 5,command = self.menu_animation)
        self.three_lines_image_label.grid(row = 0,column = 0,padx = (5,7),pady = 5)
        
        demeven_bind = tk.StringVar()
        text = "DemEven"
        demeven_bind.set(text)
        self.demeven_label = ctk.CTkLabel(self.top_frame,text_color = "#000000",textvariable = demeven_bind,font = ctk.CTkFont(size = 20,weight = "bold"))
        self.demeven_label.grid(row = 0,column = 1,padx = (0,650),pady = 5)

        self.search_widget = ctk.CTkEntry(self.top_frame,height = 35,width = 250,fg_color = "#ffffff",corner_radius = 20,text_color = "#000000",placeholder_text = "Search this event",placeholder_text_color = "#000000")
        self.search_widget.grid(row = 0,column = 2,padx = (0,35),pady = 5)

        self.search_widget_image = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (20,20))
        self.search_widget_image_button = ctk.CTkButton(self.search_widget,image = self.search_widget_image,corner_radius = 70,text = "",height = 15,width = 20,hover_color = "lightgray",fg_color = "#ffffff",command = self.search_widget_command)
        self.search_widget_image_button.place(x = 200,y = 3)

        self.preview_button = ctk.CTkButton(self.top_frame,text = "Preview",height = 35,width = 100,hover_color = "#ffffff",text_color = "#0B77E3",corner_radius = 5,fg_color = "#ffffff",border_width = 1,border_color = "#0B77E3",command = self.preview_button_command)
        self.preview_button.grid(row = 0,column = 3,padx = (25,0),pady = (6),ipadx = 25)

        self.preview_button_image = ctk.CTkImage(dark_image = Image.open(r"pics\view.png"),size = (25,25))
        self.preview_button_image_label = ctk.CTkLabel(self.preview_button,image = self.preview_button_image,height = 5,text = "",fg_color = "#ffffff")
        self.preview_button_image_label.place(x = 9,y = 5)

        self.scrollable_frame = ctk.CTkScrollableFrame(self.page_frame,fg_color = "#F0F0F0")
        self.scrollable_frame.pack(fill = "both",expand=True)

        self.registration_process_frame = ctk.CTkFrame(self.scrollable_frame,height = 100,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
        self.registration_process_frame.pack(anchor = "ne",fill = "both",expand=True,padx = 0,pady = 0)

        self.registration_process_label = ctk.CTkLabel(self.registration_process_frame,height = 70,text = self.title,fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 25,weight = "normal"))
        self.registration_process_label.pack(side = "left",padx = 30,pady = 10)

        self.build_and_image_frame = ctk.CTkFrame(self.scrollable_frame,height = 50,fg_color = "#F0F0F0")
        self.build_and_image_frame.pack(anchor = "nw",fill = "x")

        self.build_label = ctk.CTkLabel(self.build_and_image_frame,text = "Design & Build Your Registration Process",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.build_label.grid(row = 0,column = 0,padx = (10,0))

        self.build_image = ctk.CTkImage(dark_image = Image.open(r"pics\pending.png"),size = (15,15))
        self.build_image_label = ctk.CTkLabel(self.build_and_image_frame,image = self.build_image,text = "",height = 5,width = 2)
        self.build_image_label.grid(row = 0,column = 1,padx = (10,0))

        self.get_started_label = ctk.CTkLabel(self.scrollable_frame,text = "To get started, lauch our new Site Designer, or start customizing one of the pages below.",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
        self.get_started_label.pack(anchor = "nw",padx = 10,pady = 10)

        self.open_site_designer_button = ctk.CTkButton(self.scrollable_frame,text = "Open Site Designer",text_color = "#ffffff",fg_color = "#0B77E3",height = 25,width = 50,hover_color = "blue",corner_radius = 10,command = self.site_designer)
        self.open_site_designer_button.pack(anchor = "nw",padx = 10,pady = 10)

        self.registration_process_pages_frame = ctk.CTkFrame(self.scrollable_frame,fg_color = "#ffffff",width = 800,height = 1000)
        self.registration_process_pages_frame.pack(anchor = "nw",padx = 10)

        self.registration_process_pages_label = ctk.CTkLabel(self.registration_process_pages_frame,text = "Registration Process Pages",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.registration_process_pages_label.grid(row = 0,column = 0,padx = 10,pady = (20,0))

        self.personal_info_label = ctk.CTkLabel(self.registration_process_pages_frame,text = "Personal Information",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.personal_info_label.grid(row = 1,column = 0,padx = 10,pady = 20)

        self.personal_info_button = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.personal_info)
        self.personal_info_button.grid(row = 1,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        #self.canvas_line1 = tk.Canvas(self.registration_process_pages_frame,height = 2,width = 1000,bg = "lightgray",relief = tk.SUNKEN)
        #self.canvas_line1.place(x = 60,y = 150)

        self.registration_summary = ctk.CTkLabel(self.registration_process_pages_frame,text = "Registration Summary",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.registration_summary.grid(row = 3,column = 0,padx = 10,pady = 20)

        self.registration_summary_button = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.registration_summary)
        self.registration_summary_button.grid(row = 3,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        #self.canvas_line2 = tk.Canvas(self.registration_process_pages_frame,height = 2,width = 1000,bg = "lightgray",relief = tk.SUNKEN)
        #self.canvas_line2.place(x = 60,y = 250)

        self.post_registration = ctk.CTkLabel(self.registration_process_pages_frame,text = "Post Registration",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.post_registration.grid(row = 4,column = 0,sticky = "nw",padx = 10,pady = (20,0))

        self.confirmation = ctk.CTkLabel(self.registration_process_pages_frame,text = "Confirmation",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.confirmation.grid(row = 5,column = 0,sticky = "nw",padx = 40,pady = 20)

        self.confirmation_button = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.confirmation_button)
        self.confirmation_button.grid(row = 5,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        self.other = ctk.CTkLabel(self.registration_process_pages_frame,text = "Others",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.other.grid(row = 6,column = 0,sticky = "nw",padx = 10,pady = (20,0))

        self.cancellation = ctk.CTkLabel(self.registration_process_pages_frame,text = "Cancellation Form",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.cancellation.grid(row = 7,column = 0,sticky = "nw",padx = 40,pady = 20)

        self.cancellation_button = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.cancellation_button)
        self.cancellation_button.grid(row = 7,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        self.decline = ctk.CTkLabel(self.registration_process_pages_frame,text = "Decline Form",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.decline.grid(row = 8,column = 0,sticky = "nw",padx = 40,pady = 20)

        self.decline_button = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.cancellation_button)
        self.decline_button.grid(row = 8,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))

        self.guest = ctk.CTkLabel(self.registration_process_pages_frame,text = "Guest Information",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.guest.grid(row = 9,column = 0,sticky = "nw",padx = 40,pady = 20)

        self.guest_button = ctk.CTkButton(self.registration_process_pages_frame,text = "Customize",fg_color = "#ffffff",hover_color = "lightgray",width = 40,text_color = "#0B77E3",command = self.guest_button)
        self.guest_button.grid(row = 9,column = 2,sticky = "ne",padx = (290,40),pady = (20,0))


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