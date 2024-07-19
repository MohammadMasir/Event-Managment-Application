import customtkinter as ctk
from PIL import Image
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning, showerror
from .eventcreate import CreateEvent

class EventView():
    def __init__(self, main):
        self.main = main

        self.primary_color = "#093838"
        self.secondary_color = "#8bceba"
        self.bg = "gainsboro"
        self.text_color = "#092928"
        self.hovercolor_bg = "#20807f"
        self.hovercolor_txt = "white"

    def create_widgets(self):
        self.main.switch_screen(self._create_widgets)

    def _create_widgets(self):
        self.main.toggle_fullscreen()
        self.main.resizable(width=True, height=True)
        self.main.bind("<F11>", self.main.toggle_fullscreen)

        frame2 = ctk.CTkFrame(self.main, height=30, fg_color="#4bceba")
        frame2.pack(fill="x")

        primary_color_frame = ctk.CTkFrame(frame2, height=45,fg_color=self.hovercolor_bg,corner_radius=0)
        primary_color_frame.place(x=0,y=-3,relwidth=1)

        corner_colors = ("#20807f", "#20807f", "#4bceba", "#4bceba")
    
        labe = ctk.CTkButton(frame2, text="Event Manager", font=("Segoe UI", 40, "bold"), text_color="white",fg_color=self.secondary_color, width=100, height=35,corner_radius=100,background_corner_colors=corner_colors,hover=False)
        labe.pack(pady=10, expand=True)

        # Create a self.notebook (tabbed interface)
        self.notebook = ctk.CTkTabview(self.main, bg_color = self.hovercolor_bg, corner_radius=12) #3fa572 #333333
        self.notebook.pack(pady=(10,0), fill="both", expand=True)

        # # Dashboard Tab
        # self.dashboard_tab = self.notebook.add("Dashboard")
        # self.dashboard_widgets()

        # Event Management Tab
        self.event_tab = self.notebook.add("Event Management")
        self.notebook.set("Event Management")
        self.eventtab_widgets()

    def eventtab_widgets(self,event_name=None):
        # self.events = DashboardPage(self, self.event_tab)
        self.previewmain_frame = ctk.CTkFrame(self.event_tab, fg_color = "#F0F0F0")
        self.previewmain_frame.pack(side="top", fill="both", expand= True)

        self.main.topbar(self.previewmain_frame)
        
        self.canvas1 = tk.Canvas(self.previewmain_frame,height = 3,width = 1920,bg = "#0061ff",relief = tk.RAISED)
        self.canvas1.pack(side="top")

        top_bar2 = ctk.CTkFrame(self.previewmain_frame, fg_color="white")
        top_bar2.pack(side="top", fill="x", ipady=30)

        self.label15 = ctk.CTkLabel(top_bar2,text = "Events",text_color = "#000000",font = ctk.CTkFont(size = 20,weight = "bold"))
        self.label15.pack(side="left", padx=(20,0))

        self.event_form = CreateEvent(self.event_tab, self.main)

        self.create_event_button = ctk.CTkButton(top_bar2,text = "Create Event",height = 30,width = 40,fg_color = "#2380D2",text_color = "#ffffff",corner_radius = 7,command = lambda : self.event_form.create_event())
        self.create_event_button.pack(side="right", padx=(0,40))

        child_frame = ctk.CTkFrame(self.previewmain_frame,fg_color="white")
        child_frame.pack(side="top", fill="both", expand=True)

        inside_child = ctk.CTkFrame(child_frame, fg_color = "#E6E6E6", corner_radius=12)
        inside_child.pack(fill="x", anchor="center", ipady=40, padx=20)

        middle = ctk.CTkFrame(inside_child,fg_color = "#E6E6E6")
        middle.pack(side="top", anchor="center", ipady=40,fill="x")

        child_top = ctk.CTkFrame(middle, fg_color="transparent")
        child_top.pack(side="top", fill="x")

        x3 = tk.StringVar()
        x3.set("Current Events")
        current_events_opt = ctk.CTkComboBox(child_top,variable = x3,height = 35,width = 140,fg_color = "#E6E6E6",text_color = "black",button_color = "#E6E6E6",border_color = "#E6E6E6",button_hover_color = "#E6E6E6",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
        current_events_opt.pack(side="left")

        def create_view():
            pass

        create_view_button = ctk.CTkButton(child_top,text = "Create View",text_color = "#000000",hover_color = "#A4A4A4",width = 100,fg_color = "#E6E6E6",command = create_view)
        create_view_button.pack(side="left")

        advanced_search_label = ctk.CTkLabel(child_top,text = "Advanced Search",text_color = "#000000")
        advanced_search_label.pack(side="right",padx=(0,10))

        table_frame = ctk.CTkFrame(middle, fg_color="white")
        table_frame.pack(fill="x", padx=20,ipady=20)

        inner_frame1 = ctk.CTkFrame(table_frame,fg_color = "#ffffff",border_width = 0.8,border_color = "#919191")
        inner_frame1.pack(fill="x", padx=20,pady=(40,0))

        headline = ctk.CTkFrame(inner_frame1, fg_color="transparent",border_width = 0.8,border_color = "#919191")
        headline.pack(side="top", fill="x", ipady=5)

        title_label = ctk.CTkLabel(headline,text = "Title",text_color = "#000000",font = ctk.CTkFont(size = 14,weight = "normal"))
        title_label.pack(side="left", padx=10)

        no_label = ctk.CTkLabel(headline,text = "No",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
        no_label.pack(side="right", padx=10)

        img6 = ctk.CTkImage(dark_image = Image.open(r"pics\question.png"),size = (20,20))
        labimg6 = ctk.CTkLabel(headline,image = img6,text = "")
        labimg6.pack(side="right")

        x7 = tk.StringVar()
        x7.set("Yes")
        yes_dropdown = ctk.CTkComboBox(headline,variable = x7,height = 35,width = 90,fg_color = "#ffffff",text_color = "#000000",button_color = "#ffffff",border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
        yes_dropdown.pack(side="right")

        x6 = tk.StringVar()
        x6.set("Start Date")
        start_date_dropdown = ctk.CTkComboBox(headline,variable = x6,height = 35,width = 140,fg_color = "#ffffff",text_color = "#000000",button_color = "#ffffff",border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
        start_date_dropdown.pack(side="right")

        x5 = tk.StringVar()
        x5.set("Event Status")
        event_status_dropdown = ctk.CTkComboBox(headline,variable = x5,height = 35,width = 140,fg_color = "#ffffff",text_color = "#000000",button_color = "#ffffff",border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
        event_status_dropdown.pack(side="right")

        x4 = tk.StringVar()
        x4.set("Code")
        code_dropdown = ctk.CTkComboBox(headline,variable = x4,height = 35,width = 100,fg_color = "#ffffff",text_color = "#000000",button_color = "#ffffff",border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
        code_dropdown.pack(side="right",padx=(0,20))

        # canvas2 = tk.Canvas(inner_frame1,height = 3,width = 1900,bg = "#858585",relief = tk.SUNKEN)
        # canvas2.pack()

        self.inner_frame2 = ctk.CTkFrame(inner_frame1,height = 68,width = 1172,fg_color = "#E6E6E6",corner_radius=0) #E6E6E6
        self.inner_frame2.pack(fill="both", padx=1, pady=(0,1))

        self.x8 = tk.StringVar()
        text = "There are no events in this view."
        if event_name==None:
            self.x8.set(text)
        else:
            self.x8.set(event_name)
        self.data_label = ctk.CTkLabel(self.inner_frame2,text_color = "#000000",textvariable = self.x8,font = ctk.CTkFont(size = 15,weight = "bold"))
        self.data_label.pack(side="top")

        result_per_page_label = ctk.CTkLabel(table_frame,text = "Results per page",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 13,weight = "normal"))
        result_per_page_label.pack(side="left", padx=(30,0))

        x9 = tk.IntVar()
        result_per_page_dropdown = ctk.CTkComboBox(table_frame,variable = x9,height = 35,width = 60,fg_color = "#ffffff",text_color = "#000000",border_width = 0.6,button_color = "#ffffff",corner_radius = 5,border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["25","30","35","40"])
        result_per_page_dropdown.pack(side="left")

        x10 = tk.StringVar()
        text = "Displaying result 0 of 0"
        x10.set(text)
        displaying_result_label = ctk.CTkLabel(table_frame,textvariable = x10,text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        displaying_result_label.pack(side="left", padx=(40,0))

        down_line = tk.Canvas(self.previewmain_frame,height = 9,width = 1920,bg = "#858585",relief = tk.SUNKEN)
        down_line.place(x = -2,y = 768)


    def update_table(self, event_name=None, code=None, event_status=None, start_date=None, yes_count=None, no_count=None, invited=None):
        self.data_label.pack_forget()
        # name = tk.StringVar()
        # text = event_name
        # name.set(text)
        event_labelbutton = ctk.CTkButton(self.inner_frame2,textvariable = event_name,text_color = "white",font = ctk.CTkFont(size = 15,weight = "normal"), command= self.events.events_home)
        event_labelbutton.pack(side="left")
        self.text_hover(event_labelbutton)