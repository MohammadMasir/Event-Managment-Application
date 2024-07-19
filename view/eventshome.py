import customtkinter as ctk
import tkinter as tk
from PIL import Image
from commonpages import Page

class DashboardPage():
    def __init__(self, main_app):
        super().__init__()
        self.main = main_app
        self.parent = self.main.event_tab

        self.primary_color = "#093838"
        self.secondary_color = "#8bceba"
        self.bg = "gainsboro"
        self.text_color = "#092928"
        self.hovercolor_bg = "#20807f"
        self.hovercolor_txt = "white"

    def set_screen(self):
        self.main.notebook.set("Event Management")
        for widget in self.parent.winfo_children():
            widget.pack_forget()

    def events_home(self, event_name=None, event_category=None, address=None, start_date=None, end_date=None, start_time=None, end_time=None):
        self.event_name = event_name
        self.event_category = event_category
        self.event_address = address
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time

        self.set_screen()
        self.home_main_frame = ctk.CTkFrame(self.main.event_tab, corner_radius=0, fg_color = "#F0F0F0")
        self.home_main_frame.pack(fill="both", expand="true")
        self.main.topbar(self.home_main_frame)
        self.homepage = Page(main_app=self.main, parent=self.home_main_frame, heading=self.event_name)
        self.homepage.title_frame(False)
        self.homepage.content_frame()

        label8 = ctk.CTkLabel(self.homepage.upper_frame,text = "Upcoming",fg_color = "#FEEEAB",text_color = "#EB9E29",corner_radius = 3,height = 10,width = 10,padx = 2,pady = 2)
        label8.pack(side="left", padx=30)

        img8 = ctk.CTkImage(dark_image = Image.open(r"pics\calendar.png"),size = (20,20))
        labimg8 = ctk.CTkLabel(self.homepage.upper_frame,image = img8,text = "")
        labimg8.pack(side="left")

        label9 = ctk.CTkLabel(self.homepage.upper_frame,text = f" {self.start_date} {self.start_time} pm - {self.end_time} pm  IST (61 days away)",text_color = "black",font = ctk.CTkFont(size = 13,weight = "normal"))
        label9.pack(side="left")

        img9 = ctk.CTkImage(dark_image = Image.open(r"pics\location.png"),size = (20,20))
        labimg9 = ctk.CTkLabel(self.homepage.upper_frame,image = img9,text = "")
        labimg9.pack(side="left", padx=(30,0))

        label10 = ctk.CTkLabel(self.homepage.upper_frame,text = "Chicago",text_color = "black",font = ctk.CTkFont(size = 13,weight = "normal"))
        label10.pack(side="left")

        x9 =ctk.StringVar()
        x9.set("Actions")
        opt8 = ctk.CTkComboBox(self.homepage.upper_frame,height = 35,width = 150,variable = x9,fg_color = "white",button_hover_color = "#4B9EFC",border_width = 1,border_color = "lightgray",corner_radius = 7,dropdown_hover_color = "#4B9EFC",button_color = "lightgray",text_color = "#0966F1",values = ["","","",""])
        opt8.pack(side="right", padx=(0,30),pady=(0,50))

        img10 = ctk.CTkImage(dark_image = Image.open(r"pics\light-bulb.png"),size = (50,50))
        labimg10 = ctk.CTkLabel(self.homepage.scrollable_frame,image = img10,text = "")
        labimg10.place(x = 8,y = 205)

        label11 = ctk.CTkLabel(self.homepage.scrollable_frame,text = "Up next for your event",text_color = "black",font = ctk.CTkFont(size = 18,weight = "bold"))
        label11.place(x = 50,y = 215)

        f5 = ctk.CTkFrame(self.homepage.scrollable_frame,height = 150,width = 265,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
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

        f6 = ctk.CTkFrame(self.homepage.scrollable_frame,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
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

        label16 = ctk.CTkLabel(self.homepage.scrollable_frame,text = "Event Overview",text_color = "black",font = ctk.CTkFont(size = 18,weight = "bold"))
        label16.place(x = 8,y = 420)

        f7 = ctk.CTkFrame(self.homepage.scrollable_frame,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
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

        f8 = ctk.CTkFrame(self.homepage.scrollable_frame,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
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
        
        f02 = ctk.CTkFrame(self.homepage.scrollable_frame,height = 730,width = 290,fg_color = "gainsboro",corner_radius=12)
        f02.pack(side="right")

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
        e2 = ctk.CTkEntry(f02,height = 35,width = 257,corner_radius = 15,fg_color = "#ffffff",text_color = "black",placeholder_text = "Enter a name or email",placeholder_text_color = "black",textvariable = x10)
        e2.place(x = 18,y = 150)

        canvas3 =  tk.Canvas(f02,height = 3,width = 262,bg = "gray",relief = tk.RAISED)
        canvas3.place(x = 15,y = 215)

        def butimg18():
            pass 

        img18 = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (20,20))
        butimg18 = ctk.CTkButton(e2,image = img18,text = "",fg_color = "white",hover_color = "#ffffff",corner_radius = 3,height = 10,width = 10,command = butimg18)
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

    def event_information(self):
        self.set_screen()
        self.info_frame = ctk.CTkFrame(self.parent)
        self.info_frame.pack(fill="both", expand=True)
        self.infopage = Page(main_app=self.main, parent=self.info_frame, heading="Event Information")
        self.infopage.title_frame(False)
        self.infopage.content_frame()

    def event_features(self):
        self.set_screen()
        self.feature_frame = ctk.CTkFrame(self.parent)
        self.feature_frame.pack(fill="both", expand=True)
        self.featurepage = Page(main_app=self.main, parent=self.feature_frame, heading="Event Features")
        self.featurepage.title_frame(False)
        self.featurepage.content_frame()

    def event_settings(self):
        self.set_screen()
        self.settings_frame = ctk.CTkFrame(self.parent)
        self.settings_frame.pack(fill="both", expand=True)
        self.settingpage = Page(main_app=self.main, parent=self.settings_frame, heading="Event Settings")
        self.settingpage.title_frame(False)
        self.settingpage.content_frame()
