# import customtkinter as ctk
# from PIL import Image
# import pymysql as pq
# import tkinter as tk
# from tkinter.messagebox import showinfo, showwarning, showerror

#             # INSPECTION BRANCH #
            
# #COLORS :  #093838 -> Primary Color.    } In the Theme,
#            #8bceba -> Secondary Color.  }  both the Primary & Secondary colors are used interchangeably.
#            #gainsboro -> Background Color.
#            #092928 -> Text Color.
#            #20807f -> Hover Bg Color.
#            #white -> Hover Text Color. 

# class DemoApplication(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("700x500")
#         self.resizable(width=True, height=True)
#         self.title("DemoApplication")
#         self.configure(fg_color="#093838")

#         ctk.set_appearance_mode("dark")
#         ctk.set_default_color_theme("my_custom_theme")

#         self.primary_color = "#093838"
#         self.secondary_color = "#8bceba"
#         self.bg = "gainsboro"
#         self.text_color = "#092928"
#         self.hovercolor_bg = "#20807f"
#         self.hovercolor_txt = "white"
#         self.connection = self.connect_to_database()
#         self.screen_stack = []
#         self.current_screen = None
#         self.f3 = None
#         self.click_count = 0
#         self.initial_screen()

#     def connect_to_database(self):
#         connection = pq.connect(
#             host="localhost",
#             user="root",
#             password="root",
#             database="projects",
#             port=3306,
#             charset="utf8"
#         )
#         return connection
    
#     def add_hover_effect(self, widget):
#         original_txtcolor = "#092928"
#         original_bgcolor = widget.cget("fg_color")
#         hovercolor_txt = "white"
#         hovercolor_bg = "#20807f"
#         def on_enter(e):
#             widget.configure(fg_color=hovercolor_bg, text_color=hovercolor_txt)

#         def on_leave(e):
#             widget.configure(fg_color=original_bgcolor, text_color=original_txtcolor)

#         widget.bind("<Enter>", on_enter)
#         widget.bind("<Leave>", on_leave)

#     def switch_screen(self, new_screen):
#         # Save the current screen to the stack
#         if self.current_screen:
#             self.screen_stack.append(self.current_screen)
#         # Clear the current screen
#         for widget in self.winfo_children():
#             widget.destroy()
#         # Display the new screen
#         self.current_screen = new_screen
#         new_screen()

#     def back(self):
#         if self.screen_stack:
#             # Clear the current screen
#             for widget in self.winfo_children():
#                 widget.destroy()
#             # Restore the previous screen from the stack
#             self.current_screen = self.screen_stack.pop()
#             self.current_screen()
            
#     def back_but(self, 
#                  parent, 
#                  side="", 
#                  anchor=None, 
#                  padx=(0,0), pady=(0,0), 
#                  row=None, 
#                  column=None, 
#                  rowspan=None, 
#                  columnspan=None,
#                  ipady=None,
#                  ipadx=None,
#                  ):
#         back_img = ctk.CTkImage(dark_image=Image.open(r"pics\back.png"))

#         back_button = ctk.CTkButton(
#             parent,
#             text="",
#             font=("helvetica", 15),
#             command=self.back,
#             width=70, height=25,
#             corner_radius=100,
#             fg_color="#8bceba",
#             image=back_img,
#             text_color="#092928"
#         )
        
#         if row is None:
#             back_button.pack(side=side, padx=padx, pady=pady, anchor=anchor)
#         else:
#             back_button.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, rowspan=rowspan)
#         self.add_hover_effect(back_button)

#     def toggle_fullscreen(self, event=None):
#         # Set the application to fullscreen mode
#         self.attributes('-fullscreen', True)
#         self.bind("<Escape>", self.exit_fullscreen)

#     def exit_fullscreen(self, event=None):
#         width = self.winfo_screenwidth()
#         height = self.winfo_screenheight()
#         # Exit fullscreen mode
#         self.attributes('-fullscreen', False)
#         self.resizable(width=True, height=True)
#         self.geometry(f'{width - 200}x{height-100}')
#         self.maxsize(width,height)
#         # self.minsize(width,height)

#     def initial_screen(self):
#         self.switch_screen(self._initial_screen)

#     def _initial_screen(self):
#         self.image_frame = ctk.CTkFrame(self)
#         self.image_frame.grid(row=0, column=0)

#         self.buttons_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="gainsboro")
#         self.buttons_frame.grid(row=0, column=1, padx=20, pady=(5, 10), ipady=70, ipadx=58)

#         self.bg_image = ctk.CTkImage(dark_image=Image.open("pics\loginscreen_image.png"), size=(350, 510))
#         self.image_label = ctk.CTkLabel(self.image_frame, text="", image=self.bg_image)
#         self.image_label.pack()
        
#         welcome_label = ctk.CTkLabel(
#             self.buttons_frame, 
#             text="Welcome \nTo \nEvent Manager",
#             font=('Segoe UI', 25, "bold"),
#             fg_color="#8bceba",
#             compound="center",
#             # height=20,
#             text_color="white",
#             corner_radius=9,
#         ) 
        
#         welcome_label.pack(
#             pady=(10, 0), 
#             side="top", 
#         )

#         login_button = ctk.CTkButton(
#             self.buttons_frame, 
#             text="Login", 
#             font=("helvetica", 20), 
#             command=lambda: self.login(self.connection), 
#             width=110, height=35, 
#             corner_radius=100, 
#             fg_color="#8bceba", 
#             text_color="#092928",
#         )
        
#         register_button = ctk.CTkButton(
#             self.buttons_frame, 
#             text="Register", 
#             font=("helvetica", 20), 
#             command=lambda: self.register(self.connection), 
#             width=85, height=35, 
#             corner_radius=100, 
#             fg_color="#8bceba", 
#             text_color="#092928"
#         )

#         login_button.pack(pady=(100, 10), side="top")
#         register_button.pack(side="top")

#         # Bind hover events for the buttons
#         self.add_hover_effect(login_button)
#         self.add_hover_effect(register_button)

#     def register(self, connection):
#         self.switch_screen(lambda: self._register_screen(connection))

#     def _register_screen(self, connection):
#         self.image_frame = ctk.CTkFrame(self)
#         self.image_frame.grid(row=0, column=0)

#         self.buttons_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="gainsboro")
#         self.buttons_frame.grid(row=0, column=1, padx=20, pady=(0, 10))

#         self.bg_image = ctk.CTkImage(dark_image=Image.open("pics\loginscreen_image.png"), size=(350, 510))
#         self.image_label = ctk.CTkLabel(self.image_frame, text="", image=self.bg_image)
#         self.image_label.pack()

#         welcome_label = ctk.CTkLabel(
#             self.buttons_frame, 
#             text="Register",
#             font=('Segoe UI.', 25, "bold"),
#             fg_color="#8bceba",
#             compound="center",
#             text_color="white",
#             corner_radius=9,
#         ) 
        
#         welcome_label.grid(
#             pady=(10, 0), 
#             row=0, column=0,
#             columnspan=2,
#             ipady=6,
#             ipadx=10
#         )

#         email_label = ctk.CTkLabel(self.buttons_frame, text="Enter email ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")
#         password_label = ctk.CTkLabel(self.buttons_frame, text="Enter password ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")
#         retype_password_label = ctk.CTkLabel(self.buttons_frame, text="Retype password ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")

#         email_label.grid(row=1, column=0, sticky="w", pady=(50, 10), padx=(20, 10))
#         password_label.grid(row=2, column=0, sticky="w", padx=(20, 10))
#         retype_password_label.grid(row=3, column=0, sticky="w", pady=10, padx=(20, 10))

#         email = ctk.StringVar()
#         password = ctk.StringVar()
#         retype_password = ctk.StringVar()

#         email_field = ctk.CTkEntry(self.buttons_frame, textvariable=email)
#         password_field = ctk.CTkEntry(self.buttons_frame, textvariable=password, show='*')
#         retype_pass_field = ctk.CTkEntry(self.buttons_frame, textvariable=retype_password, show='*')

#         email_field.grid(row=1, column=1, sticky="nsew", pady=(50, 10), padx=(0, 8))
#         password_field.grid(row=2, column=1, sticky="nsew", padx=(0, 8))
#         retype_pass_field.grid(row=3, column=1, sticky="nsew", pady=10, padx=(0, 8))

#         def check(e):
#             if email.get().isdigit() or password.get().isdigit():
#                 showerror("Value Error!", "Please input Characters.")
#             elif email.get() == "" or password.get() == "":
#                 showerror("Value Error!", "Please input Characters.")
#             else:
#                 if password.get() != retype_password.get():
#                     showwarning("Try Again!", "Passwords do not match. Registration failed.")
#                 else:
#                     with connection.cursor() as cursor:
#                         sql = "SELECT * FROM user WHERE user_name = %s"
#                         cursor.execute(sql, (email.get(),))
#                         result = cursor.fetchone()

#                     if result:
#                         showinfo("Registration failed.", "email already exists.")
#                     else:
#                         with connection.cursor() as cursor:
#                             sql = "INSERT INTO user (user_name, password) VALUES (%s, %s)"
#                             cursor.execute(sql, (email.get(), password.get()))
#                             connection.commit()
#                             showinfo("Done!", "Registration successful!\nNow you can Login.")
#                             self.login(self.connection)

#         check_button = ctk.CTkButton(
#             self.buttons_frame, 
#             text="Submit", 
#             command=check,
#             font=("helvetica", 20),
#             width=85, height=35,
#             corner_radius=100,
#             fg_color="#8bceba",
#             text_color="#092928",
#         )
#         check_button.grid(row=4, column=0, columnspan=2, padx=(40, 20), pady=(17, 0))
#         check_button.bind("<Enter>", check)

#         self.add_hover_effect(check_button)

#         self.back_but(self.buttons_frame, row=5, column=0, columnspan=2, padx=(0, 200), pady=(90, 10))

#     def login(self, connection):
#         self.switch_screen(lambda: self._login(connection))

#     def _login(self, connection):
#         self.image_frame = ctk.CTkFrame(self)
#         self.image_frame.grid(row=0,column=0)

#         self.buttons_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="gainsboro")
#         self.buttons_frame.grid(row=0,column=1, padx=20, pady=(0,10),ipadx=3)

