import customtkinter as ctk
from PIL import Image
import pymysql as pq
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning, showerror
from eventshome import DashboardPage
from eventcreate import CreateEvent
from registration import RegistrationPage
# from commonpages import Page
# from hometemp import Test

            # INSPECTION BRANCH #
            
#COLORS :  #093838 -> Primary Color.    } In the Theme,
           #8bceba -> Secondary Color.  }  both the Primary & Secondary colors are used interchangeably.
           #gainsboro -> Background Color.
           #092928 -> Text Color.
           #20807f -> Hover Bg Color.
           #white -> Hover Text Color. 

class DemoApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.resizable(width=False, height=False)
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
        self.connection = self.connect_to_database()
        self.screen_stack = []
        self.current_screen = None

        self.sidebar = None
        self.states = False

        self.click_count = 0
        self.initial_screen()

    def connect_to_database(self):
        connection = pq.connect(
            host="localhost",
            user="root",
            password="root",
            database="projects",
            port=3306,
            charset="utf8"
        )
        return connection
    
    def add_hover_effect(self, widget):
        original_txtcolor = "#092928"
        original_bgcolor = widget.cget("fg_color")
        hovercolor_txt = "white"
        hovercolor_bg = "#20807f"
        def on_enter(e):
            widget.configure(fg_color=hovercolor_bg, text_color=hovercolor_txt)

        def on_leave(e):
            widget.configure(fg_color=original_bgcolor, text_color=original_txtcolor)

        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def back_preview(self, frame_name):
        if frame_name == self.previewmain_frame:
            return None
        else:
            for widgets in self.event_tab.winfo_children():
                widgets.pack_forget()
            self.eventtab_widgets()

    def switch_screen(self, new_screen):
        # Save the current screen to the stack
        if self.current_screen:
            self.screen_stack.append(self.current_screen)
        # Clear the current screen
        for widget in self.winfo_children():
            widget.destroy()
        # Display the new screen
        self.current_screen = new_screen
        new_screen()

    def back(self):
        if self.screen_stack:
            # Clear the current screen
            for widget in self.winfo_children():
                widget.destroy()
            # Restore the previous screen from the stack
            self.current_screen = self.screen_stack.pop()
            self.current_screen()
            
    def back_but(self, 
                 parent, 
                 side="", 
                 anchor=None, 
                 padx=(0,0), pady=(0,0), 
                 row=None, 
                 column=None, 
                 rowspan=None, 
                 columnspan=None,
                 ipady=None,
                 ipadx=None,
                 ):
        back_img = ctk.CTkImage(dark_image=Image.open(r"pics\back.png"))

        back_button = ctk.CTkButton(
            parent,
            text="",
            font=("helvetica", 15),
            command=self.back,
            width=70, height=25,
            corner_radius=100,
            fg_color="#8bceba",
            image=back_img,
            text_color="#092928"
        )
        
        if row is None:
            back_button.pack(side=side, padx=padx, pady=pady, anchor=anchor)
        else:
            back_button.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, rowspan=rowspan)
        self.add_hover_effect(back_button)

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

    def topbar(self, frame_name):
        self.top_frame = ctk.CTkFrame(frame_name, fg_color="white")
        self.top_frame.pack(side="top",fill="x", ipady=5)
#-----------------------
        # Logo and title
        logo_frame = ctk.CTkFrame(self.top_frame, fg_color="white")
        logo_frame.pack(side="left", padx=10)

        label1 = ctk.CTkLabel(logo_frame, text="cvent", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), bg_color="white")
        label1.pack(side="left")

        label2 = ctk.CTkLabel(logo_frame, text="|", font=ctk.CTkFont(size=19, weight="bold"),text_color="black", bg_color="white")
        label2.pack(side="left", padx=10)

        label3 = ctk.CTkLabel(logo_frame, text="EVENTS", text_color="#3fa6fb", font=ctk.CTkFont(size=17, weight="bold"), bg_color="white")
        label3.pack(side="left")
#-----------------------
        # Options
        options_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        options_frame.pack(side="left", expand=True, fill="x")

        another_frame = ctk.CTkFrame(options_frame, fg_color="white", bg_color="white")
        another_frame.pack(anchor="center")

        label4 = ctk.CTkButton(another_frame, text="All Events", text_color="black", font=ctk.CTkFont(size=17, weight="normal"), command = lambda : self.back_preview(frame_name), fg_color="white", hover_color="white")
        label4.pack(side="left", padx=10)

        # label4.bind("<Button-1>", lambda : self.main_app.back_preview(self.home_main_frame))

        x1 = ctk.StringVar(value="Calendar")
        opt1 = ctk.CTkComboBox(another_frame, variable=x1, width=100, values=["2020", "2021", "2022", "2023"], fg_color="white", button_color=self.secondary_color, bg_color="white")
        opt1.pack(side="left")

        x2 = ctk.StringVar(value="More")
        opt2 = ctk.CTkComboBox(another_frame, variable=x2, width=90, values=["", "", "", ""], fg_color="white", button_color=self.secondary_color, bg_color="white")
        opt2.pack(side="left", padx=10)
