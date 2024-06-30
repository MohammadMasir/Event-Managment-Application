import customtkinter as ctk
from PIL import Image
import tkinter as tk

class DemoApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.resizable(width=True, height=True)
        self.title("DemoApplication")
        self.configure(fg_color="#093838")
    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("my_custom_theme")

        self.primary_color = "#093838"
        self.secondary_color = "#8bceba"
        self.bg = "gainsboro"
        self.text_color = "#092928"
        self.hovercolor_bg = "#20807f"
        self.hovercolor_txt = "white"

        self.click_count = 0
        self.f3 = None
        self.create_widgets()

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
        self.maxsize(width, height)
        # self.minsize(width, height)

    def create_widgets(self):
        self.toggle_fullscreen()
        self.bind("<F11>", self.toggle_fullscreen)

        frame2 = ctk.CTkFrame(self, height=30, fg_color=self.bg)
        frame2.pack(fill="x")

        labe = ctk.CTkLabel(frame2, text="Event Manager", font=("Segoe UI", 30, "bold"), text_color="white", fg_color=self.secondary_color, corner_radius=12)
        labe.pack(pady=10, ipady=7)

        # Create a notebook (tabbed interface)
        notebook = ctk.CTkTabview(self, width=700, height=500, bg_color="gainsboro", corner_radius=12)  # 3fa572 #333333
        notebook.pack(padx=20, pady=20, fill="both", expand=True)
        # notebook.set(self.event_tab)

        # Event Management Tab
        self.event_tab = notebook.add("Event Management")

        self.content_frame = ctk.CTkFrame(self.event_tab, fg_color="#F0F0F0")
        self.content_frame.place(relx=0.0, y=82, relwidth=1, relheight=1)

        self.events_home()

        # Registration and Ticketing Tab
        self.ticket_tab = notebook.add("Registration and Ticketing")
        self.tickettab_widgets()

        # Reporting and Analytics Tab
        self.report_tab = notebook.add("Reporting and Analytics")
        self.reporttab_widgets()

        # Survey and Feedback Tab
        self.survey_tab = notebook.add("Survey and Feedback")
        self.surveytab_widgets()

    def create_sidebar_item(self, label, subitems):
        frame = ctk.CTkFrame(self.f3, corner_radius=0)
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
        if self.click_count % 2 != 0 and self.f3 is None:
            self.f3 = ctk.CTkScrollableFrame(self.content_frame, height = 400, width=240, fg_color="#F0F0F0")
            self.f3.place(relheight=1,relx=0, y=0)

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
            self.f0.place_configure(relheight=1,relx=0.21, y=0, relwidth=1)
        # Show/hide sidebar based on click count
        if self.click_count % 2 != 0:
            self.f3.place(relheight=1,relx=0, y=0)
            self.f0.place_configure(relheight=1,relx=0.21, y=0, relwidth=1)
        else:
            if self.f3 is not None:
                self.f3.place_forget()
                self.f0.place_configure(relheight=1,relx=0, y=0, relwidth=1.0)

    def events_home(self):
        # Main frame
        main_frame = ctk.CTkFrame(self.event_tab, fg_color="#F0F0F0")
        main_frame.pack(fill="both", expand=True)

#-----------------------
#-----------------------

        # Top frame
        top_frame = ctk.CTkFrame(main_frame, fg_color="white")
        top_frame.pack(side="top",fill="x", ipady=5)

#-----------------------

        # Logo and title
        logo_frame = ctk.CTkFrame(top_frame, fg_color="white")
        logo_frame.pack(side="left", padx=10)

        label1 = ctk.CTkLabel(logo_frame, text="cvent", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), bg_color="white")
        label1.pack(side="left")

        label2 = ctk.CTkLabel(logo_frame, text="|", font=ctk.CTkFont(size=19, weight="bold"),text_color="black", bg_color="white")
        label2.pack(side="left", padx=10)

        label3 = ctk.CTkLabel(logo_frame, text="EVENTS", text_color="#3fa6fb", font=ctk.CTkFont(size=17, weight="bold"), bg_color="white")
        label3.pack(side="left")