#         self.bg_image = ctk.CTkImage(dark_image=Image.open("pics\loginscreen_image.png"), size=(350,510))
#         self.image_label = ctk.CTkLabel(self.image_frame, text="", image=self.bg_image)
#         self.image_label.pack()

#         welcome_label = ctk.CTkLabel(
#             self.buttons_frame, 
#             text="Login",
#             font=('Segoe UI.', 25, "bold"),
#             fg_color="#8bceba",
#             compound="center",
#             text_color="white",
#             corner_radius=9,
#         ) 
        
#         welcome_label.grid(
#             pady=(10, 0), 
#             row=0, column=0,
#             columnspan=2,
#             ipady=8,
#             ipadx=8
#         )

#         email_label = ctk.CTkLabel(self.buttons_frame, text="Enter email ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")
#         password_label = ctk.CTkLabel(self.buttons_frame, text="Enter password ", font=ctk.CTkFont(size=15, weight="bold"), text_color="#092928")

#         email_label.grid(row=1, column=0, sticky="w", pady=(50,10), padx=(20,10))
#         password_label.grid(row=2, column=0, sticky="nsew", padx=(20,10))

#         email = ctk.StringVar()
#         password = ctk.StringVar()

#         email_field = ctk.CTkEntry(self.buttons_frame, textvariable=email)
#         password_field = ctk.CTkEntry(self.buttons_frame, textvariable=password, show='*')

#         email_field.grid(row=1, column=1, pady=(50,10), padx=(0,10))
#         password_field.grid(row=2, column=1, padx=(0,10))

#         def check():
#             if email.get().isdigit() or password.get().isdigit():
#                 showerror("Value Error!", "Please input Characters.")
#             elif email.get() == "" or password.get() == "":
#                 showerror("Value Error!", "Please input Characters.")
#             else:
#                 cursor = connection.cursor()
#                 sql = "SELECT * FROM user WHERE user_name = %s AND password = %s"
#                 cursor.execute(sql, (email.get(), password.get()))
#                 result = cursor.fetchone()

#                 if result:
#                     showinfo("", "Login successful")
#                     self.create_widgets()
#                 else:
#                     msg = showwarning("User Not found", "You have to Sign-Up..")
#                     if msg == 'ok':
#                         self.register(connection)

#         check_button = ctk.CTkButton(
#             self.buttons_frame, 
#             text="Submit", 
#             command=check,
#             font=("helvetica", 20),
#             width=25, height=35,
#             corner_radius=100,
#             fg_color="#8bceba",
#             text_color="#092928",
#             )
#         check_button.grid(row=3, column=0, columnspan=2, padx=(40,20), pady=(17,0))

#         self.add_hover_effect(check_button)
#         self.back_but(self.buttons_frame,row=4, column=0, columnspan=2, padx=(0, 200), pady=(70,10))
        
#     def create_widgets(self):
#         self.switch_screen(self._create_widgets)

#     def _create_widgets(self):
#         self.toggle_fullscreen()
#         self.bind("<F11>", self.toggle_fullscreen)

#         frame2 = ctk.CTkFrame(self, height=30, fg_color=self.bg)
#         frame2.pack(fill="x")

#         labe = ctk.CTkLabel(frame2, text="Event Manager", font=("Segoe UI", 40, "bold"), text_color="white", fg_color=self.secondary_color, corner_radius=12)
#         labe.pack(pady=10, ipady=5,expand=True)

#         # Create a notebook (tabbed interface)
#         notebook = ctk.CTkTabview(self, width=700, height=500, bg_color = "gainsboro", corner_radius=12) #3fa572 #333333
#         notebook.pack(padx=20, pady=20, fill="both", expand=True)
#         # notebook.set(self.event_tab)

#         # Dashboard Tab
#         self.dashboard_tab = notebook.add("Dashboard")
#         self.dashboard_widgets()

#         # Event Management Tab
#         self.event_tab = notebook.add("Event Management")
#         self.eventtab_widgets()

#         # Registration and Ticketing Tab
#         self.ticket_tab = notebook.add("Registration and Ticketing")
#         self.tickettab_widgets()

#         # Reporting and Analytics Tab
#         self.report_tab = notebook.add("Reporting and Analytics")
#         self.reporttab_widgets()

#         # Survey and Feedback Tab
#         self.survey_tab = notebook.add("Survey and Feedback")
#         self.surveytab_widgets()

#         self.xomethin = notebook.add("Something")
#         ctk.CTkLabel(self.xomethin,text="Something")

#     def dashboard_widgets(self):
#         ctk.CTkLabel(self.dashboard_tab, text="Welcome to Your Dashboard!", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

#     def eventtab_widgets(self):
#         # ctk.CTkLabel(self.event_tab, text="Manage your events here", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

#         self.event_widg_frame = ctk.CTkFrame(self.event_tab,height = 41,width = 1300,fg_color = "white")
#         self.event_widg_frame.place(x = 0,y = 0)

#         label1 = ctk.CTkLabel(self.event_widg_frame,text = "cvent",text_color = "black",justify = "right",font = ctk.CTkFont(size =  20,weight = "bold"))
#         label1.place(x = 15,y = 5)

#         label2 = ctk.CTkLabel(self.event_widg_frame,text = "",width = 2,height = 20,fg_color = "black")
#         label2.place(x = 80,y = 9.5)

#         label3 = ctk.CTkLabel(self.event_widg_frame,text = "EVENTS",text_color = "#3fa6fb",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label3.place(x = 95,y = 5)

#         label4 = ctk.CTkLabel(self.event_widg_frame,text = "All Events",text_color = "black",font = ctk.CTkFont(size = 17,weight = "normal"))
#         label4.place(x = 420,y = 5)

#         x1 = tk.StringVar()
#         x1.set("Calendar")
#         opt1 = ctk.CTkComboBox(self.event_widg_frame,variable = x1,height = 35,width = 150,fg_color = "white",text_color = "black",border_color = "white",button_color = "white",button_hover_color = "white",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["Events calendar","Internal calendar"])
#         opt1.place(x = 540,y = 5)

#         x2 = tk.StringVar()
#         x2.set("More")
#         opt2 = ctk.CTkComboBox(self.event_widg_frame,variable = x2,height = 35,width = 150,fg_color = "white",text_color = "black",border_color = "white",button_color = "white",button_hover_color = "white",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
#         opt2.place(x = 700,y = 5)

#         def butimg1():
#             pass

#         img1 = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (20,20))
#         butimg1 = ctk.CTkButton(self.event_widg_frame,image = img1,fg_color = "white",width = 20,text = "",hover_color = "#3fa6fb",command = butimg1)
#         butimg1.place(x = 1040,y = 5)

#         def butimg2():
#             pass 

#         img2 = ctk.CTkImage(dark_image = Image.open(r"pics\file.png"),size = (20,20))
#         butimg2 = ctk.CTkButton(self.event_widg_frame,image = img2,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg2)
#         butimg2.place(x = 1090,y = 5)

#         def butimg3():
#             pass

#         img3 = ctk.CTkImage(dark_image = Image.open(r"pics\question.png"),size = (20,20))
#         butimg3 = ctk.CTkButton(self.event_widg_frame,image = img3,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg3)
#         butimg3.place(x = 1140,y = 5)

#         def butimg4():
#             pass

#         img4 = ctk.CTkImage(dark_image = Image.open(r"pics\user (1).png"),size = (20,20))
#         butimg4 = ctk.CTkButton(self.event_widg_frame,image = img4,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg4)
#         butimg4.place(x = 1190,y = 5)

#         def butimg5():
#             pass

#         img5 = ctk.CTkImage(dark_image = Image.open(r"pics\menu.png"),size = (20,20))
#         butimg5 = ctk.CTkButton(self.event_widg_frame,image = img5,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg5)
#         butimg5.place(x = 1240,y = 5)

#         self.canvas1 = tk.Canvas(self.event_tab,height = 3,width = 1920,bg = "#0061ff",relief = tk.RAISED)
#         self.canvas1.place(x = 0,y = 56)

#         self.label15 = ctk.CTkLabel(self.event_tab,text = "Events",text_color = "#000000",font = ctk.CTkFont(size = 20,weight = "bold"))
#         self.label15.place(x = 15,y = 65)


#         self.create_event_button = ctk.CTkButton(self.event_tab,text = "Create Event",height = 30,width = 40,fg_color = "#2380D2",text_color = "#ffffff",corner_radius = 7,command = self.create_event)
#         self.create_event_button.place(x = 1140,y = 65)

#         self.main_frame = ctk.CTkFrame(self.event_tab,height = 520,width = 1280,fg_color = "#E6E6E6")
#         self.main_frame.place(x = 0,y = 130)

#         x3 = tk.StringVar()
#         x3.set("Current Events")
#         current_events_opt = ctk.CTkComboBox(self.main_frame,variable = x3,height = 35,width = 140,fg_color = "#E6E6E6",text_color = "black",button_color = "#E6E6E6",border_color = "#E6E6E6",button_hover_color = "#E6E6E6",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
#         current_events_opt.place(x = 30,y = 30)

#         def create_view():
#             pass

#         create_view_button = ctk.CTkButton(self.main_frame,text = "Create View",text_color = "#000000",hover_color = "#A4A4A4",width = 100,fg_color = "#E6E6E6",command = create_view)
#         create_view_button.place(x = 180,y = 35)

#         advanced_search_label = ctk.CTkLabel(self.main_frame,text = "Advanced Search",text_color = "#000000")
#         advanced_search_label.place(x = 1140,y = 35)

#         child_frame = ctk.CTkFrame(self.main_frame,fg_color = "#ffffff",height = 250,width = 1235)
#         child_frame.place(x = 20,y = 130)

#         inner_frame1 = ctk.CTkFrame(child_frame,height = 130,width = 1175,fg_color = "#ffffff",border_width = 0.8,border_color = "#919191")
#         inner_frame1.place(x = 30,y = 20)

#         title_label = ctk.CTkLabel(inner_frame1,text = "Title",text_color = "#000000",font = ctk.CTkFont(size = 14,weight = "normal"))
#         title_label.place(x = 20,y = 10)

#         x4 = tk.StringVar()
#         x4.set("Code")
#         code_dropdown = ctk.CTkComboBox(inner_frame1,variable = x4,height = 35,width = 100,fg_color = "#ffffff",text_color = "#000000",button_color = "#ffffff",border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
#         code_dropdown.place(x = 450,y = 10)

