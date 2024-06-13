import customtkinter as ctk
from PIL import Image
import pymysql as pq
from tkinter.messagebox import showinfo, showwarning, showerror


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
        back_img = ctk.CTkImage(dark_image=Image.open("back.png"))

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
        # self.minsize(width,height)

    def initial_screen(self):
        self.switch_screen(self._initial_screen)

    def _initial_screen(self):
        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=0, column=0)

        self.buttons_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="gainsboro")
        self.buttons_frame.grid(row=0, column=1, padx=20, pady=(5, 10), ipady=70, ipadx=58)

        self.bg_image = ctk.CTkImage(dark_image=Image.open("loginscreen_image.png"), size=(350, 510))
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

        self.bg_image = ctk.CTkImage(dark_image=Image.open("loginscreen_image.png"), size=(350, 510))
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

        def check():
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

        self.add_hover_effect(check_button)

        self.back_but(self.buttons_frame, row=5, column=0, columnspan=2, padx=(0, 200), pady=(90, 10))

    def login(self, connection):
        self.switch_screen(lambda: self._login(connection))

    def _login(self, connection):
        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=0,column=0)

        self.buttons_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="gainsboro")
        self.buttons_frame.grid(row=0,column=1, padx=20, pady=(0,10),ipadx=3)

        self.bg_image = ctk.CTkImage(dark_image=Image.open("loginscreen_image.png"), size=(350,510))
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

        def check():
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
        self.bind("<F11>", self.toggle_fullscreen)

        for widget in self.winfo_children():
            widget.destroy()

        frame2 = ctk.CTkFrame(self, height=30, fg_color=self.bg)
        frame2.pack(fill="x")

        labe = ctk.CTkLabel(frame2, text="Event Manager", font=("Segoe UI", 40, "bold"), text_color="white", fg_color=self.secondary_color, corner_radius=12)
        labe.pack(pady=10, ipady=5,expand=True)

        # Create a notebook (tabbed interface)
        notebook = ctk.CTkTabview(self, width=700, height=500, bg_color=self.bg, fg_color=self.bg, corner_radius=12) #3fa572 
        notebook.pack(padx=20, pady=20, fill="both", expand=True)
        # notebook.set(self.event_tab)

        # Dashboard Tab
        self.dashboard_tab = notebook.add("Dashboard")
        self.dashboard_widgets()

        # Event Management Tab
        self.event_tab = notebook.add("Event Management")
        self.eventtab_widgets()

        # Registration and Ticketing Tab
        self.ticket_tab = notebook.add("Registration and Ticketing")
        self.tickettab_widgets()

        # Reporting and Analytics Tab
        self.report_tab = notebook.add("Reporting and Analytics")
        self.reporttab_widgets()

        # Survey and Feedback Tab
        self.survey_tab = notebook.add("Survey and Feedback")
        self.surveytab_widgets()

    def dashboard_widgets(self):
        ctk.CTkLabel(self.dashboard_tab, text="Welcome to Your Dashboard!", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

    def eventtab_widgets(self):
        ctk.CTkLabel(self.event_tab, text="Manage your events here", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

    def tickettab_widgets(self):
        # ctk.CTkLabel(self.ticket_tab, text="Handle registrations and tickets", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        my_img = ctk.CTkImage(dark_image = Image.open(r"back.png"),size = (20,20))
        labimg = ctk.CTkButton(self.ticket_tab,image = my_img,text = "",fg_color = "#F0F0F0",hover_color = "white",width = 15,border_width = 1,border_color = "#F0F0F0")
        labimg.place(x = 8,y = 5)

        l1 = ctk.CTkLabel(self.ticket_tab,text = "New event",font = ("bold",26)) #,text_color = "black",fg_color = "#F0F0F0",
        l2 = ctk.CTkLabel(self.ticket_tab,text = "Great! Tell us a little about your event.",font = ("thin",19)) #,text_color = "black",fg_color = "#F0F0F0"
        l1.place(x = 70,y = 30)
        l2.place(x = 70,y = 57)

        scrollable_frame = ctk.CTkScrollableFrame(self.ticket_tab,height = 470,width = 800,orientation = "vertical",fg_color = "white",border_width = 0.8,border_color = "black",scrollbar_button_color = "white",scrollbar_fg_color = "black")
        f1 = ctk.CTkFrame(scrollable_frame,fg_color = "white",height = 950,width = 800)
        scrollable_frame.place(x = 70,y = 105)
        f1.pack(expand=True)

        img1 = ctk.CTkImage(dark_image = Image.open(r"pics\info.png"),size = (30,30))
        labimg1 = ctk.CTkLabel(f1,image = img1,text = "")
        labimg1.place(x = 30,y = 9)

        l3 = ctk.CTkLabel(f1,text = "Basic Information",text_color = "black",font = ("darkbold",23))
        l4 = ctk.CTkLabel(f1,text = "* Event Title",text_color = "black",font = ("thin",19))
        l3.place(x = 67,y = 9)
        l4.place(x = 30,y = 50)

        def check_x1():
            if x1.get() == "":
                showerror(title = "Error",message = "Please input Event Title")

            if x2.get() == "":
                showerror(title = "Error",message = "Please choose Event Category")
            
            if x6.get() == "":
                showerror(title = "Error",message = "Please input your last name")

            if x7.get() == "":
                showerror(title = "Error",message = "Please input your Email")

            if x8.get() == "":
                showerror(title = "Error",message = "Please input full Format")

            if x10.get() == "":
                showerror(title = "Error",message = "Please input full format")

            if x14.get() == "":
                showerror(title = "Error",message = "Please choose the state")


        x1 =ctk.StringVar()
        e1 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 690,textvariable = x1)
        l5 = ctk.CTkLabel(f1,text = "* Event Category",text_color = "black",font = ("thin",19))
        e1.place(x = 30,y = 82)
        l5.place(x = 30,y = 128)

        x2 =ctk.StringVar()
        opt1 = ctk.CTkComboBox(f1,variable = x2,height = 35,width = 200,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["Educational","Business","Sports"])
        opt1.place(x = 30,y = 165)

        l6 = ctk.CTkLabel(f1,text = "Language",text_color = "black",font = ("thin",19))
        l6.place(x = 280,y = 128)
        x3 =ctk.StringVar()

        opt2 =  ctk.CTkComboBox(f1,variable = x3,height = 35,width = 200,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["English","Spanish","Hindi"])
        opt2.place(x = 280,y = 165)
        l7 = ctk.CTkLabel(f1,text = "Locale",text_color = "black",font = ("thin",19))
        l7.place(x = 520,y = 128)

        x4 =ctk.StringVar()
        opt3 =  ctk.CTkComboBox(f1,variable = x4,height = 35,width = 200,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["USA","INDIA","CANADA"])
        opt3.place(x = 520,y = 165)
        l8 = ctk.CTkLabel(f1,text = "* Planner First Name",text_color = "black",font = ("thin",19))
        l8.place(x = 30,y = 220)

        x5 =ctk.StringVar()
        e2 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x5)
        e2.place(x = 30,y = 250)
        l9 = ctk.CTkLabel(f1,text = "* Last Name",text_color = "black",font = ("thin",19))
        l9.place(x = 280,y = 220)

        x6 =ctk.StringVar()
        e3 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x6)
        e3.place(x = 280,y = 250)
        label1 = ctk.CTkLabel(f1,text = "* Planner Email",text_color = "black",font = ("thin",19))
        label1.place(x = 520,y = 220)

        x7 =ctk.StringVar()
        e4 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x7)
        e4.place(x = 520,y = 250)

        img5 = ctk.CTkImage(dark_image = Image.open(r"pics\management.png"),size = (340,280))
        labimg5 = ctk.CTkLabel(self.ticket_tab,image = img5,text = "")
        labimg5.place(x = 940,y = 130)

        label2 = ctk.CTkLabel(self.ticket_tab,text = "This is just the start..!!",text_color = "black",fg_color = "#F0F0F0",font = ("semibold",21))
        label2.place(x = 940,y = 420)
        label3 = ctk.CTkLabel(self.ticket_tab,text = "We can't wait to see what kind of event you put on!",text_color = "black",fg_color = "#F0F0F0",font = ("thin",16))
        label3.place(x = 940,y = 450)

        img2 = ctk.CTkImage(dark_image = Image.open(r"pics\location.png"),size = (30,30))
        labimg2 = ctk.CTkLabel(f1,image = img2,text = "")
        labimg2.place(x = 30,y = 310)

        label4 = ctk.CTkLabel(f1,text = "Location",text_color = "black",fg_color = "white",font = ("darkbold",23))
        label4.place(x = 67,y = 310)
        label5 = ctk.CTkLabel(f1,text = "* Format",text_color = "black",font = ("thin",19))
        label5.place(x = 30,y = 352)

        x8 =ctk.StringVar()
        e5 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x8)
        e5.place(x = 30,y = 394)

        x9 =ctk.StringVar()
        e6 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x9)
        e6.place(x = 280,y = 394)

        x10 =ctk.StringVar()
        e7 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x10)
        e7.place(x = 520,y = 394)

        label6 = ctk.CTkLabel(f1,text = "Venue",text_color = "black",font = ("thin",19))
        label6.place(x = 30,y = 436)

        x11 =ctk.StringVar()
        e8 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 690,textvariable = x11)
        e8.place(x = 30,y = 478)

        img3 = ctk.CTkImage(dark_image = Image.open(r"pics\close.png"),size = (20,20))
        labimg3 = ctk.CTkButton(self.ticket_tab,image = img3,text = "",fg_color = "#F0F0F0",hover_color = "white",width = 15,border_width = 1,border_color = "#F0F0F0")
        labimg3.place(x = 1225,y = 5)

        img4 = ctk.CTkImage(dark_image = Image.open(r"pics\mall.png"),size = (20,20))
        labimg4 = ctk.CTkLabel(e8,image = img4,text = "")
        labimg4.place(x = 653,y = 3)

        label7 = ctk.CTkLabel(f1,text = "Address",text_color = "black",font = ("thin",19))
        label7.place(x = 30,y = 520)

        x12 =ctk.StringVar()
        e9 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 690,textvariable = x12)
        e9.place(x = 30,y = 562)

        label8 = ctk.CTkLabel(f1,text = "City",text_color = "black",font = ("thin",19))
        label8.place(x = 30,y = 604)

        x13 =ctk.StringVar()
        e10 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x13)
        e10.place(x = 30,y = 646)

        label9 = ctk.CTkLabel(f1,text = "* State",text_color = "black",font = ("thin",19))
        label9.place(x = 205,y = 604)

        x14 =ctk.StringVar()
        opt4 = ctk.CTkComboBox(f1,variable = x14,height = 35,width = 145,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["Maharashtra","Rajasthan","Uttar Pradesh","Gujarat","Punjab"])
        opt4.place(x = 205,y = 646)

        label10 = ctk.CTkLabel(f1,text = "ZIP/Postal code",text_color = "black",font = ("thin",19))
        label10.place(x = 375,y = 604)

        x15 =ctk.StringVar()
        e11 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x15)
        e11.place(x = 375,y = 646)

        label11 = ctk.CTkLabel(f1,text = "Country",text_color = "black",font = ("thin",19))
        label11.place(x = 540,y = 604)

        x16 =ctk.StringVar()
        opt5 = ctk.CTkComboBox(f1,variable = x16,height = 35,width = 145,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["India","New Zealand","USA","Russia"])
        opt5.place(x = 540,y = 646)

        img6 = ctk.CTkImage(dark_image = Image.open(r"pics\calendar.png"),size = (30,30))
        labimg6 = ctk.CTkLabel(f1,image = img6,text = "")
        labimg6.place(x = 30,y = 692)

        label12 = ctk.CTkLabel(f1,text = "Event Dates",text_color = "black",font = ("darkbold",23))
        label12.place(x = 67,y = 692)

        label13 = ctk.CTkLabel(f1,text = "Start Date",text_color = "black",font = ("thin",19))
        label13.place(x = 30,y = 732)

        x17 =ctk.StringVar()
        e12 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x17)
        e12.place(x = 30,y = 768)

        label14 = ctk.CTkLabel(f1,text = "Start Time",text_color = "black",font = ("thin",19))
        label14.place(x = 205,y = 732)

        x18 =ctk.StringVar()
        e13 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x18)
        e13.place(x = 205,y = 768)

        label15 = ctk.CTkLabel(f1,text = "End Date",text_color = "black",font = ("thin",19))
        label15.place(x = 375,y = 732)

        x19 =ctk.StringVar()
        e14 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x19)
        e14.place(x = 375,y = 768)

        label16 = ctk.CTkLabel(f1,text = "End Time",text_color = "black",font = ("thin",19))
        label16.place(x = 540,y = 732)

        x20 =ctk.StringVar()
        e15 = ctk.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x20)
        e15.place(x = 540,y = 768)

        img7 = ctk.CTkImage(dark_image = Image.open(r"pics\calendar (1).png"),size = (30,30))
        labimg7 = ctk.CTkLabel(e12,image = img7,text = "")
        labimg7.place(x = 105,y = 2)

        labimg8 = ctk.CTkLabel(e14,image = img7,text = "")
        labimg8.place(x = 105,y = 2)

        label17 = ctk.CTkLabel(f1,text = "Time Zone",text_color = "black",font = ("thin",19))
        label17.place(x = 30,y = 810)

        x21 =ctk.StringVar()
        opt6 = ctk.CTkComboBox(f1,variable = x21,height = 35,width = 690,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["(GMT+05:30) India","(GMT+09:05) USA","(GMT-03:40) New Zealand"])
        opt6.place(x = 30,y = 850)

        b1 = ctk.CTkButton(f1,text = "Submit",height = 40,width = 170,corner_radius =10,fg_color = "lightgreen",text_color = "black",command = check_x1)
        b1.place(x = 300,y = 904)

    def reporttab_widgets(self):
        ctk.CTkLabel(self.report_tab, text="View analytics and reports", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

    def surveytab_widgets(self):
        ctk.CTkLabel(self.survey_tab, text="Create surveys and view responses", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
        
if __name__ == "__main__":
    app = DemoApplication()
    app.mainloop()