#-----------------------
        # Icons
        icons_frame = ctk.CTkFrame(self.top_frame, fg_color="white")
        icons_frame.pack(side="right", padx=10)

        for icon_path in ["loupe.png", "file.png", "question.png", "user (1).png", "menu.png"]:
            img = ctk.CTkImage(dark_image=Image.open(f"pics/{icon_path}"), size=(20, 20))
            button = ctk.CTkButton(icons_frame, image=img, text="", width=20, fg_color="white", bg_color="white", hover_color="#3fa6fb")
            button.pack(side="left", padx=2)

    def initial_screen(self):
        self.switch_screen(self._initial_screen)

    def _initial_screen(self):
        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=0, column=0)

        self.buttons_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="gainsboro")
        self.buttons_frame.grid(row=0, column=1, padx=20, pady=(5, 10), ipady=70, ipadx=58)

        self.bg_image = ctk.CTkImage(dark_image=Image.open("pics\loginscreen_image.png"), size=(350, 510))
        self.image_label = ctk.CTkLabel(self.image_frame, text="", image=self.bg_image)
        self.image_label.pack()
        
        welcome_label = ctk.CTkLabel(
            self.buttons_frame, 
            text="Welcome \nTo \nEvent Manager",
            font=('Segoe UI', 25, "bold"),
            fg_color="#8bceba",
            compound="center",
            # height=20,
            text_color="white",
            corner_radius=9,
        ) 
        
        welcome_label.pack(
            pady=(10, 0), 
            side="top", 
        )

        login_button = ctk.CTkButton(
            self.buttons_frame, 
            text="Login", 
            font=("helvetica", 20), 
            command=lambda: self.login(self.connection), 
            width=110, height=35, 
            corner_radius=100, 
            fg_color="#8bceba", 
            text_color="#092928",
        )
        
        register_button = ctk.CTkButton(
            self.buttons_frame, 
            text="Register", 
            font=("helvetica", 20), 
            command=lambda: self.register(self.connection), 
            width=85, height=35, 
            corner_radius=100, 
            fg_color="#8bceba", 
            text_color="#092928"
        )

        login_button.pack(pady=(100, 10), side="top")
        register_button.pack(side="top")

        # Bind hover events for the buttons
        self.add_hover_effect(login_button)
        self.add_hover_effect(register_button)

    def register(self, connection):
        self.switch_screen(lambda: self._register_screen(connection))

    def _register_screen(self, connection):
        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=0, column=0)

        self.buttons_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="gainsboro")
        self.buttons_frame.grid(row=0, column=1, padx=20, pady=(0, 10))

        self.bg_image = ctk.CTkImage(dark_image=Image.open("pics\loginscreen_image.png"), size=(350, 510))
        self.image_label = ctk.CTkLabel(self.image_frame, text="", image=self.bg_image)
        self.image_label.pack()

        welcome_label = ctk.CTkLabel(
            self.buttons_frame, 
            text="Register",
            font=('Segoe UI.', 25, "bold"),
            fg_color="#8bceba",
            compound="center",
            text_color="white",
            corner_radius=9,
        ) 
        
        welcome_label.grid(
            pady=(10, 0), 
            row=0, column=0,
            columnspan=2,
            ipady=6,
            ipadx=10
        )

        email_label = ctk.CTkLabel(self.buttons_frame, text="Enter email ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")
        password_label = ctk.CTkLabel(self.buttons_frame, text="Enter password ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")
        retype_password_label = ctk.CTkLabel(self.buttons_frame, text="Retype password ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")

        email_label.grid(row=1, column=0, sticky="w", pady=(50, 10), padx=(20, 10))
        password_label.grid(row=2, column=0, sticky="w", padx=(20, 10))
        retype_password_label.grid(row=3, column=0, sticky="w", pady=10, padx=(20, 10))

        email = ctk.StringVar()
        password = ctk.StringVar()
        retype_password = ctk.StringVar()

        email_field = ctk.CTkEntry(self.buttons_frame, textvariable=email)
        password_field = ctk.CTkEntry(self.buttons_frame, textvariable=password, show='*')
        retype_pass_field = ctk.CTkEntry(self.buttons_frame, textvariable=retype_password, show='*')

        email_field.grid(row=1, column=1, sticky="nsew", pady=(50, 10), padx=(0, 8))
        password_field.grid(row=2, column=1, sticky="nsew", padx=(0, 8))
        retype_pass_field.grid(row=3, column=1, sticky="nsew", pady=10, padx=(0, 8))

        def check(e):
            if email.get().isdigit() or password.get().isdigit():
                showerror("Value Error!", "Please input Characters.")
            elif email.get() == "" or password.get() == "":
                showerror("Value Error!", "Please input Characters.")
            else:
                if password.get() != retype_password.get():
                    showwarning("Try Again!", "Passwords do not match. Registration failed.")
                else:
                    with connection.cursor() as cursor:
                        sql = "SELECT * FROM user WHERE user_name = %s"
                        cursor.execute(sql, (email.get(),))
                        result = cursor.fetchone()

                    if result:
                        showinfo("Registration failed.", "email already exists.")
                    else:
                        with connection.cursor() as cursor:
                            sql = "INSERT INTO user (user_name, password) VALUES (%s, %s)"
                            cursor.execute(sql, (email.get(), password.get()))
                            connection.commit()
                            showinfo("Done!", "Registration successful!\nNow you can Login.")
                            self.login(self.connection)

        password_field.bind("<Return>", check)

        check_button = ctk.CTkButton(
            self.buttons_frame, 
            text="Submit", 
            command=check,
            font=("helvetica", 20),
            width=85, height=35,
            corner_radius=100,
            fg_color="#8bceba",
            text_color="#092928",
        )
        check_button.grid(row=4, column=0, columnspan=2, padx=(40, 20), pady=(17, 0))
        check_button.bind("<Return>", check)

        self.add_hover_effect(check_button)

        self.back_but(self.buttons_frame, row=5, column=0, columnspan=2, padx=(0, 200), pady=(90, 10))

    def login(self, connection):
        self.switch_screen(lambda: self._login(connection))

    def _login(self, connection):
        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=0,column=0)

        self.buttons_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="gainsboro")
        self.buttons_frame.grid(row=0,column=1, padx=20, pady=(0,10),ipadx=3)

        self.bg_image = ctk.CTkImage(dark_image=Image.open("pics\loginscreen_image.png"), size=(350,510))
        self.image_label = ctk.CTkLabel(self.image_frame, text="", image=self.bg_image)
        self.image_label.pack()

        welcome_label = ctk.CTkLabel(
            self.buttons_frame, 
            text="Login",
            font=('Segoe UI.', 25, "bold"),
            fg_color="#8bceba",
            compound="center",
            text_color="white",
            corner_radius=9,
        ) 
        
        welcome_label.grid(
            pady=(10, 0), 
            row=0, column=0,
            columnspan=2,
            ipady=8,
            ipadx=8
        )

        email_label = ctk.CTkLabel(self.buttons_frame, text="Enter email ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")
        password_label = ctk.CTkLabel(self.buttons_frame, text="Enter password ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")

        email_label.grid(row=1, column=0, sticky="w", pady=(50,10), padx=(20,10))
        password_label.grid(row=2, column=0, sticky="nsew", padx=(20,10))

        email = ctk.StringVar()
        password = ctk.StringVar()

        email_field = ctk.CTkEntry(self.buttons_frame, textvariable=email)
        password_field = ctk.CTkEntry(self.buttons_frame, textvariable=password, show='*')

        email_field.grid(row=1, column=1, pady=(50,10), padx=(0,10))
        password_field.grid(row=2, column=1, padx=(0,10))

        def check(event=None):
            if email.get().isdigit() or password.get().isdigit():
                showerror("Value Error!", "Please input Characters.")
            elif email.get() == "" or password.get() == "":
                showerror("Value Error!", "Please input Characters.")
            else:
                cursor = connection.cursor()
                sql = "SELECT * FROM user WHERE user_name = %s AND password = %s"
                cursor.execute(sql, (email.get(), password.get()))
                result = cursor.fetchone()

                if result:
                    showinfo("", "Login successful")
                    self.create_widgets()
                else:
                    msg = showwarning("User Not found", "You have to Sign-Up..")
                    if msg == 'ok':
                        self.register(connection)

        password_field.bind("<Return>", check)

        check_button = ctk.CTkButton(
            self.buttons_frame, 
            text="Submit", 
            command=check,
            font=("helvetica", 20),
            width=25, height=35,
            corner_radius=100,
            fg_color="#8bceba",
            text_color="#092928",
            )
        check_button.grid(row=3, column=0, columnspan=2, padx=(40,20), pady=(17,0))

        self.add_hover_effect(check_button)
        self.back_but(self.buttons_frame,row=4, column=0, columnspan=2, padx=(0, 200), pady=(70,10))
        
    def create_widgets(self):
        self.switch_screen(self._create_widgets)

    def _create_widgets(self):
        self.toggle_fullscreen()
        self.resizable(width=True, height=True)
        self.bind("<F11>", self.toggle_fullscreen)

        frame2 = ctk.CTkFrame(self, height=30, fg_color="#4bceba")
        frame2.pack(fill="x")

        primary_color_frame = ctk.CTkFrame(frame2, height=45,fg_color=self.hovercolor_bg,corner_radius=0)
        primary_color_frame.place(x=0,y=-3,relwidth=1)

        corner_colors = ("#20807f", "#20807f", "#4bceba", "#4bceba")
    
        labe = ctk.CTkButton(frame2, text="Event Manager", font=("Segoe UI", 40, "bold"), text_color="white",fg_color=self.secondary_color, width=100, height=35,corner_radius=100,background_corner_colors=corner_colors,hover=False)
        labe.pack(pady=10, expand=True)

        # Create a self.notebook (tabbed interface)
        self.notebook = ctk.CTkTabview(self, width=700, height=500, bg_color = self.hovercolor_bg, corner_radius=12) #3fa572 #333333
        self.notebook.pack(padx=20, pady=20, fill="both", expand=True)

        # Dashboard Tab
        self.dashboard_tab = self.notebook.add("Dashboard")
        self.dashboard_widgets()

        # Event Management Tab
        self.event_tab = self.notebook.add("Event Management")
        self.eventtab_widgets()
        self.events = DashboardPage(self)

        # Registration and Ticketing Tab
        self.register_tab = self.notebook.add("Registration and Ticketing")
        self.registertab_widgets()

        # Reporting and Analytics Tab
        self.attendee_tab = self.notebook.add("Attendee / Invitee")
        self.attendeetab_widgets()

        # Survey and Feedback Tab
        self.survey_tab = self.notebook.add("Survey and Feedback")
        self.surveytab_widgets()

        self.notebook.set("Event Management")

    def dashboard_widgets(self):
        ctk.CTkLabel(self.dashboard_tab, text="Welcome to Your Dashboard!", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

    def eventtab_widgets(self):

        self.previewmain_frame = ctk.CTkFrame(self.event_tab, fg_color = "#F0F0F0")
        self.previewmain_frame.pack(side="top", fill="both", expand= True)

        self.topbar(self.previewmain_frame)
        
        self.canvas1 = tk.Canvas(self.previewmain_frame,height = 3,width = 1920,bg = "#0061ff",relief = tk.RAISED)
        self.canvas1.pack(side="top")

        top_bar2 = ctk.CTkFrame(self.previewmain_frame, fg_color="white")
        top_bar2.pack(side="top", fill="x", ipady=30)

        self.label15 = ctk.CTkLabel(top_bar2,text = "Events",text_color = "#000000",font = ctk.CTkFont(size = 20,weight = "bold"))
        self.label15.pack(side="left", padx=(20,0))

        self.event_form = CreateEvent(self.event_tab, self)

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

        inner_frame2 = ctk.CTkFrame(inner_frame1,height = 68,width = 1172,fg_color = "#E6E6E6",corner_radius=0) #E6E6E6
        inner_frame2.pack(fill="both", padx=1, pady=(0,1))

        x8 = tk.StringVar()
        text = "There are no events in this view."
        x8.set(text)
        data_label = ctk.CTkLabel(inner_frame2,text_color = "#000000",textvariable = x8,font = ctk.CTkFont(size = 15,weight = "bold"))
        data_label.pack(side="top")

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


    def registertab_widgets(self):
        # ctk.CTkLabel(self.ticket_tab, text="Handle registrations and tickets", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
        self.register_page = RegistrationPage(self)
        self.register_page.registration_proccess()
    # def register_settings_tab(self):
    #     self.register_page.registration_settings

    def attendeetab_widgets(self):
        ctk.CTkLabel(self.attendee_tab, text="View analytics and reports", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

    def surveytab_widgets(self):
        ctk.CTkLabel(self.survey_tab, text="Create surveys and view responses", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
    

if __name__ == "__main__":
    app = DemoApplication()
    app.mainloop()