#         x5 = tk.StringVar()
#         x5.set("Event Status")
#         event_status_dropdown = ctk.CTkComboBox(inner_frame1,variable = x5,height = 35,width = 140,fg_color = "#ffffff",text_color = "#000000",button_color = "#ffffff",border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
#         event_status_dropdown.place(x = 590,y = 10)

#         x6 = tk.StringVar()
#         x6.set("Start Date")
#         start_date_dropdown = ctk.CTkComboBox(inner_frame1,variable = x6,height = 35,width = 140,fg_color = "#ffffff",text_color = "#000000",button_color = "#ffffff",border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
#         start_date_dropdown.place(x = 750,y = 10)

#         x7 = tk.StringVar()
#         x7.set("Yes")
#         yes_dropdown = ctk.CTkComboBox(inner_frame1,variable = x7,height = 35,width = 90,fg_color = "#ffffff",text_color = "#000000",button_color = "#ffffff",border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
#         yes_dropdown.place(x = 920,y = 10)

#         img6 = ctk.CTkImage(dark_image = Image.open(r"pics\question.png"),size = (20,20))
#         labimg6 = ctk.CTkLabel(inner_frame1,image = img6,text = "")
#         labimg6.place(x = 1050,y = 10)

#         no_label = ctk.CTkLabel(inner_frame1,text = "No",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
#         no_label.place(x = 1090,y = 10)

#         canvas2 = tk.Canvas(inner_frame1,height = 3,width = 1900,bg = "#858585",relief = tk.SUNKEN)
#         canvas2.place(x =  -2,y = 70)

#         inner_frame2 = ctk.CTkFrame(inner_frame1,height = 78,width = 1172,fg_color = "#E6E6E6")
#         inner_frame2.place(x = 1,y = 50)

#         x8 = tk.StringVar()
#         text = "There are no events in this view."
#         x8.set(text)
#         data_label = ctk.CTkLabel(inner_frame2,text_color = "#000000",textvariable = x8,font = ctk.CTkFont(size = 15,weight = "bold"))
#         data_label.place(x = 500,y = 10)

#         result_per_page_label = ctk.CTkLabel(child_frame,text = "Results per page",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 13,weight = "normal"))
#         result_per_page_label.place(x = 30,y = 170)

#         x9 = tk.IntVar()
#         result_per_page_dropdown = ctk.CTkComboBox(child_frame,variable = x9,height = 35,width = 60,fg_color = "#ffffff",text_color = "#000000",border_width = 0.6,button_color = "#ffffff",corner_radius = 5,border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["25","30","35","40"])
#         result_per_page_dropdown.place(x = 180,y = 170)

#         x10 = tk.StringVar()
#         text = "Displaying result 0 of 0"
#         x10.set(text)
#         displaying_result_label = ctk.CTkLabel(child_frame,textvariable = x10,text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
#         displaying_result_label.place(x = 600,y = 170)

#         down_line = tk.Canvas(self.main_frame,height = 9,width = 1920,bg = "#858585",relief = tk.SUNKEN)
#         down_line.place(x = -2,y = 768)


#     def create_event(self):
#         self.event_widg_frame.destroy()
#         self.main_frame.destroy()
#         self.canvas1.destroy()
#         self.create_event_button.destroy()
#         self.label15.destroy()

#         my_img = ctk.CTkImage(dark_image = Image.open(r"pics\back.png"),size = (20,20))
#         self.cvent_labimg = ctk.CTkButton(self.event_tab,image = my_img,text = "",fg_color = "#F0F0F0",hover_color = "white",width = 15,border_width = 1,border_color = "#F0F0F0", command=self.back)
#         self.cvent_labimg.place(x = 8,y = 5)

#         self.cvent_l1 = ctk.CTkLabel(self.event_tab,text = "New event",font = ("bold",26)) #,text_color = "black",fg_color = "#F0F0F0",
#         self.cvent_l2 = ctk.CTkLabel(self.event_tab,text = "Great! Tell us a little about your event.",font = ("thin",19)) #,text_color = "black",fg_color = "#F0F0F0"
#         self.cvent_l1.place(x = 70,y = 30)
#         self.cvent_l2.place(x = 70,y = 57)

#         self.cvent_scrollable_frame = ctk.CTkScrollableFrame(self.event_tab,height = 470,width = 800,orientation = "vertical",fg_color = "white",border_width = 0.8,border_color = "black",scrollbar_button_color = "white",scrollbar_fg_color = "black")
#         self.cvent_frame = ctk.CTkFrame(self.cvent_scrollable_frame,fg_color = "white",height = 950,width = 800)
#         self.cvent_scrollable_frame.place(x = 70,y = 105)
#         self.cvent_frame.pack(expand=True)

#         img1 = ctk.CTkImage(dark_image = Image.open(r"pics\info.png"),size = (30,30))
#         labimg1 = ctk.CTkLabel(self.cvent_frame,image = img1,text = "")
#         labimg1.place(x = 30,y = 9)

#         l3 = ctk.CTkLabel(self.cvent_frame,text = "Basic Information",text_color = "black",font = ("darkbold",23))
#         l4 = ctk.CTkLabel(self.cvent_frame,text = "* Event Title",text_color = "black",font = ("thin",19))
#         l3.place(x = 67,y = 9)
#         l4.place(x = 30,y = 50)

#         def check_x1():
#             if x1.get() == "":
#                 showerror(title = "Error",message = "Please input Event Title")

#             if x2.get() == "":
#                 showerror(title = "Error",message = "Please choose Event Category")
            
#             if x6.get() == "":
#                 showerror(title = "Error",message = "Please input your last name")

#             if x7.get() == "":
#                 showerror(title = "Error",message = "Please input your Email")

#             if x8.get() == "":
#                 showerror(title = "Error",message = "Please input full Format")

#             if x10.get() == "":
#                 showerror(title = "Error",message = "Please input full format")

#             if x14.get() == "":
#                 showerror(title = "Error",message = "Please choose the state")
#             self.events_home()


#         x1 =ctk.StringVar()
#         e1 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 690,textvariable = x1)
#         l5 = ctk.CTkLabel(self.cvent_frame,text = "* Event Category",text_color = "black",font = ("thin",19))
#         e1.place(x = 30,y = 82)
#         l5.place(x = 30,y = 128)

#         x2 =ctk.StringVar()
#         opt1 = ctk.CTkComboBox(self.cvent_frame,variable = x2,height = 35,width = 200,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["Educational","Business","Sports"])
#         opt1.place(x = 30,y = 165)

#         l6 = ctk.CTkLabel(self.cvent_frame,text = "Language",text_color = "black",font = ("thin",19))
#         l6.place(x = 280,y = 128)
#         x3 =ctk.StringVar()

#         opt2 =  ctk.CTkComboBox(self.cvent_frame,variable = x3,height = 35,width = 200,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["English","Spanish","Hindi"])
#         opt2.place(x = 280,y = 165)
#         l7 = ctk.CTkLabel(self.cvent_frame,text = "Locale",text_color = "black",font = ("thin",19))
#         l7.place(x = 520,y = 128)

#         x4 =ctk.StringVar()
#         opt3 =  ctk.CTkComboBox(self.cvent_frame,variable = x4,height = 35,width = 200,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["USA","INDIA","CANADA"])
#         opt3.place(x = 520,y = 165)
#         l8 = ctk.CTkLabel(self.cvent_frame,text = "* Planner First Name",text_color = "black",font = ("thin",19))
#         l8.place(x = 30,y = 220)

#         x5 =ctk.StringVar()
#         e2 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x5)
#         e2.place(x = 30,y = 250)
#         l9 = ctk.CTkLabel(self.cvent_frame,text = "* Last Name",text_color = "black",font = ("thin",19))
#         l9.place(x = 280,y = 220)

#         x6 =ctk.StringVar()
#         e3 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x6)
#         e3.place(x = 280,y = 250)
#         label1 = ctk.CTkLabel(self.cvent_frame,text = "* Planner Email",text_color = "black",font = ("thin",19))
#         label1.place(x = 520,y = 220)

#         x7 =ctk.StringVar()
#         e4 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x7)
#         e4.place(x = 520,y = 250)

#         img5 = ctk.CTkImage(dark_image = Image.open(r"pics\management.png"),size = (340,280))
#         self.cvent_labimg5 = ctk.CTkLabel(self.event_tab,image = img5,text = "")
#         self.cvent_labimg5.place(x = 940,y = 130)

#         self.label2 = ctk.CTkLabel(self.event_tab,text = "This is just the start..!!",text_color = "black",fg_color = "#F0F0F0",font = ("semibold",21))
#         self.label2.place(x = 940,y = 420)
#         self.label3 = ctk.CTkLabel(self.event_tab,text = "We can't wait to see what kind of event you put on!",text_color = "black",fg_color = "#F0F0F0",font = ("thin",16))
#         self.label3.place(x = 940,y = 450)

#         img2 = ctk.CTkImage(dark_image = Image.open(r"pics\location.png"),size = (30,30))
#         labimg2 = ctk.CTkLabel(self.cvent_frame,image = img2,text = "")
#         labimg2.place(x = 30,y = 310)

#         label4 = ctk.CTkLabel(self.cvent_frame,text = "Location",text_color = "black",fg_color = "white",font = ("darkbold",23))
#         label4.place(x = 67,y = 310)
#         label5 = ctk.CTkLabel(self.cvent_frame,text = "* Format",text_color = "black",font = ("thin",19))
#         label5.place(x = 30,y = 352)

#         x8 =ctk.StringVar()
#         e5 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x8)
#         e5.place(x = 30,y = 394)

#         x9 =ctk.StringVar()
#         e6 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x9)
#         e6.place(x = 280,y = 394)

#         x10 =ctk.StringVar()
#         e7 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x10)
#         e7.place(x = 520,y = 394)

#         label6 = ctk.CTkLabel(self.cvent_frame,text = "Venue",text_color = "black",font = ("thin",19))
#         label6.place(x = 30,y = 436)

#         x11 =ctk.StringVar()
#         e8 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 690,textvariable = x11)
#         e8.place(x = 30,y = 478)