#-----------------------

        # Options
        options_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
        options_frame.pack(side="left", expand=True, fill="x")

        another_frame = ctk.CTkFrame(options_frame, fg_color="white", bg_color="white")
        another_frame.pack(anchor="center")

        label4 = ctk.CTkLabel(another_frame, text="All Events", text_color="black", font=ctk.CTkFont(size=17, weight="normal"))
        label4.pack(side="left", padx=10)

        x1 = ctk.StringVar(value="Calendar")
        opt1 = ctk.CTkComboBox(another_frame, variable=x1, width=100, values=["2020", "2021", "2022", "2023"], fg_color="white", button_color=self.secondary_color, bg_color="white")
        opt1.pack(side="left")

        x2 = ctk.StringVar(value="More")
        opt2 = ctk.CTkComboBox(another_frame, variable=x2, width=90, values=["", "", "", ""], fg_color="white", button_color=self.secondary_color, bg_color="white")
        opt2.pack(side="left", padx=10)

#-----------------------

        # Icons
        icons_frame = ctk.CTkFrame(top_frame, fg_color="white")
        icons_frame.pack(side="right", padx=10)

        for icon_path in ["loupe.png", "file.png", "question.png", "user (1).png", "menu.png"]:
            img = ctk.CTkImage(dark_image=Image.open(f"pics/{icon_path}"), size=(20, 20))
            button = ctk.CTkButton(icons_frame, image=img, text="", width=20, fg_color="white", bg_color="white", hover_color="#3fa6fb")
            button.pack(side="left", padx=2)

#-----------------------
#-----------------------

        top_frame2 = ctk.CTkFrame(main_frame, fg_color=self.secondary_color, corner_radius=0)
        top_frame2.pack(side="top",fill="x", ipady=5, anchor="n")
                    
        img6 = ctk.CTkImage(dark_image=Image.open(r"pics\lines.png"), size=(20, 20))
        butimg6 = ctk.CTkButton(top_frame2, image=img6, text="", fg_color="white", width=20, hover_color="white", command=self.menu_animation)
        butimg6.pack(side="left", padx=10)

        label5 = ctk.CTkLabel(top_frame2, text="DemEven", text_color="black", font=ctk.CTkFont(size=15, weight="normal"))
        label5.pack(side="left")

        x3 =ctk.StringVar()
        e1 = ctk.CTkEntry(top_frame2,height = 28,width = 250,fg_color = "white",corner_radius = 15,placeholder_text = "Search this Event",placeholder_text_color = "gray",text_color = "black",textvariable = x3)
        e1.pack(side="right",padx=(0,10))

        def search():
            pass

        img7 = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (20,15))
        butimg7 = ctk.CTkButton(top_frame2,image = img7,text = "",fg_color = "white",width = 20,border_width = 1,border_color = "black",hover_color = "#8BFAFF",command = search)
        butimg7.pack(side="right", padx=10)

        # Content frame
        self.content_frame = ctk.CTkFrame(main_frame)
        self.content_frame.pack(side="top",fill="both", expand=True)

        # Add your content widgets here, using grid or pack as appropriate

