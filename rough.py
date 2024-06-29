import customtkinter as ctk
from PIL import Image
import pymysql as pq
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning, showerror
from registration import RegistrationPage  


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
        # self.minsize(width,height)

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
        check_button.bind("<Enter>", check)

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
        notebook = ctk.CTkTabview(self, width=700, height=500, bg_color = "gainsboro", corner_radius=12) #3fa572 #333333
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
        self.report_tab = notebook.add("Venue Sourcing")
        self.reporttab_widgets()

        # Survey and Feedback Tab
        self.survey_tab = notebook.add("Survey and Feedback")
        self.surveytab_widgets()

    def dashboard_widgets(self):
        ctk.CTkLabel(self.dashboard_tab, text="Welcome to Your Dashboard!", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

    def eventtab_widgets(self):
        # ctk.CTkLabel(self.event_tab, text="Manage your events here", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        f1 = ctk.CTkFrame(self.event_tab,height = 41,width = 1300,fg_color = "white")
        f1.place(x = 0,y = 0)

        label1 = ctk.CTkLabel(f1,text = "cvent",text_color = "black",justify = "right",font = ctk.CTkFont(size =  20,weight = "bold"))
        label1.place(x = 15,y = 5)

        label2 = ctk.CTkLabel(f1,text = "",width = 2,height = 20,fg_color = "black")
        label2.place(x = 80,y = 9.5)

        label3 = ctk.CTkLabel(f1,text = "EVENTS",text_color = "#3fa6fb",font = ctk.CTkFont(size = 17,weight = "bold"))
        label3.place(x = 95,y = 5)

        label4 = ctk.CTkLabel(f1,text = "All Events",text_color = "black",font = (ctk.CTkFont(size = 17,weight = "normal")))
        label4.place(x = 420,y = 5)

        x1 =ctk.StringVar()
        x1.set("Calendar")
        opt1 = ctk.CTkComboBox(f1,variable = x1,height = 35,width = 100,fg_color = "white",text_color = "black",border_color = "white",button_color = "white",button_hover_color = "white",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["2020","2021","2022","2023"])
        opt1.place(x = 540,y = 5)

        x2 =ctk.StringVar()
        x2.set("More")
        opt2 = ctk.CTkComboBox(f1,variable = x2,height = 35,width = 90,fg_color = "white",text_color = "black",border_color = "white",button_color = "white",button_hover_color = "white",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
        opt2.place(x = 670,y = 5)

        def butimg1():
            pass

        img1 = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (20,20))
        butimg1 = ctk.CTkButton(f1,image = img1,fg_color = "white",width = 20,text = "",hover_color = "#3fa6fb",command = butimg1)
        butimg1.place(x = 1040,y = 5)

        def butimg2():
            pass 

        img2 = ctk.CTkImage(dark_image = Image.open(r"pics\file.png"),size = (20,20))
        butimg2 = ctk.CTkButton(f1,image = img2,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg2)
        butimg2.place(x = 1090,y = 5)

        def butimg3():
            pass

        img3 = ctk.CTkImage(dark_image = Image.open(r"pics\question.png"),size = (20,20))
        butimg3 = ctk.CTkButton(f1,image = img3,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg3)
        butimg3.place(x = 1140,y = 5)

        def butimg4():
            pass

        img4 = ctk.CTkImage(dark_image = Image.open(r"pics\user (1).png"),size = (20,20))
        butimg4 = ctk.CTkButton(f1,image = img4,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg4)
        butimg4.place(x = 1190,y = 5)

        def butimg5():
            pass

        img5 = ctk.CTkImage(dark_image = Image.open(r"pics\menu.png"),size = (20,20))
        butimg5 = ctk.CTkButton(f1,image = img5,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg5)
        butimg5.place(x = 1240,y = 5)

        canvas1 = tk.Canvas(self.event_tab,height = 3,width = 1920,bg = "#0061ff",relief = "raised")
        canvas1.place(x = 0,y = 56)

        f2 = ctk.CTkFrame(self.event_tab,height = 44,width = 1300,fg_color = self.secondary_color)
        f2.place(x = 0,y = 41)

        self.click_count = 0
        def menu_animation(): # MENU ANIMATION COMMAND ...
            self.click_count += 1

            if self.click_count % 2 != 0 :
                self.after(1, animate(250,82, 0.808))

                self.f3 = ctk.CTkFrame(self.event_tab,fg_color = "white",height = 600,width = 250,border_width = 1,border_color = "lightgray")
                self.f3.place(x = 0,y = 81)

                label6 = ctk.CTkLabel(self.f3,text = "HOME",text_color = "#3fa6fb",font = (ctk.CTkFont(size = 20,weight = "bold")))
                label6.place(x = 13,y = 17)

                x4 =ctk.StringVar()
                x4.set("General")
                opt3 = ctk.CTkOptionMenu(self.f3,variable = x4,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
                opt3.place(x = 5,y = 50)

                x5 =ctk.StringVar()
                x5.set("Marketing")
                opt4 = ctk.CTkOptionMenu(self.f3,variable = x5,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
                opt4.place(x = 5,y = 100)

                x6 =ctk.StringVar()
                x6.set("Email")
                opt5 = ctk.CTkOptionMenu(self.f3,variable = x6,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
                opt5.place(x = 5,y = 150)

                x7 =ctk.StringVar()
                x7.set("Attendees")
                opt6 = ctk.CTkOptionMenu(self.f3,variable = x7,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
                opt6.place(x = 5,y = 200)

                x8 =ctk.StringVar()
                x8.set("Reports")
                opt7 = ctk.CTkOptionMenu(self.f3,height = 35,width = 230,variable = x8,fg_color = "white",dropdown_hover_color = "lightblue",text_color = "black",button_color = "white",button_hover_color = "white",values = ["","","",""])
                opt7.place(x = 5,y = 250)

                b1 = ctk.CTkLabel(self.f3,text = "Integrations",fg_color = "white",text_color = "black")
                b1.place(x = 10,y = 300)
            else:
                self.f3.destroy()
                self.f0.place(x=0, y=82,relwidth=1.0)

        def animate(x,y,relwidth=None):
            self.f0.place(x=x, y=y, relwidth=relwidth)

        img6 = ctk.CTkImage(dark_image = Image.open(r"pics\lines.png"),size = (20,20))
        butimg6 = ctk.CTkButton(f2,image = img6,text = "",fg_color = "white",width = 20,hover_color = "white",command = menu_animation)
        butimg6.place(x = 6,y = 5)

        label5 = ctk.CTkLabel(f2,text = "DemEven",text_color = "black",font = (ctk.CTkFont(size = 15,weight = "normal")))
        label5.place(x = 47,y = 5)

        x3 =ctk.StringVar()
        e1 = ctk.CTkEntry(f2,height = 28,width = 250,fg_color = "white",corner_radius = 15,placeholder_text = "Search this Event",placeholder_text_color = "gray",text_color = "black",textvariable = x3)
        e1.place(x = 1000,y = 5)

        def butimg7():
            pass

        img7 = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (20,15))
        butimg7 = ctk.CTkButton(f2,image = img7,text = "",fg_color = "white",width = 20,border_width = 1,border_color = "black",hover_color = "#8BFAFF",command = butimg7)
        butimg7.place(x = 958,y = 5)

#-----------------------

        self.f0 = ctk.CTkScrollableFrame(self.event_tab,height = 700,fg_color = "#F0F0F0")
        self.f0.place(x = 0,y = 82, relwidth=1.0)

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
        f02.grid(row=0,column=1, padx=12, sticky="n")

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

    def tickettab_widgets(self):
        # ctk.CTkLabel(self.ticket_tab, text="Handle registrations and tickets", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
        RegistrationPage(self.ticket_tab)

    def reporttab_widgets(self):
        ctk.CTkLabel(self.report_tab, text="View analytics and reports", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

    def surveytab_widgets(self):
        ctk.CTkLabel(self.survey_tab, text="Create surveys and view responses", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
        
if __name__ == "__main__":
    app = DemoApplication()
    app.mainloop()