#         img3 = ctk.CTkImage(dark_image = Image.open(r"pics\close.png"),size = (20,20))
#         self.cvent_labimg3 = ctk.CTkButton(self.event_tab,image = img3,text = "",fg_color = "#F0F0F0",hover_color = "white",width = 15,border_width = 1,border_color = "#F0F0F0")
#         self.cvent_labimg3.place(x = 1225,y = 5)

#         img4 = ctk.CTkImage(dark_image = Image.open(r"pics\mall.png"),size = (20,20))
#         labimg4 = ctk.CTkLabel(e8,image = img4,text = "")
#         labimg4.place(x = 653,y = 3)

#         label7 = ctk.CTkLabel(self.cvent_frame,text = "Address",text_color = "black",font = ("thin",19))
#         label7.place(x = 30,y = 520)

#         x12 =ctk.StringVar()
#         e9 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 690,textvariable = x12)
#         e9.place(x = 30,y = 562)

#         label8 = ctk.CTkLabel(self.cvent_frame,text = "City",text_color = "black",font = ("thin",19))
#         label8.place(x = 30,y = 604)

#         x13 =ctk.StringVar()
#         e10 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x13)
#         e10.place(x = 30,y = 646)

#         label9 = ctk.CTkLabel(self.cvent_frame,text = "* State",text_color = "black",font = ("thin",19))
#         label9.place(x = 205,y = 604)

#         x14 =ctk.StringVar()
#         opt4 = ctk.CTkComboBox(self.cvent_frame,variable = x14,height = 35,width = 145,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["Maharashtra","Rajasthan","Uttar Pradesh","Gujarat","Punjab"])
#         opt4.place(x = 205,y = 646)

#         label10 = ctk.CTkLabel(self.cvent_frame,text = "ZIP/Postal code",text_color = "black",font = ("thin",19))
#         label10.place(x = 375,y = 604)

#         x15 =ctk.StringVar()
#         e11 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x15)
#         e11.place(x = 375,y = 646)

#         label11 = ctk.CTkLabel(self.cvent_frame,text = "Country",text_color = "black",font = ("thin",19))
#         label11.place(x = 540,y = 604)

#         x16 =ctk.StringVar()
#         opt5 = ctk.CTkComboBox(self.cvent_frame,variable = x16,height = 35,width = 145,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["India","New Zealand","USA","Russia"])
#         opt5.place(x = 540,y = 646)

#         img6 = ctk.CTkImage(dark_image = Image.open(r"pics\calendar.png"),size = (30,30))
#         labimg6 = ctk.CTkLabel(self.cvent_frame,image = img6,text = "")
#         labimg6.place(x = 30,y = 692)

#         label12 = ctk.CTkLabel(self.cvent_frame,text = "Event Dates",text_color = "black",font = ("darkbold",23))
#         label12.place(x = 67,y = 692)

#         label13 = ctk.CTkLabel(self.cvent_frame,text = "Start Date",text_color = "black",font = ("thin",19))
#         label13.place(x = 30,y = 732)

#         x17 =ctk.StringVar()
#         e12 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x17)
#         e12.place(x = 30,y = 768)

#         label14 = ctk.CTkLabel(self.cvent_frame,text = "Start Time",text_color = "black",font = ("thin",19))
#         label14.place(x = 205,y = 732)

#         x18 =ctk.StringVar()
#         e13 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x18)
#         e13.place(x = 205,y = 768)

#         label15 = ctk.CTkLabel(self.cvent_frame,text = "End Date",text_color = "black",font = ("thin",19))
#         label15.place(x = 375,y = 732)

#         x19 =ctk.StringVar()
#         e14 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x19)
#         e14.place(x = 375,y = 768)

#         label16 = ctk.CTkLabel(self.cvent_frame,text = "End Time",text_color = "black",font = ("thin",19))
#         label16.place(x = 540,y = 732)

#         x20 =ctk.StringVar()
#         e15 = ctk.CTkEntry(self.cvent_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x20)
#         e15.place(x = 540,y = 768)

#         img7 = ctk.CTkImage(dark_image = Image.open(r"pics\calendar (1).png"),size = (30,30))
#         labimg7 = ctk.CTkLabel(e12,image = img7,text = "")
#         labimg7.place(x = 105,y = 2)

#         labimg8 = ctk.CTkLabel(e14,image = img7,text = "")
#         labimg8.place(x = 105,y = 2)

#         label17 = ctk.CTkLabel(self.cvent_frame,text = "Time Zone",text_color = "black",font = ("thin",19))
#         label17.place(x = 30,y = 810)

#         x21 =ctk.StringVar()
#         opt6 = ctk.CTkComboBox(self.cvent_frame,variable = x21,height = 35,width = 690,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["(GMT+05:30) India","(GMT+09:05) USA","(GMT-03:40) New Zealand"])
#         opt6.place(x = 30,y = 850)

#         b1 = ctk.CTkButton(self.cvent_frame,text = "Submit",height = 40,width = 170,corner_radius =10,fg_color = "lightgreen",text_color = "black",command = check_x1)
#         b1.place(x = 300,y = 904)

#     def create_sidebar_item(self, label, subitems):
#         self.frame = ctk.CTkFrame(self.f3, corner_radius=0)
#         self.frame.pack(fill="x", pady=(0, 1))

#         # Create a sub-frame for the button content
#         button_frame = ctk.CTkFrame(self.frame, corner_radius=0, fg_color="#20807f")
#         button_frame.pack(fill="x")

#         # Label on the left
#         label_widget = ctk.CTkButton(button_frame, text=label, anchor="w", command= lambda : self.toggle_subitems(self.frame, label, subitems), fg_color="#20807f", text_color="white")
#         label_widget.pack(side="left")

#         # Arrow on the right
#         self.arrow_label = ctk.CTkLabel(button_frame, text="▼", anchor="e")
#         self.arrow_label.pack(side="right",padx=(0,5))

#         # Make the whole frame clickable
#         button_frame.bind("<Button-1>", lambda event: self.toggle_subitems(self.frame, label, subitems))

#         # Create hidden frame for subitems
#         self.subframe = ctk.CTkFrame(self.frame, corner_radius=20, fg_color="#093838")
#         self.subframe.pack(fill="x")
#         self.subframe.pack_forget()  # Initially hidden

#     # Create buttons for subitems
#         for item in subitems:
#             sub_button = ctk.CTkButton(self.subframe, text=f"  • {item}", anchor="w", fg_color="transparent", hover_color=("gray70", "gray30"), text_color="white")
#             sub_button.pack(fill="x")

#     def toggle_subitems(self, parent_frame, label, subitems):
#         self.subframe = parent_frame.winfo_children()[1]  # The subframe
#         self.arrow_label = parent_frame.winfo_children()[0].winfo_children()[1]  # The arrow label
        
#         if self.subframe.winfo_viewable():
#             self.subframe.pack_forget()
#             self.arrow_label.configure(text="▼")
#         else:
#             self.subframe.pack(fill="x")
#             self.arrow_label.configure(text="▲")

#     def events_home(self):
#         self.cvent_frame.destroy()
#         self.cvent_l1.destroy()
#         self.cvent_l2.destroy()
#         self.cvent_labimg.destroy()
#         self.cvent_labimg3.destroy()
#         self.cvent_labimg5.destroy()
#         self.cvent_scrollable_frame.destroy()

#         f1 = ctk.CTkFrame(self.event_tab,height = 41,width = 1300,fg_color = "white")
#         f1.place(x = 0,y = 0)

#         label1 = ctk.CTkLabel(f1,text = "cvent",text_color = "black",justify = "right",font = ctk.CTkFont(size =  20,weight = "bold"))
#         label1.place(x = 15,y = 5)

#         label2 = ctk.CTkLabel(f1,text = "",width = 2,height = 20,fg_color = "black")
#         label2.place(x = 80,y = 9.5)

#         label3 = ctk.CTkLabel(f1,text = "EVENTS",text_color = "#3fa6fb",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label3.place(x = 95,y = 5)

#         label4 = ctk.CTkLabel(f1,text = "All Events",text_color = "black",font = (ctk.CTkFont(size = 17,weight = "normal")))
#         label4.place(x = 420,y = 5)

#         x1 =ctk.StringVar()
#         x1.set("Calendar")
#         opt1 = ctk.CTkComboBox(f1,variable = x1,height = 35,width = 100,fg_color = "white",text_color = "black",border_color = "white",button_color = "white",button_hover_color = "white",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["2020","2021","2022","2023"])
#         opt1.place(x = 540,y = 5)

#         x2 =ctk.StringVar()
#         x2.set("More")
#         opt2 = ctk.CTkComboBox(f1,variable = x2,height = 35,width = 90,fg_color = "white",text_color = "black",border_color = "white",button_color = "white",button_hover_color = "white",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
#         opt2.place(x = 670,y = 5)

#         def butimg1():
#             pass

#         img1 = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (20,20))
#         butimg1 = ctk.CTkButton(f1,image = img1,fg_color = "white",width = 20,text = "",hover_color = "#3fa6fb",command = butimg1)
#         butimg1.place(x = 1040,y = 5)

#         def butimg2():
#             pass 

#         img2 = ctk.CTkImage(dark_image = Image.open(r"pics\file.png"),size = (20,20))
#         butimg2 = ctk.CTkButton(f1,image = img2,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg2)
#         butimg2.place(x = 1090,y = 5)

#         def butimg3():
#             pass

#         img3 = ctk.CTkImage(dark_image = Image.open(r"pics\question.png"),size = (20,20))
#         butimg3 = ctk.CTkButton(f1,image = img3,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg3)
#         butimg3.place(x = 1140,y = 5)

#         def butimg4():
#             pass

#         img4 = ctk.CTkImage(dark_image = Image.open(r"pics\user (1).png"),size = (20,20))
#         butimg4 = ctk.CTkButton(f1,image = img4,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg4)
#         butimg4.place(x = 1190,y = 5)

#         def butimg5():
#             pass

#         img5 = ctk.CTkImage(dark_image = Image.open(r"pics\menu.png"),size = (20,20))
#         butimg5 = ctk.CTkButton(f1,image = img5,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg5)
#         butimg5.place(x = 1240,y = 5)

#         canvas1 = tk.Canvas(self.event_tab,height = 3,width = 1920,bg = "#0061ff",relief = "raised")
#         canvas1.place(x = 0,y = 56)

