import customtkinter as ctk
from PIL import Image, ImageEnhance
import pymysql as pq
from tkinter.messagebox import showinfo, showwarning, showerror

class DemoApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.resizable(width=False, height=False)
        self.title("DemoApplication")
        self.configure(fg_color="#093838")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.connection = self.connect_to_database()
        self.screen_stack = []
        self.current_screen = None
        self.login_screen()

    def connect_to_database(self):
        connection = pq.connect(
            host="localhost",
            user="root",
            password="root",
            database="projects",
            port=3307,
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

    def login_screen(self):
        self.switch_screen(self._login_screen)

    def _login_screen(self):
        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=0,column=0)

        self.buttons_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="gainsboro")
        self.buttons_frame.grid(row=0,column=1, padx=20, pady=(0,10), ipady=70, ipadx=70)

        self.bg_image = ctk.CTkImage(dark_image=Image.open("loginscreen_image.png"), size=(350,510))
        self.image_label = ctk.CTkLabel(self.image_frame, text="", image=self.bg_image)
        self.image_label.pack()
        
        welcome_label = ctk.CTkLabel(
            self.buttons_frame, 
            text="Welcome \nTo \nEvent Manager",
            font=('Franklin Gothic Medium Cond', 25, "bold"),
            fg_color="#8bceba",
            compound="center",
            height=70,
            text_color="white",
            corner_radius=9,
        ) 
        
        welcome_label.pack(
            pady=(10,0), 
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

        login_button.pack(pady=(100,10), side="top")
        register_button.pack(side="top")

        # Bind hover events for the buttons
        self.add_hover_effect(login_button)
        self.add_hover_effect(register_button)

    def register(self, connection):
        self.switch_screen(lambda: self._register_screen(connection))

    def _register_screen(self, connection):
        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=0,column=0)

        self.buttons_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="gainsboro")
        self.buttons_frame.grid(row=0,column=1, padx=20, pady=(0,10))

        self.bg_image = ctk.CTkImage(dark_image=Image.open("loginscreen_image.png"), size=(350,510))
        self.image_label = ctk.CTkLabel(self.image_frame, text="", image=self.bg_image)
        self.image_label.pack()

        username_label = ctk.CTkLabel(self.buttons_frame, text="Enter username ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")
        password_label = ctk.CTkLabel(self.buttons_frame, text="Enter password ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")
        retype_password_label = ctk.CTkLabel(self.buttons_frame, text="Retype password ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")

        username_label.grid(row=0, column=0, sticky="nsew", pady=(90,10), padx=(20,10))
        password_label.grid(row=1, column=0, sticky="nsew", padx=(20,10))
        retype_password_label.grid(row=2, column=0, sticky="nsew", pady=10, padx=(20,10))

        username = ctk.StringVar()
        password = ctk.StringVar()
        retype_password = ctk.StringVar()

        username_field = ctk.CTkEntry(self.buttons_frame, textvariable=username)
        password_field = ctk.CTkEntry(self.buttons_frame, textvariable=password, show='*')
        retype_pass_field = ctk.CTkEntry(self.buttons_frame, textvariable=retype_password, show='*')

        username_field.grid(row=0, column=1, sticky="nsew", pady=(90,10), padx=(0,10))
        password_field.grid(row=1, column=1, sticky="nsew", padx=(0,10))
        retype_pass_field.grid(row=2, column=1, sticky="nsew", pady=10, padx=(0,10))

        def check():
            if username.get().isdigit() or password.get().isdigit():
                showerror("Value Error!", "Please input Characters.")
            elif username.get() == "" or password.get() == "":
                showerror("Value Error!", "Please input Characters.")
            else:
                if password.get() != retype_password.get():
                    showwarning("Try Again!", "Passwords do not match. Registration failed.")
                else:
                    with connection.cursor() as cursor:
                        sql = "SELECT * FROM user WHERE user_name = %s"
                        cursor.execute(sql, (username.get(),))
                        result = cursor.fetchone()

                    if result:
                        showinfo("Registration failed.", "Username already exists.")
                    else:
                        with connection.cursor() as cursor:
                            sql = "INSERT INTO user (user_name, password) VALUES (%s, %s)"
                            cursor.execute(sql, (username.get(), password.get()))
                            connection.commit()
                            showinfo("Done!", "Registration successful!")
                            self.create_widgets()

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
        check_button.grid(row=3, column=0, columnspan=2, padx=(40,20), pady=(17,0))

        self.add_hover_effect(check_button)

        back_img = ctk.CTkImage(dark_image=Image.open("back.png"))

        back_button = ctk.CTkButton(
            self.buttons_frame,
            text="",
            font=("helvetica", 15),
            command=self.back,
            width=70, height=25,
            corner_radius=100,
            fg_color="#8bceba",
            image=back_img,
            text_color="#092928"
        )
        back_button.grid(row=4, column=0, columnspan=2, padx=(0, 200), pady=(90,10))

        self.add_hover_effect(back_button)

    def login(self, connection):
        self.switch_screen(lambda: self._login(connection))

    def _login(self, connection):
        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=0,column=0)

        self.buttons_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="gainsboro")
        self.buttons_frame.grid(row=0,column=1, padx=20, pady=(0,10))

        self.bg_image = ctk.CTkImage(dark_image=Image.open("loginscreen_image.png"), size=(350,510))
        self.image_label = ctk.CTkLabel(self.image_frame, text="", image=self.bg_image)
        self.image_label.pack()

        username_label = ctk.CTkLabel(self.buttons_frame, text="Enter username: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")
        password_label = ctk.CTkLabel(self.buttons_frame, text="Enter password: ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")

        username_label.grid(row=0, column=0, sticky="nsew", pady=(90,10), padx=(20,10))
        password_label.grid(row=1, column=0, sticky="nsew", padx=(20,10))

        username = ctk.StringVar()
        password = ctk.StringVar()

        username_field = ctk.CTkEntry(self.buttons_frame, textvariable=username)
        password_field = ctk.CTkEntry(self.buttons_frame, textvariable=password, show='*')

        username_field.grid(row=0, column=1, pady=(90,10), padx=(0,10))
        password_field.grid(row=1, column=1, padx=(0,10))

        def check():
            if username.get().isdigit() or password.get().isdigit():
                showerror("Value Error!", "Please input Characters.")
            elif username.get() == "" or password.get() == "":
                showerror("Value Error!", "Please input Characters.")
            else:
                cursor = connection.cursor()
                sql = "SELECT * FROM user WHERE user_name = %s AND password = %s"
                cursor.execute(sql, (username.get(), password.get()))
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
            width=85, height=35,
            corner_radius=100,
            fg_color="#8bceba",
            text_color="#092928",
            )
        check_button.grid(row=2, column=0, columnspan=2, padx=(40,20), pady=(17,0))

        back_img = ctk.CTkImage(dark_image=Image.open("back.png"))

        back_button = ctk.CTkButton(
            self.buttons_frame,
            text="",
            font=("helvetica", 15),
            command=self.back,
            width=70, height=25,
            corner_radius=100,
            fg_color="#8bceba",
            image=back_img,
            text_color="#092928"
        )
        back_button.grid(row=3, column=0, columnspan=2, padx=(0, 200), pady=(90,10))

        self.add_hover_effect(check_button)
        self.add_hover_effect(back_button)
        
    def create_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

        frame2 = ctk.CTkFrame(self, height=30, fg_color="#2fa572")
        frame2.pack(fill="both")

        labe = ctk.CTkLabel(frame2, text="Event Management System", font=("Segoe UI", 40, "bold"))
        labe.grid(row=0, column=0, padx=(420, 220))

        self.head_img = ctk.CTkImage(dark_image=Image.open("Logo.png"), size=(200, 90))
        head_label = ctk.CTkLabel(frame2, image=self.head_img, text="")
        head_label.grid(row=0, column=1)

        # Create a notebook (tabbed interface)
        notebook = ctk.CTkTabview(self, width=700, height=500, fg_color="#3fa572")
        notebook.pack(padx=20, pady=20, fill="both", expand=True)

        # Dashboard Tab
        dashboard_tab = notebook.add("Dashboard")

        # Event Management Tab
        event_tab = notebook.add("Event Management")
        ctk.CTkLabel(event_tab, text="Manage your events here", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        # Registration and Ticketing Tab
        ticket_tab = notebook.add("Registration and Ticketing")
        ctk.CTkLabel(ticket_tab, text="Handle registrations and tickets", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        # Reporting and Analytics Tab
        report_tab = notebook.add("Reporting and Analytics")
        ctk.CTkLabel(report_tab, text="View analytics and reports", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        # Survey and Feedback Tab
        survey_tab = notebook.add("Survey and Feedback")
        ctk.CTkLabel(survey_tab, text="Create surveys and view responses", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

if __name__ == "__main__":
    app = DemoApplication()
    app.mainloop()

