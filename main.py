import customtkinter as ctk
from PIL import Image
import pymysql as pmql
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning, showerror
from model.auth import GoogleSignInApp, Auth
from model.database_structure import Db
from view.eventshome import DashboardPage
from view.registration import RegistrationPage
from view.invitation import InviteeAttendeePage
from view.surveyresponse import SurveyResponsePage
from view.eventview import EventView
from model.backend import DataClass

#COLORS :  #093838 -> Primary Color.    } In the Theme,
           #8bceba -> Secondary Color.  }  both the Primary & Secondary colors are used interchangeably.
           #gainsboro -> Background Color.
           #092928 -> Text Color.
           #20807f -> Hover Bg Color.
           #white -> Hover Text Color. git add <resolved_file>

class DemoApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.resizable(width=False, height=False)
        self.title("DemoApplication")
        self.configure(fg_color="#093838")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("my_custom_theme.json")
    
        self.primary_color = "#093838"
        self.secondary_color = "#8bceba"
        self.bg = "gainsboro"
        self.text_color = "#092928"
        self.hovercolor_bg = "#20807f"
        self.hovercolor_txt = "white"
        self.screen_stack = []
        self.current_screen = None
        database =Db(self)
        database.create_database()
        self.datab_name = database.db_name
        self.connections = self.connect_to_database()

        self.auth = Auth()
        self.initial_screen()
        self.backend = DataClass(self)
        self.user = None
        self.count = 0

    def connect_to_database(self):
            self.connection = pmql.connect(
                host="localhost",
                user="root",
                password="sankalp",
                charset="utf8",
                database= self.datab_name,
            )
            self.cur = self.connection.cursor()

    def google_sign_in_handler(self):
        sign_in = GoogleSignInApp()
        if sign_in.handle_google_sign_in():
            self.create_widgets()
        else:
            self.initial_screen()
    
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
        if frame_name == self.event_preview.previewmain_frame:
            return None
        else:
            for widgets in self.event_tab.winfo_children():
                widgets.pack_forget()
            self.event_preview.eventtab_widgets()

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
            command=lambda: self.login(), 
            width=110, height=35, 
            corner_radius=100, 
            fg_color="#8bceba", 
            text_color="#092928",
        )
        
        register_button = ctk.CTkButton(
            self.buttons_frame, 
            text="Register", 
            font=("helvetica", 20), 
            command=lambda: self.register(), 
            width=85, height=35, 
            corner_radius=100, 
            fg_color="#8bceba", 
            text_color="#092928"
        )
        google_sign_in_button = tk.Button(self.buttons_frame, text="Sign in with Google", command=self.google_sign_in_handler)
        google_sign_in_button.pack(pady=20)

        login_button.pack(pady=(100, 10), side="top")
        register_button.pack(side="top")

        # Bind hover events for the buttons
        self.add_hover_effect(login_button)
        self.add_hover_effect(register_button)

    def register(self):
        self.switch_screen(lambda: self._register_screen())

    def _register_screen(self):
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

        def check(event=None):
            if email.get().isdigit() or password.get().isdigit():
                showerror("Value Error!", "Please input Characters.")
            elif email.get() == "" or password.get() == "":
                showerror("Value Error!", "Please input Characters.")
            else:
                if password.get() != retype_password.get():
                    showwarning("Try Again!", "Passwords do not match. Registration failed.")
                else:
                    sql = "SELECT * FROM user WHERE email= %s"
                    self.cur.execute(sql, (email.get(),))
                    result = self.cur.fetchone()
                    if result:
                        showinfo("Registration failed.", "email already exists.")
                    else:
                        sql = "INSERT INTO user (email, password) VALUES (%s, %s)"
                        self.cur.execute(sql, (email.get(), password.get()))
                        self.connection.commit()
                        showinfo("Done!", "Registration successful!\nNow you can Login.")
                        query = ("SELECT user_id from user where email=%s")
                        id = self.cur.execute(query, (email.get()))
                        print("user_id : ", id)
                        self.destroy()
                        new_app = DemoApplication()
                        new_app.mainloop()

        retype_pass_field.bind("<Return>", check)

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

    def login(self):
        self.switch_screen(lambda: self._login())

    def _login(self):
        
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
                self.user = self.auth.authenticate(email.get(), password.get())
                if self.user:
                    showinfo("", "Login successful")
                    if self.backend.is_first_time_user(self.user):
                        self.create_widgets() 
                    else:
                        self.show_regular_app(self.user)
                else:
                    msg = showwarning("User Not found", "You have to Sign-Up..")
                    if msg == 'ok':
                        self.register()

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

    def show_regular_app(self, user_id):
        self.backend.check_existing_user_events(user_id)

    def main_screen(self):
        self.switch_screen(self._main_screen)

    def _main_screen(self):
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

        self.notebook = ctk.CTkTabview(self, bg_color = self.hovercolor_bg, corner_radius=12) #3fa572 #333333
        self.notebook.pack(pady=(10,0), fill="both", expand=True)

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
        self.notebook = ctk.CTkTabview(self, bg_color = self.hovercolor_bg, corner_radius=12) #3fa572 #333333
        self.notebook.pack( fill="both", expand=True)

        # Event Management Tab
        self.event_tab = self.notebook.add("Event Management")
        self.notebook.set("Event Management")
        self.event_preview = EventView(self)
        self.event_preview.eventtab_widgets()

    def tab_screens(self, event_name):
        self.home_page = DashboardPage(self, self.event_tab, event_name)
        self.home_page.events_home()

        self.register_page = RegistrationPage(self, self.register_tab, event_name)
        self.register_page.registration_proccess()

        self.invitation_attendee = InviteeAttendeePage(self, self.invitee_tab, event_name)
        self.invitation_attendee.invitation_list_screen()

        self.survey_response = SurveyResponsePage(self, self.survey_tab, event_name)
        self.survey_response.feedback_surveys_screen()

    def create_tabs(self, event_name):
        self.count += 1
        if self.count <= 1:
            if self.backend.is_first_time_user(self.user):
                print("self.user : ",self.user)
                self.notebook.delete("Event Management")
            else:
                self.main_screen()

            self.dashboard_tab = self.notebook.add("Dashboard")
            self.event_tab = self.notebook.add("Event Management")
            self.notebook.set("Event Management")
            self.event_preview = EventView(self)
            self.event_preview.eventtab_widgets()
            self.register_tab = self.notebook.add("Registration & Ticketing")
            self.invitee_tab = self.notebook.add("Invitation & Attendees")
            self.survey_tab = self.notebook.add("Survey & Feedback")

            self.tab_screens(event_name)
        else:
            self.tab_screens(event_name)

    def update_screens(self, event_id,  event_name, command=None,event_category=None, address=None, start_date=None, end_date=None, start_time=None, end_time=None, planner_email=None):
        self.create_tabs(event_name[-1])
        self.event_preview.update_event_list(event_name)

    def dashboard_widgets(self):
        ctk.CTkLabel(self.dashboard_tab, text="Welcome to Your Dashboard!", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

    def text_hover(self, widget):
        def on_enter(e):
            widget.configure(text_color="#3fa6fb")
        def on_leave(e):
            widget.configure(text_color="white")

        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

if __name__ == "__main__":
    app = DemoApplication()
    app.mainloop()