#         self.f2 = ctk.CTkFrame(self.event_tab,height = 44,width = 1300,fg_color = self.secondary_color)
#         self.f2.place(x = 0,y = 41)

#         def menu_animation(): # MENU ANIMATION COMMAND ...
#             self.click_count += 1

#             if self.click_count % 2 != 0 :
#                 self.after(1, animate(250,82, 0.808))
#                 self.f3 = ctk.CTkScrollableFrame(self.event_tab,bg_color = "red",height = 600,width = 240,border_width = 1,border_color = "lightgray") 
#                 self.f3.place(x = 0,y = 81)

#                 self.create_sidebar_item("General", ["Option 1", "Option 2"])
#                 self.create_sidebar_item("Registration", ["Register", "Unregister"])
#                 self.create_sidebar_item("Marketing", ["Campaigns", "Analytics"])
#                 self.create_sidebar_item("Email", ["Compose", "Inbox", "Sent"])
#                 self.create_sidebar_item("Attendees", ["List", "Groups"])
#                 self.create_sidebar_item("Surveys", ["Feedback Surveys", "Responses"])
#                 self.create_sidebar_item("Reports", ["Generate", "View"])
#                 self.create_sidebar_item("Integrations", ["Connect", "Manage"])
#             else:
#                 if self.f3 is not None:
#                     self.f3.destroy()
#                     self.f3 = None
#                 self.f0.place(x=0, y=82,relwidth=1.0)

#         def animate(x,y,relwidth=None):
#             self.f0.place(x=x, y=y, relwidth=relwidth)
            

#         img6 = ctk.CTkImage(dark_image = Image.open(r"pics\lines.png"),size = (20,20))
#         butimg6 = ctk.CTkButton(self.f2,image = img6,text = "",fg_color = "white",width = 20,hover_color = "white",command = menu_animation)
#         butimg6.place(x = 6,y = 5)

#         label5 = ctk.CTkLabel(self.f2,text = "DemEven",text_color = "black",font = (ctk.CTkFont(size = 15,weight = "normal")))
#         label5.place(x = 47,y = 5)

#         x3 =ctk.StringVar()
#         e1 = ctk.CTkEntry(self.f2,height = 28,width = 250,fg_color = "white",corner_radius = 15,placeholder_text = "Search this Event",placeholder_text_color = "gray",text_color = "black",textvariable = x3)
#         e1.place(x = 1000,y = 5)

#         def butimg7():
#             pass

#         img7 = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (20,15))
#         butimg7 = ctk.CTkButton(self.f2,image = img7,text = "",fg_color = "white",width = 20,border_width = 1,border_color = "black",hover_color = "#8BFAFF",command = butimg7)
#         butimg7.place(x = 958,y = 5)

# #-----------------------

#         self.f0 = ctk.CTkScrollableFrame(self.event_tab,height = 700,fg_color = "#F0F0F0")
#         self.f0.place(x = 0,y = 82, relwidth=1.0)

#         f01 = ctk.CTkFrame(self.f0,height = 1050,width = 970,fg_color = "#F0F0F0")
#         f01.grid(row = 0,column = 0)

#         f4 = ctk.CTkFrame(f01,height = 200,width = 970,fg_color = "#ffffff")
#         f4.place(x = 0,y = 0)

#         label7 = ctk.CTkLabel(f4,text = "DemEven",fg_color = "white",text_color = "black",font = ctk.CTkFont(size = 25,weight = "bold"))
#         label7.place(x = 20,y = 80)

#         label8 = ctk.CTkLabel(f4,text = "Upcoming",fg_color = "#FEEEAB",text_color = "#EB9E29",corner_radius = 3,height = 10,width = 10,padx = 2,pady = 2)
#         label8.place(x = 20,y = 140)

#         img8 = ctk.CTkImage(dark_image = Image.open(r"pics\calendar.png"),size = (20,20))
#         labimg8 = ctk.CTkLabel(f4,image = img8,text = "")
#         labimg8.place(x = 120,y = 137)

#         label9 = ctk.CTkLabel(f4,text = "30/7/2024  6:00 pm - 10:00 pm  IST (61 days away)",text_color = "black",font = ctk.CTkFont(size = 13,weight = "normal"))
#         label9.place(x = 150,y = 137)

#         img9 = ctk.CTkImage(dark_image = Image.open(r"pics\location.png"),size = (20,20))
#         labimg9 = ctk.CTkLabel(f4,image = img9,text = "")
#         labimg9.place(x = 500,y = 137)

#         label10 = ctk.CTkLabel(f4,text = "Chicago",text_color = "black",font = ctk.CTkFont(size = 13,weight = "normal"))
#         label10.place(x = 522,y = 137)

#         x9 =ctk.StringVar()
#         x9.set("Actions")
#         opt8 = ctk.CTkComboBox(f4,height = 35,width = 150,variable = x9,fg_color = "white",button_hover_color = "#4B9EFC",border_width = 1,border_color = "lightgray",corner_radius = 7,dropdown_hover_color = "#4B9EFC",button_color = "lightgray",text_color = "#0966F1",values = ["","","",""])
#         opt8.place(x = 800,y = 96)

#         img10 = ctk.CTkImage(dark_image = Image.open(r"pics\light-bulb.png"),size = (50,50))
#         labimg10 = ctk.CTkLabel(self.f0,image = img10,text = "")
#         labimg10.place(x = 8,y = 205)

#         label11 = ctk.CTkLabel(self.f0,text = "Up next for your event",text_color = "black",font = ctk.CTkFont(size = 18,weight = "bold"))
#         label11.place(x = 50,y = 215)

#         f5 = ctk.CTkFrame(f01,height = 150,width = 265,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
#         f5.place(x = 8,y = 255)

#         img11 = ctk.CTkImage(dark_image = Image.open(r"pics\features.png"),size = (38,38))
#         labimg11 = ctk.CTkLabel(f5,image = img11,text = "")
#         labimg11.place(x = 15,y = 48)

#         label12 = ctk.CTkLabel(f5,text = "Add Event Features",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label12.place(x = 75,y = 20)

#         label13 = ctk.CTkLabel(f5,text = "Make sure you have all the\nfeatures you need for your event",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
#         label13.place(x = 75,y = 55)

#         def funbut1():
#             pass

#         button1 = ctk.CTkButton(f5,text = "Add features",corner_radius = 5,border_width = 1,width = 6,hover_color = "lightgray",border_color = "#3fa6fb",fg_color = "#ffffff",border_spacing = 3,text_color = "#3fa6fb",command = funbut1)
#         button1.place(x = 75,y = 100)

#         def skip1():
#             pass

#         button2 = ctk.CTkButton(f5,text = "Skip",width = 6,fg_color = "#ffffff",text_color = "#3fa6fb",hover_color = "#ffffff",command = skip1)
#         button2.place(x = 185,y = 100)

#         f6 = ctk.CTkFrame(f01,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
#         f6.place(x = 290,y = 255)

#         img12 = ctk.CTkImage(dark_image = Image.open(r"pics\registration.png"),size = (42,38))
#         labimg12 = ctk.CTkLabel(f6,image = img12,text = "")
#         labimg12.place(x = 15,y = 48)

#         label14 = ctk.CTkLabel(f6,text = "Set up registration types",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label14.place(x = 45,y = 20)

#         label15 = ctk.CTkLabel(f6,text = "Add registration types to\ncustomize the registration...",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
#         label15.place(x = 75,y = 55)

#         def funbut2():
#             pass

#         button3 = ctk.CTkButton(f6,text = "Get Started",corner_radius = 5,border_width = 1,width = 6,hover_color = "lightgray",border_color = "#3fa6fb",fg_color = "#ffffff",border_spacing = 3,text_color = "#3fa6fb",command = funbut2)
#         button3.place(x = 75,y = 100)

#         def skip2():
#             pass

#         button4 = ctk.CTkButton(f6,text = "Skip",width = 6,fg_color = "#ffffff",text_color = "#3fa6fb",hover_color = "#ffffff",command = skip2)
#         button4.place(x = 185,y = 100)

#         label16 = ctk.CTkLabel(f01,text = "Event Overview",text_color = "black",font = ctk.CTkFont(size = 18,weight = "bold"))
#         label16.place(x = 8,y = 420)

#         f7 = ctk.CTkFrame(f01,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
#         f7.place(x = 8,y = 460)

#         label17 = ctk.CTkLabel(f7,text = "Registration",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label17.place(x = 20,y = 20)

#         label18 = ctk.CTkLabel(f7,text = "Invitee Conversion Rate",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
#         label18.place(x = 20,y = 50)

#         label19 =  ctk.CTkLabel(f7,text = "0.0%",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label19.place(x = 20,y = 75)

#         img13 = ctk.CTkImage(dark_image = Image.open(r"pics\light-bulb.png"),size = (30,30))
#         labimg13 = ctk.CTkLabel(f7,image = img13,text = "")
#         labimg13.place(x = 15,y = 105)

#         label20 = ctk.CTkLabel(f7,text = "Set your event's deadline\nand capacity",text_color = "#3fa6fb",font = ctk.CTkFont(size = 12,weight = "normal"))
#         label20.place(x = 60,y = 105)

#         def butimg14():
#             pass 

#         img14 = ctk.CTkImage(dark_image = Image.open(r"pics\ellipsis.png"),size = (30,20))
#         butimg14 = ctk.CTkButton(f7,image = img14,text = "",command = butimg14,width = 20,fg_color = "#ffffff",hover_color = "#ffffff")
#         butimg14.place(x = 220,y = 20)

#         f8 = ctk.CTkFrame(f01,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
#         f8.place(x = 290,y = 460)

#         label21 = ctk.CTkLabel(f8,text = "Emails",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label21.place(x = 20,y = 20)

#         label22 = ctk.CTkLabel(f8,text = "Email sent",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
#         label22.place(x = 20,y = 50)

#         label23 =  ctk.CTkLabel(f8,text = "0",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label23.place(x = 20,y = 75)

#         labimg15 = ctk.CTkLabel(f8,image = img13,text = "")
#         labimg15.place(x = 15,y = 105)