#-----------------------

        self.f0 = ctk.CTkScrollableFrame(self.content_frame,fg_color = "#F0F0F0")
        self.f0.place(relheight = 1, relwidth=1,relx = 0.0,y = 0)

        f01 = ctk.CTkFrame(self.f0,height = 1050,width = 970,fg_color = "#F0F0F0")
        f01.grid(row = 0,column = 0)

        f4 = ctk.CTkFrame(f01,height = 200,width = 970,fg_color = "#ffffff")
        f4.place(x = 0,y = 0)

        label7 = ctk.CTkLabel(f4,text = "DemEven",fg_color = "white",text_color = "black",font = ctk.CTkFont(size = 25,weight = "bold"))
        label7.place(x = 20,y = 80)

        label8 = ctk.CTkLabel(f4,text = "Upcoming",fg_color = "#FEEEAB",text_color = "#EB9E29",corner_radius = 3,height = 10,width = 10,padx = 2,pady = 2)
        label8.place(x = 20,y = 140)

        img8 = ctk.CTkImage(dark_image = Image.open(r"pics\calendar.png"),size = (20,20))
        labimg8 = ctk.CTkLabel(f4,image = img8,text = "")
        labimg8.place(x = 120,y = 137)

        label9 = ctk.CTkLabel(f4,text = "30/7/2024  6:00 pm - 10:00 pm  IST (61 days away)",text_color = "black",font = ctk.CTkFont(size = 13,weight = "normal"))
        label9.place(x = 150,y = 137)

        img9 = ctk.CTkImage(dark_image = Image.open(r"pics\location.png"),size = (20,20))
        labimg9 = ctk.CTkLabel(f4,image = img9,text = "")
        labimg9.place(x = 500,y = 137)

        label10 = ctk.CTkLabel(f4,text = "Chicago",text_color = "black",font = ctk.CTkFont(size = 13,weight = "normal"))
        label10.place(x = 522,y = 137)

        x9 =ctk.StringVar()
        x9.set("Actions")
        opt8 = ctk.CTkComboBox(f4,height = 35,width = 150,variable = x9,fg_color = "white",button_hover_color = "#4B9EFC",border_width = 1,border_color = "lightgray",corner_radius = 7,dropdown_hover_color = "#4B9EFC",button_color = "lightgray",text_color = "#0966F1",values = ["","","",""])
        opt8.place(x = 800,y = 96)

        img10 = ctk.CTkImage(dark_image = Image.open(r"pics\light-bulb.png"),size = (50,50))
        labimg10 = ctk.CTkLabel(self.f0,image = img10,text = "")
        labimg10.place(x = 8,y = 205)

        label11 = ctk.CTkLabel(self.f0,text = "Up next for your event",text_color = "black",font = ctk.CTkFont(size = 18,weight = "bold"))
        label11.place(x = 50,y = 215)

        f5 = ctk.CTkFrame(f01,height = 150,width = 265,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
        f5.place(x = 8,y = 255)

        img11 = ctk.CTkImage(dark_image = Image.open(r"pics\features.png"),size = (38,38))
        labimg11 = ctk.CTkLabel(f5,image = img11,text = "")
        labimg11.place(x = 15,y = 48)

        label12 = ctk.CTkLabel(f5,text = "Add Event Features",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
        label12.place(x = 75,y = 20)

        label13 = ctk.CTkLabel(f5,text = "Make sure you have all the\nfeatures you need for your event",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
        label13.place(x = 75,y = 55)

        def funbut1():
            pass

        button1 = ctk.CTkButton(f5,text = "Add features",corner_radius = 5,border_width = 1,width = 6,hover_color = "lightgray",border_color = "#3fa6fb",fg_color = "#ffffff",border_spacing = 3,text_color = "#3fa6fb",command = funbut1)
        button1.place(x = 75,y = 100)

        def skip1():
            pass

        button2 = ctk.CTkButton(f5,text = "Skip",width = 6,fg_color = "#ffffff",text_color = "#3fa6fb",hover_color = "#ffffff",command = skip1)
        button2.place(x = 185,y = 100)

        f6 = ctk.CTkFrame(f01,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
        f6.place(x = 290,y = 255)

        img12 = ctk.CTkImage(dark_image = Image.open(r"pics\registration.png"),size = (42,38))
        labimg12 = ctk.CTkLabel(f6,image = img12,text = "")
        labimg12.place(x = 15,y = 48)

        label14 = ctk.CTkLabel(f6,text = "Set up registration types",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
        label14.place(x = 45,y = 20)

        label15 = ctk.CTkLabel(f6,text = "Add registration types to\ncustomize the registration...",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
        label15.place(x = 75,y = 55)

        def funbut2():
            pass

        button3 = ctk.CTkButton(f6,text = "Get Started",corner_radius = 5,border_width = 1,width = 6,hover_color = "lightgray",border_color = "#3fa6fb",fg_color = "#ffffff",border_spacing = 3,text_color = "#3fa6fb",command = funbut2)
        button3.place(x = 75,y = 100)

        def skip2():
            pass

        button4 = ctk.CTkButton(f6,text = "Skip",width = 6,fg_color = "#ffffff",text_color = "#3fa6fb",hover_color = "#ffffff",command = skip2)
        button4.place(x = 185,y = 100)

        label16 = ctk.CTkLabel(f01,text = "Event Overview",text_color = "black",font = ctk.CTkFont(size = 18,weight = "bold"))
        label16.place(x = 8,y = 420)

        f7 = ctk.CTkFrame(f01,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
        f7.place(x = 8,y = 460)

        label17 = ctk.CTkLabel(f7,text = "Registration",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
        label17.place(x = 20,y = 20)

        label18 = ctk.CTkLabel(f7,text = "Invitee Conversion Rate",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
        label18.place(x = 20,y = 50)

        label19 =  ctk.CTkLabel(f7,text = "0.0%",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
        label19.place(x = 20,y = 75)

        img13 = ctk.CTkImage(dark_image = Image.open(r"pics\light-bulb.png"),size = (30,30))
        labimg13 = ctk.CTkLabel(f7,image = img13,text = "")
        labimg13.place(x = 15,y = 105)

        label20 = ctk.CTkLabel(f7,text = "Set your event's deadline\nand capacity",text_color = "#3fa6fb",font = ctk.CTkFont(size = 12,weight = "normal"))
        label20.place(x = 60,y = 105)

        def butimg14():
            pass 

        img14 = ctk.CTkImage(dark_image = Image.open(r"pics\ellipsis.png"),size = (30,20))
        butimg14 = ctk.CTkButton(f7,image = img14,text = "",command = butimg14,width = 20,fg_color = "#ffffff",hover_color = "#ffffff")
        butimg14.place(x = 220,y = 20)

        f8 = ctk.CTkFrame(f01,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
        f8.place(x = 290,y = 460)

        label21 = ctk.CTkLabel(f8,text = "Emails",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
        label21.place(x = 20,y = 20)

        label22 = ctk.CTkLabel(f8,text = "Email sent",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
        label22.place(x = 20,y = 50)

        label23 =  ctk.CTkLabel(f8,text = "0",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
        label23.place(x = 20,y = 75)

        labimg15 = ctk.CTkLabel(f8,image = img13,text = "")
        labimg15.place(x = 15,y = 105)

        label24 = ctk.CTkLabel(f8,text = "Add any custom data tags you\nneed for your event",text_color = "#3fa6fb",font = ctk.CTkFont(size = 12,weight = "normal"))
        label24.place(x = 60,y = 105)
        
        def butimg15():
            pass

        img15 = ctk.CTkImage(dark_image = Image.open(r"pics\ellipsis.png"),size = (30,20))
        butimg15 = ctk.CTkButton(f8,image = img15,text = "",command = butimg15,width = 20,fg_color = "#ffffff",hover_color = "#ffffff")
        butimg15.place(x = 220,y = 20)
        
        f02 = ctk.CTkFrame(self.f0,height = 730,width = 290,fg_color = "gainsboro",corner_radius=12)
        f02.grid(row=0,column=1, padx=(12,0), sticky="n")

        def butimg16():
            pass 

        img16 = ctk.CTkImage(dark_image = Image.open(r"pics\right-arrow.png"),size = (30,30))
        butimg16 = ctk.CTkButton(f02,image = img16,text = "",command = butimg16,fg_color = "#C8C6F3",hover_color = "#ffffff",width = 20)
        butimg16.place(x = 400,y = 0)

        label25 = ctk.CTkLabel(f02,text = "Feature Status",text_color = "black",font = ctk.CTkFont(size = 17,weight = "bold"), corner_radius = 9, fg_color="#F0F0F0")
        label25.place(x = 15,y = 30)

        img17 = ctk.CTkImage(dark_image = Image.open(r"pics\pending.png"),size = (20,20))
        labimg17 = ctk.CTkLabel(f02,image = img17,text = "")
        labimg17.place(x = 165,y = 30)

        label26 = ctk.CTkLabel(f02,text = "Registration",text_color = "black", font = ctk.CTkFont(size = 19,weight = "normal"))
        label26.place(x = 19,y = 60)

        label27 = ctk.CTkLabel(f02,text = "Pending",text_color = "black",corner_radius = 19,height = 10,width = 10,padx = 2,pady = 2,font = ctk.CTkFont(size = 19))
        label27.place(x = 350,y = 80)

        label28 = ctk.CTkLabel(f02,text = "Search for attendees",text_color = "black",fg_color = "#F0F0F0",font = ctk.CTkFont(size = 17,weight = "bold"), corner_radius = 9, width=262)
        label28.place(x = 15,y = 110)

        x10 = tk.StringVar()
        e2 = ctk.CTkEntry(f02,height = 30,width = 257,corner_radius = 15,fg_color = "#ffffff",text_color = "black",placeholder_text = "Enter a name or email",placeholder_text_color = "black",textvariable = x10)
        e2.place(x = 18,y = 150)

        canvas3 =  tk.Canvas(f02,height = 3,width = 262,bg = "gray",relief = tk.RAISED)
        canvas3.place(x = 15,y = 215)

        def butimg18():
            pass 

        img18 = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (10,10))
        butimg18 = ctk.CTkButton(e2,image = img7,text = "",fg_color = "white",hover_color = "#ffffff",corner_radius = 3,height = 10,width = 10,command = butimg18)
        butimg18.place(x = 218,y = 3)

        label29 = ctk.CTkLabel(f02,text = "Event Information",text_color = "black",fg_color = "#F0F0F0",font = ctk.CTkFont(size = 17,weight = "bold"), corner_radius = 9, width=262)
        label29.place(x = 15,y = 260)

        label30 = ctk.CTkLabel(f02,text = "Event Code",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
        label30.place(x = 15,y = 310)

        x11 = tk.StringVar()
        x11.set("BAMMCYD")
        label31 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x11,font = ctk.CTkFont(size = 12,weight = "bold"))
        label31.place(x = 22,y = 340)

        label32 = ctk.CTkLabel(f02,text = "Event Format",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
        label32.place(x = 15,y = 380)

        x12 = tk.StringVar()
        x12.set("Hybrid")
        label33 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x12,font = ctk.CTkFont(size = 12,weight = "bold"))
        label33.place(x = 22,y = 410)

        label34 = ctk.CTkLabel(f02,text = "Registration Capacity",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
        label34.place(x = 15,y = 450)

        x13 = tk.StringVar()
        x13.set("In Person:Unlimited | Virtual:Unlimited")
        label35 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x13,font = ctk.CTkFont(size = 12,weight = "bold"))
        label35.place(x = 22,y = 480)

        label36 = ctk.CTkLabel(f02,text = "Registration Deadline",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
        label36.place(x = 15,y = 520)

        x14 = tk.StringVar()
        x14.set("30/7/2024 9:59 pm IST")
        label37 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x14,font = ctk.CTkFont(size = 12,weight = "bold"))
        label37.place(x = 22,y = 550)

        label38 = ctk.CTkLabel(f02,text = "Planner",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
        label38.place(x = 15,y = 590)

        x15 = tk.StringVar()
        x15.set("Lucky Tungariya")
        label39 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x15,font = ctk.CTkFont(size = 12,weight = "bold"))
        label39.place(x = 22,y = 620)

        label40 = ctk.CTkLabel(f02,text = "Planner's Email",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
        label40.place(x = 15,y = 660)

        x16 = tk.StringVar()
        x16.set("send@gmail.com")
        label41 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x16,font = ctk.CTkFont(size = 12,weight = "bold"))
        label41.place(x = 22,y = 690)

    def reporttab_widgets(self):
        pass
    def tickettab_widgets(self):
        pass
    def surveytab_widgets(self):
        pass

if __name__ == "__main__" : 
    app = DemoApplication()
    app.mainloop()