import customtkinter as ctk
import tkinter as tk
from PIL import Image
from view.commonpages import Page

class DashboardPage():
    def __init__(self, main_app, parent, event_name):
        super().__init__()
        self.main = main_app
        self.parent = parent
        self.event_name = event_name

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

    def events_home(self, event_category=None, address=None, start_date=None, end_date=None, start_time=None, end_time=None):

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
        self.homepage = Page(main_app=self.main, parent=self.home_main_frame, event_name=self.event_name, heading=self.event_name)
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
        self.infopage = Page(main_app=self.main, parent=self.info_frame, event_name=self.event_name, heading="Event Information")
        self.infopage.title_frame(False)
        self.infopage.content_frame()

        self.basic_info_frame = ctk.CTkFrame(self.infopage.scrollable_frame,fg_color = "#ffffff")
        self.basic_info_frame.pack(fill = "both",expand = True, padx=(10,90), pady=30)

        self.basic_info_label = ctk.CTkLabel(self.basic_info_frame,text = "Basic Information",text_color = "#000000",font = ctk.CTkFont("Segoe UI",21,"bold"))
        self.basic_info_label.pack(anchor = "nw",padx = 15,pady = 5)

        self.title_label = ctk.CTkLabel(self.basic_info_frame,text = "Title:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.title_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        title_variable = tk.StringVar()
        title_variable.set("lucky")
        self.title_value = ctk.CTkLabel(self.basic_info_frame,textvariable = title_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.title_value.pack(anchor = "nw",padx = 15,pady = 7)

        title_line = tk.Canvas(self.basic_info_frame,height = 1,width = 600,bg = "lightgray")
        title_line.pack(anchor = "nw",padx = 15,pady = 0)

        self.code_label = ctk.CTkLabel(self.basic_info_frame,text = "Code:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.code_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        code_variable = tk.StringVar()
        code_variable.set("NYNMK82YDWQ")
        self.code_value = ctk.CTkLabel(self.basic_info_frame,textvariable = code_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.code_value.pack(anchor = "nw",padx = 15,pady = 7)

        code_line = tk.Canvas(self.basic_info_frame,height = 1,width = 600,bg = "lightgray")
        code_line.pack(anchor = "nw",padx = 15,pady = 0)

        self.category_label =  ctk.CTkLabel(self.basic_info_frame,text = "Category:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.category_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        category_variable = tk.StringVar()
        category_variable.set("Seminar")
        self.category_value = ctk.CTkLabel(self.basic_info_frame,textvariable = category_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.category_value.pack(anchor = "nw",padx = 15,pady = 7)

        category_line = tk.Canvas(self.basic_info_frame,height = 1,width = 600,bg = "lightgray")
        category_line.pack(anchor = "nw",padx = 15,pady = 0)
        
        self.created_label = ctk.CTkLabel(self.basic_info_frame,text = "Created:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.created_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        created_variable = tk.StringVar()
        created_variable.set("31-5-2024 16:13 IST by send2atm@gmail.com")
        self.created_value = ctk.CTkLabel(self.basic_info_frame,textvariable = created_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.created_value.pack(anchor = "nw",padx = 15,pady = 7)

        line_under_created_value = tk.Canvas(self.basic_info_frame,height = 1,width = 600,bg = "lightgray")
        line_under_created_value.pack(anchor = "nw",padx = 15,pady = 0)

        self.language_label = ctk.CTkLabel(self.basic_info_frame,text = "Language:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.language_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        language_variable = tk.StringVar()
        language_variable.set("English")
        self.langauge_value =  ctk.CTkLabel(self.basic_info_frame,textvariable = language_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.langauge_value.pack(anchor = "nw",padx = 15,pady = 7)
        
        self.locale_label = ctk.CTkLabel(self.basic_info_frame,text = "Locale",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.locale_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        locale_variable = tk.StringVar()
        locale_variable.set("USA")
        self.locale_value = ctk.CTkLabel(self.basic_info_frame,textvariable = locale_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.locale_value.pack(anchor = "nw",padx = 15,pady = 7)

        locale_line = tk.Canvas(self.basic_info_frame,height = 1,width = 600,bg = "lightgray")
        locale_line.pack(anchor = "nw",padx = 15,pady = 0)

        self.multilanguage_event_label = ctk.CTkLabel(self.basic_info_frame,text = "Multi-Language Event:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.multilanguage_event_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        multilanguage_variable = tk.StringVar()
        multilanguage_variable.set("No")
        self.multilanguage_value = ctk.CTkLabel(self.basic_info_frame,textvariable = multilanguage_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.multilanguage_value.pack(anchor = "nw",padx = 15,pady = 7)

        multilanguage_line = tk.Canvas(self.basic_info_frame,height = 1,width = 600,bg = "lightgray")
        multilanguage_line.pack(anchor = "nw",padx = 15,pady = 0)

        self.description_label = ctk.CTkLabel(self.basic_info_frame,text = "Description:",text_color = "#000000",font = ctk.CTkFont("Segoe UI",15,"bold"))
        self.description_label.pack(anchor = "nw",padx = 15,pady = 10)

        self.internal_note_label = ctk.CTkLabel(self.basic_info_frame,text = "Internal Note:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.internal_note_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        internal_note_variable = tk.StringVar()
        internal_note_variable.set("--")
        self.internal_note_value = ctk.CTkLabel(self.basic_info_frame,textvariable = internal_note_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.internal_note_value.pack(anchor = "nw",padx = 15,pady = 7)

        internal_note_line = tk.Canvas(self.basic_info_frame,height = 1,width = 600,bg = "lightgray")
        internal_note_line.pack(anchor = "nw",padx = 15,pady = (0,9))

#---------------------------------------------------------------------------------------------------------------------

        self.event_information_content_frame = ctk.CTkFrame(self.infopage.scrollable_frame,fg_color = "#ffffff")
        self.event_information_content_frame.pack(fill = "both",expand = True, padx=(10,90), pady=20)

        self.when_label = ctk.CTkLabel(self.event_information_content_frame,text = "When",text_color = "#000000",font = ctk.CTkFont("Segoe UI",21,"bold"))
        self.when_label.pack(anchor = "nw",padx = 15,pady = 5)

        self.time_zone_label = ctk.CTkLabel(self.event_information_content_frame,text = "Time Zone",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.time_zone_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        time_zone_variable = tk.StringVar()
        time_zone_variable.set("(GMT+05:30) India")
        self.time_zone_value = ctk.CTkLabel(self.event_information_content_frame,textvariable = time_zone_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.time_zone_value.pack(anchor = "nw",padx = 15,pady = 7)

        line_under_time_zone = tk.Canvas(self.event_information_content_frame,height = 1,width = 600,bg = "lightgray")
        line_under_time_zone.pack(anchor = "nw",padx = 15,pady = 1)

        self.start_date_label = ctk.CTkLabel(self.event_information_content_frame,text = "Start Date:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.start_date_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        self.start_date_time_frame = ctk.CTkFrame(self.event_information_content_frame,fg_color = "#ffffff",height = 10,width = 400)
        self.start_date_time_frame.pack(anchor = "nw",padx = 15,pady = 10)

        start_date_variable = tk.StringVar()
        start_date_variable.set("30-7-2024")
        self.start_date_value = ctk.CTkLabel(self.start_date_time_frame,textvariable = start_date_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.start_date_value.pack(side = "left",padx = 0,pady = 10)

        start_time_variable = tk.StringVar()
        start_time_variable.set("18:00")
        self.start_time_value =  ctk.CTkLabel(self.start_date_time_frame,textvariable = start_time_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.start_time_value.pack(side = "right",padx = (150,150),pady = 0)
        
        self.start_line_frame = ctk.CTkFrame(self.event_information_content_frame,fg_color = "#ffffff",height = 2,width = 400)
        self.start_line_frame.pack(anchor = "nw",padx = 10,pady = 0)

        line_under_start_date = tk.Canvas(self.start_line_frame,height = 1,width = 300,bg = "lightgray")
        line_under_start_date.pack(side = "left",padx = 0,pady = 0)

        line_right_of_start_date = tk.Canvas(self.start_line_frame,height = 1,width = 300,bg = "lightgray")
        line_right_of_start_date.pack(side = "right",padx = 30,pady = 0)

        self.end_dt_label = ctk.CTkLabel(self.event_information_content_frame,text = "End Date:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.end_dt_label.pack(anchor = "nw",padx = 15,pady = 10)

        self.end_date_time_frame = ctk.CTkFrame(self.event_information_content_frame,fg_color = "#ffffff",height = 10,width = 400)
        self.end_date_time_frame.pack(anchor = "nw",padx = 15,pady = 10)
        
        end_date_variable = tk.StringVar()
        end_date_variable.set("30-7-2024")
        self.end_date_value = ctk.CTkLabel(self.end_date_time_frame,textvariable = end_date_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.end_date_value.pack(side = "left",padx = 0,pady = 0)
        
        end_time_variable = tk.StringVar()
        end_time_variable.set("22:00")
        self.end_time_value = ctk.CTkLabel(self.end_date_time_frame,textvariable = end_time_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.end_time_value.pack(side = "right",padx = (150,150),pady = 0)

        self.end_line_frame = ctk.CTkFrame(self.event_information_content_frame,fg_color = "#ffffff",height = 2,width = 400)
        self.end_line_frame.pack(anchor = "nw",padx = 5,pady = 0)

        line_under_end_date = tk.Canvas(self.end_line_frame,height = 1,width = 300,bg = "lightgray")
        line_under_end_date.pack(side = "left",padx = 0,pady = 0)

        line_right_of_end_date =  tk.Canvas(self.end_line_frame,height = 1,width = 300,bg = "lightgray")
        line_right_of_end_date.pack(side = "right",padx = 30,pady = 0)

        self.archive_date_label = ctk.CTkLabel(self.event_information_content_frame,text = "Archive Date:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.archive_date_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        archive_date_variable = tk.StringVar()
        archive_date_variable.set("28-10-2024")
        self.archive_date_value = ctk.CTkLabel(self.event_information_content_frame,textvariable = archive_date_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.archive_date_value.pack(anchor = "nw",padx = 15,pady = 7)

        line_under_archive = tk.Canvas(self.event_information_content_frame,height = 1,width = 600,bg = "lightgray")
        line_under_archive.pack(anchor = "nw",padx = 15,pady = (0,9))

#------------------------------------------------------------------------------------------------------------------
        self.event_format_frame = ctk.CTkFrame(self.infopage.scrollable_frame,fg_color = "#ffffff")
        self.event_format_frame.pack(fill = "both",expand = True, padx=(10,90), pady=20)

        self.event_format_label = ctk.CTkLabel(self.event_format_frame,text = "Event Format",text_color = "#000000",font = ctk.CTkFont("Segoe UI",21,"bold"))
        self.event_format_label.pack(anchor = "nw",padx = 15,pady = 5)

        self.question_label = ctk.CTkLabel(self.event_format_frame,text = "What's your event format?",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.question_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        question_variable = tk.StringVar()
        question_variable.set("Hybrid (people can attend in person or virtually)")
        self.question_value = ctk.CTkLabel(self.event_format_frame,textvariable = question_variable,text_color = "#000000",font =  ctk.CTkFont(size=15,weight="bold"))
        self.question_value.pack(anchor = "nw",padx = 15,pady = 7)

        question_line = tk.Canvas(self.event_format_frame,height = 1,width = 600,bg = "lightgray")
        question_line.pack(anchor = "nw",padx = 15,pady = (0,9))
      
#------------------------------------------------------------------------------------------------------------------
        self.location_frame = ctk.CTkFrame(self.infopage.scrollable_frame,fg_color = "#ffffff")
        self.location_frame.pack(fill = "both",expand = True, padx=(10,90), pady=20)

        self.location_label = ctk.CTkLabel(self.location_frame,text = "Location",text_color = "#000000",font = ctk.CTkFont("Segoe UI",21,"bold"))
        self.location_label.pack(anchor = "nw",padx = 15,pady = 5)

        self.venue_label = ctk.CTkLabel(self.location_frame,text = "Venue:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.venue_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        venue_variable = tk.StringVar()
        venue_variable.set("Custom Location")
        self.venue_value = ctk.CTkLabel(self.location_frame,textvariable = venue_variable,text_color = "#000000",font =  ctk.CTkFont(size=15,weight="bold"))
        self.venue_value.pack(anchor = "nw",padx = 15,pady = 7)

        venue_line = tk.Canvas(self.location_frame,height = 1,width = 600,bg = "lightgray")
        venue_line.pack(anchor = "nw",padx = 15,pady = (0,9))

#------------------------------------------------------------------------------------------------------------------
        self.where_frame = ctk.CTkFrame(self.infopage.scrollable_frame,fg_color = "#ffffff")
        self.where_frame.pack(fill = "both",expand = True, padx=(10,90), pady=20)

        self.where_label = ctk.CTkLabel(self.where_frame,text = "Where",text_color = "#000000",font = ctk.CTkFont("Segoe UI",21,"bold"))
        self.where_label.pack(anchor = "nw",padx = 15,pady = 5)

        self.venue_label = ctk.CTkLabel(self.where_frame,text = "Venue:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.venue_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        where_variable = tk.StringVar()
        where_variable.set("Taj Hotel")
        self.where_value =  ctk.CTkLabel(self.where_frame,textvariable = where_variable,text_color = "#000000",font =  ctk.CTkFont(size=15,weight="bold"))
        self.where_value.pack(anchor = "nw",padx = 15,pady = 7)

        where_line = tk.Canvas(self.where_frame,height = 1,width = 600,bg = "lightgray")
        where_line.pack(anchor = "nw",padx = 15,pady = (0,9))

        self.phone_label = ctk.CTkLabel(self.where_frame,text = "Phone:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.phone_label.pack(anchor = "nw",padx = 15,pady = 5)
        
        phone_variable = tk.StringVar()
        phone_variable.set("9820568660")
        self.phone_value = ctk.CTkLabel(self.where_frame,textvariable = phone_variable,text_color = "#000000",font =  ctk.CTkFont(size=15,weight="bold"))
        self.phone_value.pack(anchor = "nw",padx = 15,pady = 7)

        phone_line =  tk.Canvas(self.where_frame,height = 1,width = 600,bg = "lightgray")
        phone_line.pack(anchor = "nw",padx = 15,pady = (0,9))

        self.address_label = ctk.CTkLabel(self.where_frame,text = "Address:",text_color = "#000000",font = ctk.CTkFont("Segoe UI",21,"bold"))
        self.address_label.pack(anchor = "nw",padx = 15,pady = 10)

        self.city_frame = ctk.CTkFrame(self.where_frame,fg_color = "#ffffff",height = 200,width = 250)
        self.city_frame.pack(side = "left",padx = 15,pady = 20)

        self.state_frame = ctk.CTkFrame(self.where_frame,fg_color = "#ffffff",height = 200,width = 250)
        self.state_frame.pack(side = "right",padx = (0,400),pady = 20)

        self.city_label = ctk.CTkLabel(self.city_frame,text = "City:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.city_label.pack(anchor = "nw",padx = 0,pady = 0)
        
        city_variable = tk.StringVar()
        city_variable.set("Mumbai")
        self.city_value = ctk.CTkLabel(self.city_frame,textvariable = city_variable,text_color = "#000000",font =  ctk.CTkFont(size=15,weight="bold"))
        self.city_value.pack(anchor = "nw",padx = 0,pady = 5)

        city_line = tk.Canvas(self.city_frame,height = 1,width = 300,bg = "lightgray")
        city_line.pack(anchor = "nw",padx = 0)

        self.postal_code_label = ctk.CTkLabel(self.city_frame,text = "ZIP/Postal Code:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.postal_code_label.pack(anchor = "nw",padx = 0,pady = 5)
        
        postal_variable = tk.StringVar()
        postal_variable.set("400071")
        self.postal_code_value = ctk.CTkLabel(self.city_frame,textvariable = postal_variable,text_color = "#000000",font =  ctk.CTkFont(size=15,weight="bold"))
        self.postal_code_value.pack(anchor = "nw",padx = 0,pady = 5)

        postal_line = tk.Canvas(self.city_frame,height = 1,width = 300,bg = "lightgray")
        postal_line.pack(anchor = "nw",padx = 0)

        self.state_label = ctk.CTkLabel(self.state_frame,text = "State/Provine:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.state_label.pack(anchor = "nw",padx = 0,pady = 0)
        
        state_variable = tk.StringVar()
        state_variable.set("Maharashtra")
        self.state_value = ctk.CTkLabel(self.state_frame,textvariable = state_variable,text_color = "#000000",font =  ctk.CTkFont(size=15,weight="bold"))
        self.state_value.pack(anchor = "nw",padx = 0,pady = 5)

        state_line = tk.Canvas(self.state_frame,height = 1,width = 300,bg = "lightgray")
        state_line.pack(anchor = "nw",padx = 0,pady = 0)

        self.country_label = ctk.CTkLabel(self.state_frame,text = "State/Provine:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.country_label.pack(anchor = "nw",padx = 0,pady = 5)
        
        country_variable = tk.StringVar()
        country_variable.set("India")
        self.country_value = ctk.CTkLabel(self.state_frame,textvariable = country_variable,text_color = "#000000",font =  ctk.CTkFont(size=15,weight="bold"))
        self.country_value.pack(anchor = "nw",padx = 0,pady = 5)

        country_line = tk.Canvas(self.state_frame,height = 1,width = 300,bg = "lightgray")
        country_line.pack(anchor = "nw",padx = 0,pady = 0)    
#------------------------------------------------------------------------------------------------------------------
        self.event_planner_frame = ctk.CTkFrame(self.infopage.scrollable_frame,fg_color = "#ffffff")
        self.event_planner_frame.pack(fill = "both",expand = True, padx=(10,90), pady=20)

        self.event_planner_label = ctk.CTkLabel(self.event_planner_frame,text = "Event Planner",text_color = "#000000",font = ctk.CTkFont("Segoe UI",21,"bold"))
        self.event_planner_label.pack(anchor = "nw",padx = 15,pady = 5)

        self.name_label = ctk.CTkLabel(self.event_planner_frame,text = "Name:",text_color = "#000000",font = ctk.CTkFont(size=19,weight="bold"))
        self.name_label.pack(anchor = "nw",padx = 15,pady = 10)

        self.first_last_name_frame = ctk.CTkFrame(self.event_planner_frame,fg_color = "#ffffff",height = 5)
        self.first_last_name_frame.pack(anchor = "nw",fill = "x",padx = 15,pady = 5)

        self.first_name_label = ctk.CTkLabel(self.first_last_name_frame,text = "First",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.first_name_label.pack(side = "left",padx = 0,pady = 0)

        self.last_name_label = ctk.CTkLabel(self.first_last_name_frame,text = "Last",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.last_name_label.pack(side = "right",padx = 350,pady = 0)
        
        self.first_last_name_value_frame = ctk.CTkFrame(self.event_planner_frame,fg_color = "#ffffff",height = 5)
        self.first_last_name_value_frame.pack(anchor = "nw",fill = "x",padx = 15,pady = 5)

        first_name_variable = tk.StringVar()
        first_name_variable.set("Lucky")
        self.first_name_value = ctk.CTkLabel(self.first_last_name_value_frame,textvariable = first_name_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.first_name_value.pack(side = "left",padx = 0,pady = 0)

        last_name_variable = tk.StringVar()
        last_name_variable.set("Tungariya")
        self.last_name_value = ctk.CTkLabel(self.first_last_name_value_frame,textvariable = last_name_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.last_name_value.pack(side = "right",padx = 320,pady = 0)

        self.separate_line_frame = ctk.CTkFrame(self.event_planner_frame,fg_color = "#ffffff",height = 3)
        self.separate_line_frame.pack(anchor = "nw",fill = "x",padx = 15,pady = 5)

        first_name_line = tk.Canvas(self.separate_line_frame,height = 1,width = 300,bg = "lightgray")
        first_name_line.pack(side = "left",padx = 0,pady = (0,9))

        last_name_line = tk.Canvas(self.separate_line_frame,height = 1,width = 300,bg = "lightgray")
        last_name_line.pack(side = "right",padx = 300,pady = (0,9))

        self.company_label = ctk.CTkLabel(self.event_planner_frame,text = "Company:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.company_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        company_variable = tk.StringVar()
        company_variable.set("--")
        self.company_value = ctk.CTkLabel(self.event_planner_frame,textvariable = company_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.company_value.pack(anchor = "nw",padx = 15,pady = 7)

        company_line = tk.Canvas(self.event_planner_frame,height = 1,width = 600,bg = "lightgray")
        company_line.pack(anchor = "nw",padx = 15,pady = (0,9))

        self.title_label = ctk.CTkLabel(self.event_planner_frame,text = "Title:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.title_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        title_variable = tk.StringVar()
        title_variable.set("--")
        self.title_value = ctk.CTkLabel(self.event_planner_frame,textvariable = title_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.title_value.pack(anchor = "nw",padx = 15,pady = 7)

        title_line = tk.Canvas(self.event_planner_frame,height = 1,width = 600,bg = "lightgray")
        title_line.pack(anchor = "nw",padx = 15,pady = (0,9))

        self.email_label = ctk.CTkLabel(self.event_planner_frame,text = "Email:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.email_label.pack(anchor = "nw",padx = 15,pady = 10)
        
        email_variable = tk.StringVar()
        email_variable.set("send2atm@gmail.com")
        self.email_value = ctk.CTkLabel(self.event_planner_frame,textvariable = email_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.email_value.pack(anchor = "nw",padx = 15,pady = 7)

        email_line = tk.Canvas(self.event_planner_frame,height = 1,width = 600,bg = "lightgray")
        email_line.pack(anchor = "nw",padx = 15,pady = (0,9))

#------------------------------------------------------------------------------------------------------------------
    def event_features(self):
        self.set_screen()
        self.feature_frame = ctk.CTkFrame(self.parent)
        self.feature_frame.pack(fill="both", expand=True)
        self.featurepage = Page(main_app=self.main, parent=self.feature_frame, event_name=self.event_name, heading="Event Features")
        self.featurepage.title_frame(False)
        self.featurepage.content_frame()

#------------------------------------------------------------------------------------------------------------------

    def event_settings(self):
        self.set_screen()
        self.settings_frame = ctk.CTkFrame(self.parent)
        self.settings_frame.pack(fill="both", expand=True)
        self.settingpage = Page(main_app=self.main, parent=self.settings_frame, event_name=self.event_name, heading="Event Settings")
        self.settingpage.title_frame(False)
        self.settingpage.content_frame()

        self.event_settings_content_frame = ctk.CTkFrame(self.settingpage.scrollable_frame,fg_color = "#ffffff")
        self.event_settings_content_frame.pack(fill = "both",expand = True, padx=(10,90),pady=20)

        self.video_label =  ctk.CTkLabel(self.event_settings_content_frame,text = "Video Conferencing Platform",text_color = "#000000",font = ctk.CTkFont("Segoe UI",21,"bold"))
        self.video_label.pack(anchor = "nw",padx = 15,pady = 10)

        self.choose_video_label = ctk.CTkLabel(self.event_settings_content_frame,text = "Choose the video conferencing platform you're using for your event.",text_color = "#000000",font = ctk.CTkFont(size=19,weight="bold"))
        self.choose_video_label.pack(anchor = "nw",padx = 15,pady = 10)

        self.platform_name = ctk.CTkLabel(self.event_settings_content_frame,text = "Platform name:",text_color = "#000000",font = ctk.CTkFont(size=20,weight="normal"))
        self.platform_name.pack(anchor = "nw",padx = 15,pady = 5)
        
        platform_variable = tk.StringVar()
        platform_variable.set("None")
        self.platform_value = ctk.CTkLabel(self.event_settings_content_frame,textvariable = platform_variable,text_color = "#000000",font = ctk.CTkFont(size=15,weight="bold"))
        self.platform_value.pack(anchor = "nw",padx = 15,pady = 5)

        platform_line = tk.Canvas(self.event_settings_content_frame,height = 1,width = 600,bg = "lightgray")
        platform_line.pack(anchor = "nw",padx = 15,pady = (0,12))

    def edit_pricing_command(self):
        pass  