#         label24 = ctk.CTkLabel(f8,text = "Add any custom data tags you\nneed for your event",text_color = "#3fa6fb",font = ctk.CTkFont(size = 12,weight = "normal"))
#         label24.place(x = 60,y = 105)
        
#         def butimg15():
#             pass

#         img15 = ctk.CTkImage(dark_image = Image.open(r"pics\ellipsis.png"),size = (30,20))
#         butimg15 = ctk.CTkButton(f8,image = img15,text = "",command = butimg15,width = 20,fg_color = "#ffffff",hover_color = "#ffffff")
#         butimg15.place(x = 220,y = 20)
        
#         f02 = ctk.CTkFrame(self.f0,height = 730,width = 290,fg_color = "gainsboro",corner_radius=12)
#         f02.grid(row=0,column=1, padx=12, sticky="n")

#         def butimg16():
#             pass 

#         img16 = ctk.CTkImage(dark_image = Image.open(r"pics\right-arrow.png"),size = (30,30))
#         butimg16 = ctk.CTkButton(f02,image = img16,text = "",command = butimg16,fg_color = "#C8C6F3",hover_color = "#ffffff",width = 20)
#         butimg16.place(x = 400,y = 0)

#         label25 = ctk.CTkLabel(f02,text = "Feature Status",text_color = "black",font = ctk.CTkFont(size = 17,weight = "bold"), corner_radius = 9, fg_color="#F0F0F0")
#         label25.place(x = 15,y = 30)

#         img17 = ctk.CTkImage(dark_image = Image.open(r"pics\pending.png"),size = (20,20))
#         labimg17 = ctk.CTkLabel(f02,image = img17,text = "")
#         labimg17.place(x = 165,y = 30)

#         label26 = ctk.CTkLabel(f02,text = "Registration",text_color = "black", font = ctk.CTkFont(size = 19,weight = "normal"))
#         label26.place(x = 19,y = 60)

#         label27 = ctk.CTkLabel(f02,text = "Pending",text_color = "black",corner_radius = 19,height = 10,width = 10,padx = 2,pady = 2,font = ctk.CTkFont(size = 19))
#         label27.place(x = 350,y = 80)

#         label28 = ctk.CTkLabel(f02,text = "Search for attendees",text_color = "black",fg_color = "#F0F0F0",font = ctk.CTkFont(size = 17,weight = "bold"), corner_radius = 9, width=262)
#         label28.place(x = 15,y = 110)

#         x10 = tk.StringVar()
#         e2 = ctk.CTkEntry(f02,height = 30,width = 257,corner_radius = 15,fg_color = "#ffffff",text_color = "black",placeholder_text = "Enter a name or email",placeholder_text_color = "black",textvariable = x10)
#         e2.place(x = 18,y = 150)

#         canvas3 =  tk.Canvas(f02,height = 3,width = 262,bg = "gray",relief = tk.RAISED)
#         canvas3.place(x = 15,y = 215)

#         def butimg18():
#             pass 

#         img18 = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (10,10))
#         butimg18 = ctk.CTkButton(e2,image = img7,text = "",fg_color = "white",hover_color = "#ffffff",corner_radius = 3,height = 10,width = 10,command = butimg18)
#         butimg18.place(x = 218,y = 3)

#         label29 = ctk.CTkLabel(f02,text = "Event Information",text_color = "black",fg_color = "#F0F0F0",font = ctk.CTkFont(size = 17,weight = "bold"), corner_radius = 9, width=262)
#         label29.place(x = 15,y = 260)

#         label30 = ctk.CTkLabel(f02,text = "Event Code",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
#         label30.place(x = 15,y = 310)

#         x11 = tk.StringVar()
#         x11.set("BAMMCYD")
#         label31 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x11,font = ctk.CTkFont(size = 12,weight = "bold"))
#         label31.place(x = 22,y = 340)

#         label32 = ctk.CTkLabel(f02,text = "Event Format",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
#         label32.place(x = 15,y = 380)

#         x12 = tk.StringVar()
#         x12.set("Hybrid")
#         label33 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x12,font = ctk.CTkFont(size = 12,weight = "bold"))
#         label33.place(x = 22,y = 410)

#         label34 = ctk.CTkLabel(f02,text = "Registration Capacity",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
#         label34.place(x = 15,y = 450)

#         x13 = tk.StringVar()
#         x13.set("In Person:Unlimited | Virtual:Unlimited")
#         label35 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x13,font = ctk.CTkFont(size = 12,weight = "bold"))
#         label35.place(x = 22,y = 480)

#         label36 = ctk.CTkLabel(f02,text = "Registration Deadline",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
#         label36.place(x = 15,y = 520)

#         x14 = tk.StringVar()
#         x14.set("30/7/2024 9:59 pm IST")
#         label37 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x14,font = ctk.CTkFont(size = 12,weight = "bold"))
#         label37.place(x = 22,y = 550)

#         label38 = ctk.CTkLabel(f02,text = "Planner",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
#         label38.place(x = 15,y = 590)

#         x15 = tk.StringVar()
#         x15.set("Lucky Tungariya")
#         label39 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x15,font = ctk.CTkFont(size = 12,weight = "bold"))
#         label39.place(x = 22,y = 620)

#         label40 = ctk.CTkLabel(f02,text = "Planner's Email",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
#         label40.place(x = 15,y = 660)

#         x16 = tk.StringVar()
#         x16.set("send@gmail.com")
#         label41 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x16,font = ctk.CTkFont(size = 12,weight = "bold"))
#         label41.place(x = 22,y = 690)

#     def tickettab_widgets(self):
#         ctk.CTkLabel(self.ticket_tab, text="Handle registrations and tickets", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

#     def reporttab_widgets(self):
#         ctk.CTkLabel(self.report_tab, text="View analytics and reports", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

#     def surveytab_widgets(self):
#         ctk.CTkLabel(self.survey_tab, text="Create surveys and view responses", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
        
# if __name__ == "__main__":
#     app = DemoApplication()
#     app.mainloop()

# import customtkinter as ctk
# from PIL import Image
# import tkinter as tk

# class DemoApplication(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("700x500")
#         self.resizable(width=True, height=True)
#         self.title("DemoApplication")
#         self.configure(fg_color="#093838")

#         ctk.set_appearance_mode("dark")
#         ctk.set_default_color_theme("my_custom_theme")

#         self.primary_color = "#093838"
#         self.secondary_color = "#8bceba"
#         self.bg = "gainsboro"
#         self.text_color = "#092928"
#         self.hovercolor_bg = "#20807f"
#         self.hovercolor_txt = "white"

#         self.click_count = 0
#         self.f3 = None
#         self.create_widgets()

#     def toggle_fullscreen(self, event=None):
#         # Set the application to fullscreen mode
#         self.attributes('-fullscreen', True)
#         self.bind("<Escape>", self.exit_fullscreen)

#     def exit_fullscreen(self, event=None):
#         width = self.winfo_screenwidth()
#         height = self.winfo_screenheight()
#         # Exit fullscreen mode
#         self.attributes('-fullscreen', False)
#         self.resizable(width=True, height=True)
#         self.geometry(f'{width - 200}x{height-100}')
#         self.maxsize(width,height)
#         # self.minsize(width,height)

#     def create_widgets(self):
#         self.toggle_fullscreen()
#         self.bind("<F11>", self.toggle_fullscreen)

#         frame2 = ctk.CTkFrame(self, height=30, fg_color=self.bg)
#         frame2.pack(fill="x")

#         labe = ctk.CTkLabel(frame2, text="Event Manager", font=("Segoe UI", 40, "bold"), text_color="white", fg_color=self.secondary_color, corner_radius=12)
#         labe.pack(pady=10, ipady=5,expand=True)

#         # Create a notebook (tabbed interface)
#         notebook = ctk.CTkTabview(self, width=700, height=500, bg_color = "gainsboro", corner_radius=12) #3fa572 #333333
#         notebook.pack(padx=20, pady=20, fill="both", expand=True)
#         # notebook.set(self.event_tab)

#         # Dashboard Tab
#         self.dashboard_tab = notebook.add("Dashboard")
#         self.dashboard_widgets()

#         # Event Management Tab
#         self.event_tab = notebook.add("Event Management")

#         self.full_frame1 = ctk.CTkFrame(self.event_tab, fg_color="white")
#         self.full_frame1.place(relx = 0.0, rely=0.0, relwidth =1, relheight = 1)

#         self.full_frame2 = ctk.CTkFrame(self.event_tab, fg_color=self.secondary_color, height=44)
#         self.full_frame2.place(relx = 0.0, y=41, relwidth =1)

#         self.full_frame3 = ctk.CTkFrame(self.event_tab, fg_color="#F0F0F0")
#         self.full_frame3.place(relx = 0.0,y = 82, relwidth =1, relheight = 1)

#         self.events_home()

#         # Registration and Ticketing Tab
#         self.ticket_tab = notebook.add("Registration and Ticketing")
#         self.tickettab_widgets()

#         # Reporting and Analytics Tab
#         self.report_tab = notebook.add("Reporting and Analytics")
#         self.reporttab_widgets()

#         # Survey and Feedback Tab
#         self.survey_tab = notebook.add("Survey and Feedback")
#         self.surveytab_widgets()

#     def create_sidebar_item(self, label, subitems):
#         frame = ctk.CTkFrame(self.f3, corner_radius=0)
#         frame.pack(fill="x", pady=(0, 1))

#         # Create a sub-frame for the button content
#         button_frame = ctk.CTkFrame(frame, corner_radius=0, fg_color="#20807f")
#         button_frame.pack(fill="x")

#         # Label on the left
#         label_widget = ctk.CTkButton(button_frame, text=label, anchor="w", command=lambda: self.toggle_subitems(frame, subitems), fg_color="#20807f", text_color="white")
#         label_widget.pack(side="left")

#         # Arrow on the right
#         arrow_label = ctk.CTkLabel(button_frame, text="▼", anchor="e")
#         arrow_label.pack(side="right", padx=(0, 5))

#         # Make the whole frame clickable
#         button_frame.bind("<Button-1>", lambda event: self.toggle_subitems(frame, subitems))

#         # Create hidden frame for subitems
#         subframe = ctk.CTkFrame(frame, corner_radius=20, fg_color="#093838")
#         subframe.pack(fill="x")
#         subframe.pack_forget()  # Initially hidden

#         # Create buttons for subitems
#         for item in subitems:
#             sub_button = ctk.CTkButton(subframe, text=f"  • {item}", anchor="w", fg_color="transparent", hover_color=("gray70", "gray30"), text_color="white")
#             sub_button.pack(fill="x")

#     def toggle_subitems(self, frame, subitems):
#         subframe = frame.winfo_children()[1]  # The subframe
#         arrow_label = frame.winfo_children()[0].winfo_children()[1]  # The arrow label

#         if subframe.winfo_viewable():
#             subframe.pack_forget()
#             arrow_label.configure(text="▼")
#         else:
#             subframe.pack(fill="x")
#             arrow_label.configure(text="▲")
        

#     def menu_animation(self):
#         self.click_count += 1

#         # self.temp_fr = ctk.CTkFrame(self.full_frame3, fg_color="yellow", width=246, border_width=1, border_color="lightgray")
#         # self.temp_fr.place(relheight=1, relx=0.1, y=0)

#         # Conditionally create sidebar on first click
#         if self.click_count % 2 != 0 and self.f3 is None:
#             self.f3 = ctk.CTkScrollableFrame(self.full_frame3, width=240, border_width=1, border_color="lightgray")
#             self.f3.place(relheight=1, relx=0.1, y=0)
            

#             # Add the sidebar content here (create_sidebar_item calls)
#             self.create_sidebar_item("General", ["Option 1", "Option 2"])
#             self.create_sidebar_item("Registration", ["Register", "Unregister"])
#             self.create_sidebar_item("Marketing", ["Campaigns", "Analytics"])
#             self.create_sidebar_item("Email", ["Compose", "Inbox", "Sent"])
#             self.create_sidebar_item("Attendees", ["List", "Groups"])
#             self.create_sidebar_item("Surveys", ["Feedback Surveys", "Responses"])
#             self.create_sidebar_item("Reports", ["Generate", "View"])
#             self.create_sidebar_item("Integrations", ["Connect", "Manage"])            
#             # ... add more sidebar items

#         # Show/hide sidebar based on click count
#         if self.click_count % 2 != 0:
#             self.f3.place_configure(relheight=1, relx=0.1, y=0)

#         else:
#             self.f3.place_forget()        
        
#         # No need for separate animate method
#         # self.after(1, lambda: self.animate(250, 82, 0.808))
#     def events_home(self):

#         f1 = ctk.CTkFrame(self.full_frame1, height=41, fg_color="white")
#         f1.place(relwidth = 1,relx=0.1, y=0)

#         label1 = ctk.CTkLabel(f1, text="cvent", text_color="black", justify="right", font=ctk.CTkFont(size=20, weight="bold"))
#         label1.place(x=15, y=5)

#         label2 = ctk.CTkLabel(f1, text="", width=2, height=20, fg_color="black")
#         label2.place(x=80, y=9.5)

#         label3 = ctk.CTkLabel(f1, text="EVENTS", text_color="#3fa6fb", font=ctk.CTkFont(size=17, weight="bold"))
#         label3.place(x=95, y=5)

#         label4 = ctk.CTkLabel(f1, text="All Events", text_color="black", font=ctk.CTkFont(size=17, weight="normal"))
#         label4.place(x=420, y=5)

#         x1 = ctk.StringVar()
#         x1.set("Calendar")
#         opt1 = ctk.CTkComboBox(f1, variable=x1, height=35, width=100, fg_color="white", text_color="black", border_color="white", button_color="white", button_hover_color="white", font=ctk.CTkFont(size=13, weight="normal"), values=["2020", "2021", "2022", "2023"])
#         opt1.place(x=540, y=5)

#         x2 = ctk.StringVar()
#         x2.set("More")
#         opt2 = ctk.CTkComboBox(f1, variable=x2, height=35, width=90, fg_color="white", text_color="black", border_color="white", button_color="white", button_hover_color="white", font=ctk.CTkFont(size=13, weight="normal"), values=["", "", "", ""])
#         opt2.place(x=670, y=5)

#         def butimg1():
#             pass

#         img1 = ctk.CTkImage(dark_image=Image.open(r"pics\loupe.png"), size=(20, 20))
#         butimg1 = ctk.CTkButton(f1, image=img1, fg_color="white", width=20, text="", hover_color="#3fa6fb", command=butimg1)
#         butimg1.place(x=1040, y=5)

#         def butimg2():
#             pass

#         img2 = ctk.CTkImage(dark_image=Image.open(r"pics\file.png"), size=(20, 20))
#         butimg2 = ctk.CTkButton(f1, image=img2, text="", fg_color="white", width=20, hover_color="#3fa6fb", command=butimg2)
#         butimg2.place(x=1090, y=5)

#         def butimg3():
#             pass

#         img3 = ctk.CTkImage(dark_image=Image.open(r"pics\question.png"), size=(20, 20))
#         butimg3 = ctk.CTkButton(f1, image=img3, text="", fg_color="white", width=20, hover_color="#3fa6fb", command=butimg3)
#         butimg3.place(x=1140, y=5)

#         def butimg4():
#             pass

#         img4 = ctk.CTkImage(dark_image=Image.open(r"pics\user (1).png"), size=(20, 20))
#         butimg4 = ctk.CTkButton(f1, image=img4, text="", fg_color="white", width=20, hover_color="#3fa6fb", command=butimg4)
#         butimg4.place(x=1190, y=5)

#         def butimg5():
#             pass

#         img5 = ctk.CTkImage(dark_image=Image.open(r"pics\menu.png"), size=(20, 20))
#         butimg5 = ctk.CTkButton(f1, image=img5, text="", fg_color="white", width=20, hover_color="#3fa6fb", command=butimg5)
#         butimg5.place(x=1240, y=5)

#         # canvas1 = tk.Canvas(self.event_tab, height=3, width=1920, bg="#0061ff", relief="raised")
#         # canvas1.place(x=0, y=56)

#         self.f2 = ctk.CTkFrame(self.full_frame2, height=44, fg_color="transparent")
#         self.f2.place(relwidth = 1,relx=0.107, y=0)

            
#         img6 = ctk.CTkImage(dark_image=Image.open(r"pics\lines.png"), size=(20, 20))
#         butimg6 = ctk.CTkButton(self.f2, image=img6, text="", fg_color="white", width=20, hover_color="white", command=self.menu_animation)
#         butimg6.place(x=6, y=5)

#         label5 = ctk.CTkLabel(self.f2, text="DemEven", text_color="black", font=ctk.CTkFont(size=15, weight="normal"))
#         label5.place(x=47, y=5)

#         x3 =ctk.StringVar()
#         e1 = ctk.CTkEntry(self.f2,height = 28,width = 250,fg_color = "white",corner_radius = 15,placeholder_text = "Search this Event",placeholder_text_color = "gray",text_color = "black",textvariable = x3)
#         e1.place(x = 1000,y = 5)

#         def butimg7():
#             pass

#         img7 = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (20,15))
#         butimg7 = ctk.CTkButton(self.f2,image = img7,text = "",fg_color = "white",width = 20,border_width = 1,border_color = "black",hover_color = "#8BFAFF",command = butimg7)
#         butimg7.place(x = 958,y = 5)

# #-----------------------

#         self.f0 = ctk.CTkScrollableFrame(self.full_frame3,width=1300,fg_color = "#F0F0F0")
#         self.f0.place(relheight = 1,relx = 0.1,y = 0)

#         f01 = ctk.CTkFrame(self.f0,height = 1050,width = 970,fg_color = "#F0F0F0")
#         f01.grid(row = 0,column = 0)

#         f4 = ctk.CTkFrame(f01,height = 200,width = 970,fg_color = "#ffffff")
#         f4.place(x = 0,y = 0)

#         label7 = ctk.CTkLabel(f4,text = "DemEven",fg_color = "white",text_color = "black",font = ctk.CTkFont(size = 25,weight = "bold"))
#         label7.place(x = 20,y = 80)

#         label8 = ctk.CTkLabel(f4,text = "Upcoming",fg_color = "#FEEEAB",text_color = "#EB9E29",corner_radius = 3,height = 10,width = 10,padx = 2,pady = 2)
#         label8.place(x = 20,y = 140)

#         img8 = ctk.CTkImage(dark_image = Image.open(r"pics\calendar.png"),size = (20,20))
#         labimg8 = ctk.CTkLabel(f4,image = img8,text = "")
#         labimg8.place(x = 120,y = 137)

#         label9 = ctk.CTkLabel(f4,text = "30/7/2024  6:00 pm - 10:00 pm  IST (61 days away)",text_color = "black",font = ctk.CTkFont(size = 13,weight = "normal"))
#         label9.place(x = 150,y = 137)

#         img9 = ctk.CTkImage(dark_image = Image.open(r"pics\location.png"),size = (20,20))
#         labimg9 = ctk.CTkLabel(f4,image = img9,text = "")
#         labimg9.place(x = 500,y = 137)

#         label10 = ctk.CTkLabel(f4,text = "Chicago",text_color = "black",font = ctk.CTkFont(size = 13,weight = "normal"))
#         label10.place(x = 522,y = 137)

#         x9 =ctk.StringVar()
#         x9.set("Actions")
#         opt8 = ctk.CTkComboBox(f4,height = 35,width = 150,variable = x9,fg_color = "white",button_hover_color = "#4B9EFC",border_width = 1,border_color = "lightgray",corner_radius = 7,dropdown_hover_color = "#4B9EFC",button_color = "lightgray",text_color = "#0966F1",values = ["","","",""])
#         opt8.place(x = 800,y = 96)

#         img10 = ctk.CTkImage(dark_image = Image.open(r"pics\light-bulb.png"),size = (50,50))
#         labimg10 = ctk.CTkLabel(self.f0,image = img10,text = "")
#         labimg10.place(x = 8,y = 205)

#         label11 = ctk.CTkLabel(self.f0,text = "Up next for your event",text_color = "black",font = ctk.CTkFont(size = 18,weight = "bold"))
#         label11.place(x = 50,y = 215)

#         f5 = ctk.CTkFrame(f01,height = 150,width = 265,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
#         f5.place(x = 8,y = 255)

#         img11 = ctk.CTkImage(dark_image = Image.open(r"pics\features.png"),size = (38,38))
#         labimg11 = ctk.CTkLabel(f5,image = img11,text = "")
#         labimg11.place(x = 15,y = 48)

#         label12 = ctk.CTkLabel(f5,text = "Add Event Features",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label12.place(x = 75,y = 20)

#         label13 = ctk.CTkLabel(f5,text = "Make sure you have all the\nfeatures you need for your event",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
#         label13.place(x = 75,y = 55)

#         def funbut1():
#             pass

#         button1 = ctk.CTkButton(f5,text = "Add features",corner_radius = 5,border_width = 1,width = 6,hover_color = "lightgray",border_color = "#3fa6fb",fg_color = "#ffffff",border_spacing = 3,text_color = "#3fa6fb",command = funbut1)
#         button1.place(x = 75,y = 100)

#         def skip1():
#             pass

#         button2 = ctk.CTkButton(f5,text = "Skip",width = 6,fg_color = "#ffffff",text_color = "#3fa6fb",hover_color = "#ffffff",command = skip1)
#         button2.place(x = 185,y = 100)

#         f6 = ctk.CTkFrame(f01,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
#         f6.place(x = 290,y = 255)

#         img12 = ctk.CTkImage(dark_image = Image.open(r"pics\registration.png"),size = (42,38))
#         labimg12 = ctk.CTkLabel(f6,image = img12,text = "")
#         labimg12.place(x = 15,y = 48)

#         label14 = ctk.CTkLabel(f6,text = "Set up registration types",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label14.place(x = 45,y = 20)

#         label15 = ctk.CTkLabel(f6,text = "Add registration types to\ncustomize the registration...",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
#         label15.place(x = 75,y = 55)

#         def funbut2():
#             pass

#         button3 = ctk.CTkButton(f6,text = "Get Started",corner_radius = 5,border_width = 1,width = 6,hover_color = "lightgray",border_color = "#3fa6fb",fg_color = "#ffffff",border_spacing = 3,text_color = "#3fa6fb",command = funbut2)
#         button3.place(x = 75,y = 100)

#         def skip2():
#             pass

#         button4 = ctk.CTkButton(f6,text = "Skip",width = 6,fg_color = "#ffffff",text_color = "#3fa6fb",hover_color = "#ffffff",command = skip2)
#         button4.place(x = 185,y = 100)

#         label16 = ctk.CTkLabel(f01,text = "Event Overview",text_color = "black",font = ctk.CTkFont(size = 18,weight = "bold"))
#         label16.place(x = 8,y = 420)

#         f7 = ctk.CTkFrame(f01,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
#         f7.place(x = 8,y = 460)

#         label17 = ctk.CTkLabel(f7,text = "Registration",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label17.place(x = 20,y = 20)

#         label18 = ctk.CTkLabel(f7,text = "Invitee Conversion Rate",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
#         label18.place(x = 20,y = 50)

#         label19 =  ctk.CTkLabel(f7,text = "0.0%",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label19.place(x = 20,y = 75)

#         img13 = ctk.CTkImage(dark_image = Image.open(r"pics\light-bulb.png"),size = (30,30))
#         labimg13 = ctk.CTkLabel(f7,image = img13,text = "")
#         labimg13.place(x = 15,y = 105)

#         label20 = ctk.CTkLabel(f7,text = "Set your event's deadline\nand capacity",text_color = "#3fa6fb",font = ctk.CTkFont(size = 12,weight = "normal"))
#         label20.place(x = 60,y = 105)

#         def butimg14():
#             pass 

#         img14 = ctk.CTkImage(dark_image = Image.open(r"pics\ellipsis.png"),size = (30,20))
#         butimg14 = ctk.CTkButton(f7,image = img14,text = "",command = butimg14,width = 20,fg_color = "#ffffff",hover_color = "#ffffff")
#         butimg14.place(x = 220,y = 20)

#         f8 = ctk.CTkFrame(f01,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
#         f8.place(x = 290,y = 460)

#         label21 = ctk.CTkLabel(f8,text = "Emails",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label21.place(x = 20,y = 20)

#         label22 = ctk.CTkLabel(f8,text = "Email sent",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
#         label22.place(x = 20,y = 50)

#         label23 =  ctk.CTkLabel(f8,text = "0",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 17,weight = "bold"))
#         label23.place(x = 20,y = 75)

#         labimg15 = ctk.CTkLabel(f8,image = img13,text = "")
#         labimg15.place(x = 15,y = 105)

#         label24 = ctk.CTkLabel(f8,text = "Add any custom data tags you\nneed for your event",text_color = "#3fa6fb",font = ctk.CTkFont(size = 12,weight = "normal"))
#         label24.place(x = 60,y = 105)
        
#         def butimg15():
#             pass

#         img15 = ctk.CTkImage(dark_image = Image.open(r"pics\ellipsis.png"),size = (30,20))
#         butimg15 = ctk.CTkButton(f8,image = img15,text = "",command = butimg15,width = 20,fg_color = "#ffffff",hover_color = "#ffffff")
#         butimg15.place(x = 220,y = 20)
        
#         f02 = ctk.CTkFrame(self.f0,height = 730,width = 290,fg_color = "gainsboro",corner_radius=12)
#         f02.grid(row=0,column=1, padx=(12,0), sticky="n")

#         def butimg16():
#             pass 

#         img16 = ctk.CTkImage(dark_image = Image.open(r"pics\right-arrow.png"),size = (30,30))
#         butimg16 = ctk.CTkButton(f02,image = img16,text = "",command = butimg16,fg_color = "#C8C6F3",hover_color = "#ffffff",width = 20)
#         butimg16.place(x = 400,y = 0)

#         label25 = ctk.CTkLabel(f02,text = "Feature Status",text_color = "black",font = ctk.CTkFont(size = 17,weight = "bold"), corner_radius = 9, fg_color="#F0F0F0")
#         label25.place(x = 15,y = 30)

#         img17 = ctk.CTkImage(dark_image = Image.open(r"pics\pending.png"),size = (20,20))
#         labimg17 = ctk.CTkLabel(f02,image = img17,text = "")
#         labimg17.place(x = 165,y = 30)

#         label26 = ctk.CTkLabel(f02,text = "Registration",text_color = "black", font = ctk.CTkFont(size = 19,weight = "normal"))
#         label26.place(x = 19,y = 60)

#         label27 = ctk.CTkLabel(f02,text = "Pending",text_color = "black",corner_radius = 19,height = 10,width = 10,padx = 2,pady = 2,font = ctk.CTkFont(size = 19))
#         label27.place(x = 350,y = 80)

#         label28 = ctk.CTkLabel(f02,text = "Search for attendees",text_color = "black",fg_color = "#F0F0F0",font = ctk.CTkFont(size = 17,weight = "bold"), corner_radius = 9, width=262)
#         label28.place(x = 15,y = 110)

#         x10 = tk.StringVar()
#         e2 = ctk.CTkEntry(f02,height = 30,width = 257,corner_radius = 15,fg_color = "#ffffff",text_color = "black",placeholder_text = "Enter a name or email",placeholder_text_color = "black",textvariable = x10)
#         e2.place(x = 18,y = 150)

#         canvas3 =  tk.Canvas(f02,height = 3,width = 262,bg = "gray",relief = tk.RAISED)
#         canvas3.place(x = 15,y = 215)

#         def butimg18():
#             pass 

#         img18 = ctk.CTkImage(dark_image = Image.open(r"pics\loupe.png"),size = (10,10))
#         butimg18 = ctk.CTkButton(e2,image = img7,text = "",fg_color = "white",hover_color = "#ffffff",corner_radius = 3,height = 10,width = 10,command = butimg18)
#         butimg18.place(x = 218,y = 3)

#         label29 = ctk.CTkLabel(f02,text = "Event Information",text_color = "black",fg_color = "#F0F0F0",font = ctk.CTkFont(size = 17,weight = "bold"), corner_radius = 9, width=262)
#         label29.place(x = 15,y = 260)

#         label30 = ctk.CTkLabel(f02,text = "Event Code",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
#         label30.place(x = 15,y = 310)

#         x11 = tk.StringVar()
#         x11.set("BAMMCYD")
#         label31 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x11,font = ctk.CTkFont(size = 12,weight = "bold"))
#         label31.place(x = 22,y = 340)

#         label32 = ctk.CTkLabel(f02,text = "Event Format",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
#         label32.place(x = 15,y = 380)

#         x12 = tk.StringVar()
#         x12.set("Hybrid")
#         label33 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x12,font = ctk.CTkFont(size = 12,weight = "bold"))
#         label33.place(x = 22,y = 410)

#         label34 = ctk.CTkLabel(f02,text = "Registration Capacity",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
#         label34.place(x = 15,y = 450)

#         x13 = tk.StringVar()
#         x13.set("In Person:Unlimited | Virtual:Unlimited")
#         label35 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x13,font = ctk.CTkFont(size = 12,weight = "bold"))
#         label35.place(x = 22,y = 480)

#         label36 = ctk.CTkLabel(f02,text = "Registration Deadline",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
#         label36.place(x = 15,y = 520)

#         x14 = tk.StringVar()
#         x14.set("30/7/2024 9:59 pm IST")
#         label37 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x14,font = ctk.CTkFont(size = 12,weight = "bold"))
#         label37.place(x = 22,y = 550)

#         label38 = ctk.CTkLabel(f02,text = "Planner",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
#         label38.place(x = 15,y = 590)

#         x15 = tk.StringVar()
#         x15.set("Lucky Tungariya")
#         label39 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x15,font = ctk.CTkFont(size = 12,weight = "bold"))
#         label39.place(x = 22,y = 620)

#         label40 = ctk.CTkLabel(f02,text = "Planner's Email",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"), corner_radius = 9)
#         label40.place(x = 15,y = 660)

#         x16 = tk.StringVar()
#         x16.set("send@gmail.com")
#         label41 = ctk.CTkLabel(f02,text_color = "#000000",textvariable = x16,font = ctk.CTkFont(size = 12,weight = "bold"))
#         label41.place(x = 22,y = 690)


#     def dashboard_widgets(self):
#         pass
#     def reporttab_widgets(self):
#         pass
#     def tickettab_widgets(self):
#         pass
#     def surveytab_widgets(self):
#         pass

# if __name__ == "__main__" : 
#     app = DemoApplication()
#     app.mainloop()