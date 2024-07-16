import customtkinter as ctk
from tkinter.messagebox import showinfo, showwarning, showerror
from PIL import Image
from eventshome import DashboardPage

class CreateEvent():
    def __init__(self, parent, main_app):
        super().__init__()
        self.parent = parent
        self.main_app = main_app

    def create_event(self):
        # self.main_app.previewmain_frame.destroy()
        for widget in self.parent.winfo_children():
            widget.pack_forget()

        # Main container frame
        self.form_main = ctk.CTkFrame(self.parent)
        self.form_main.pack(fill="both", expand=True)

        # Top frame for back button and labels
        top_frame = ctk.CTkFrame(self.form_main, fg_color="transparent")
        top_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Back button
        my_img = ctk.CTkImage(dark_image=Image.open(r"pics\back.png"), size=(20, 20))
        self.cvent_labimg = ctk.CTkButton(top_frame, image=my_img, text="", fg_color="#F0F0F0", hover_color="white", width=15, border_width=1, border_color="#F0F0F0", command=lambda: self.main_app.back_preview(self.form_main))
        self.cvent_labimg.pack(side="left", anchor="nw",padx=10, pady=10)

        # Labels
        self.cvent_l1 = ctk.CTkLabel(top_frame, text="New event", font=("bold", 26))
        self.cvent_l2 = ctk.CTkLabel(top_frame, text="Great! Tell us a little about your event.", font=("thin", 19))
        self.cvent_l1.pack(side="top", anchor="nw", pady=(10,5))
        self.cvent_l2.pack(side="top", anchor="nw")

        # Content frame (will contain scrollable frame and image frame)
        content_frame = ctk.CTkFrame(self.form_main, fg_color="transparent")
        content_frame.grid(row=1, column=0, columnspan=2, sticky="nsew",pady=4)

        # Scrollable frame (left side)
        self.cvent_scrollable_frame = ctk.CTkScrollableFrame(content_frame, height=470, width=800, orientation="vertical", fg_color="white", border_width=0.8, border_color="black", scrollbar_button_color="white", scrollbar_fg_color="black")
        self.cvent_scrollable_frame.grid(row=0, column=0, sticky="nsew")

        # Image frame (right side)
        image_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        image_frame.grid(row=0, column=1, sticky="nsew")

        # Add your image and labels to the image_frame here
        img5 = ctk.CTkImage(dark_image=Image.open(r"pics\management.png"), size=(340, 280))
        self.cvent_labimg5 = ctk.CTkLabel(image_frame, image=img5, text="", bg_color="white")
        self.cvent_labimg5.pack(pady=20)

        self.label2 = ctk.CTkLabel(image_frame, text="This is just the start..!!", text_color="black", fg_color="#F0F0F0", font=("semibold", 21))
        self.label2.pack()
        self.label3 = ctk.CTkLabel(image_frame, text="We can't wait to see what kind of event you put on!", text_color="black", fg_color="#F0F0F0", font=("thin", 16))
        self.label3.pack()

        # Configure grid weights
        self.form_main.grid_rowconfigure(1, weight=1)
        self.form_main.grid_columnconfigure(0, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=3)  # Give more weight to the scrollable frame
        content_frame.grid_columnconfigure(1, weight=1)

        # Add your form elements to self.cvent_scrollable_frame here
        # ...
        self.inside_scrollable_frame = ctk.CTkFrame(self.cvent_scrollable_frame,fg_color = "white",height = 950,width = 800)
        self.inside_scrollable_frame.pack(fill="both",expand=True)

        img1 = ctk.CTkImage(dark_image = Image.open(r"pics\info.png"),size = (30,30))
        labimg1 = ctk.CTkLabel(self.inside_scrollable_frame,image = img1,text = "")
        labimg1.place(x = 30,y = 9)

        l3 = ctk.CTkLabel(self.inside_scrollable_frame,text = "Basic Information",text_color = "black",font = ("darkbold",23))
        l4 = ctk.CTkLabel(self.inside_scrollable_frame,text = "* Event Title",text_color = "black",font = ("thin",19))
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

            self.homepage = DashboardPage(self.main_app)
            self.homepage.events_home()

        x1 =ctk.StringVar()
        e1 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 690,textvariable = x1)
        l5 = ctk.CTkLabel(self.inside_scrollable_frame,text = "* Event Category",text_color = "black",font = ("thin",19))
        e1.place(x = 30,y = 82)
        l5.place(x = 30,y = 128)

        x2 =ctk.StringVar()
        opt1 = ctk.CTkComboBox(self.inside_scrollable_frame,variable = x2,height = 35,width = 200,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["Educational","Business","Sports"])
        opt1.place(x = 30,y = 165)

        l6 = ctk.CTkLabel(self.inside_scrollable_frame,text = "Language",text_color = "black",font = ("thin",19))
        l6.place(x = 280,y = 128)
        x3 =ctk.StringVar()

        opt2 =  ctk.CTkComboBox(self.inside_scrollable_frame,variable = x3,height = 35,width = 200,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["English","Spanish","Hindi"])
        opt2.place(x = 280,y = 165)
        l7 = ctk.CTkLabel(self.inside_scrollable_frame,text = "Locale",text_color = "black",font = ("thin",19))
        l7.place(x = 520,y = 128)

        x4 =ctk.StringVar()
        opt3 =  ctk.CTkComboBox(self.inside_scrollable_frame,variable = x4,height = 35,width = 200,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["USA","INDIA","CANADA"])
        opt3.place(x = 520,y = 165)
        l8 = ctk.CTkLabel(self.inside_scrollable_frame,text = "* Planner First Name",text_color = "black",font = ("thin",19))
        l8.place(x = 30,y = 220)

        x5 =ctk.StringVar()
        e2 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x5)
        e2.place(x = 30,y = 250)
        l9 = ctk.CTkLabel(self.inside_scrollable_frame,text = "* Last Name",text_color = "black",font = ("thin",19))
        l9.place(x = 280,y = 220)

        x6 =ctk.StringVar()
        e3 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x6)
        e3.place(x = 280,y = 250)
        label1 = ctk.CTkLabel(self.inside_scrollable_frame,text = "* Planner Email",text_color = "black",font = ("thin",19))
        label1.place(x = 520,y = 220)

        x7 =ctk.StringVar()
        e4 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x7)
        e4.place(x = 520,y = 250)

        img2 = ctk.CTkImage(dark_image = Image.open(r"pics\location.png"),size = (30,30))
        labimg2 = ctk.CTkLabel(self.inside_scrollable_frame,image = img2,text = "")
        labimg2.place(x = 30,y = 310)

        label4 = ctk.CTkLabel(self.inside_scrollable_frame,text = "Location",text_color = "black",fg_color = "white",font = ("darkbold",23))
        label4.place(x = 67,y = 310)
        label5 = ctk.CTkLabel(self.inside_scrollable_frame,text = "* Format",text_color = "black",font = ("thin",19))
        label5.place(x = 30,y = 352)

        x8 =ctk.StringVar()
        e5 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x8)
        e5.place(x = 30,y = 394)

        x9 =ctk.StringVar()
        e6 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x9)
        e6.place(x = 280,y = 394)

        x10 =ctk.StringVar()
        e7 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x10)
        e7.place(x = 520,y = 394)

        label6 = ctk.CTkLabel(self.inside_scrollable_frame,text = "Venue",text_color = "black",font = ("thin",19))
        label6.place(x = 30,y = 436)

        x11 =ctk.StringVar()
        e8 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 690,textvariable = x11)
        e8.place(x = 30,y = 478)

        img4 = ctk.CTkImage(dark_image = Image.open(r"pics\mall.png"),size = (20,20))
        labimg4 = ctk.CTkLabel(e8,image = img4,text = "")
        labimg4.place(x = 653,y = 3)

        label7 = ctk.CTkLabel(self.inside_scrollable_frame,text = "Address",text_color = "black",font = ("thin",19))
        label7.place(x = 30,y = 520)

        x12 =ctk.StringVar()
        e9 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 690,textvariable = x12)
        e9.place(x = 30,y = 562)

        label8 = ctk.CTkLabel(self.inside_scrollable_frame,text = "City",text_color = "black",font = ("thin",19))
        label8.place(x = 30,y = 604)

        x13 =ctk.StringVar()
        e10 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x13)
        e10.place(x = 30,y = 646)

        label9 = ctk.CTkLabel(self.inside_scrollable_frame,text = "* State",text_color = "black",font = ("thin",19))
        label9.place(x = 205,y = 604)

        x14 =ctk.StringVar()
        opt4 = ctk.CTkComboBox(self.inside_scrollable_frame,variable = x14,height = 35,width = 145,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["Maharashtra","Rajasthan","Uttar Pradesh","Gujarat","Punjab"])
        opt4.place(x = 205,y = 646)

        label10 = ctk.CTkLabel(self.inside_scrollable_frame,text = "ZIP/Postal code",text_color = "black",font = ("thin",19))
        label10.place(x = 375,y = 604)

        x15 =ctk.StringVar()
        e11 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x15)
        e11.place(x = 375,y = 646)

        label11 = ctk.CTkLabel(self.inside_scrollable_frame,text = "Country",text_color = "black",font = ("thin",19))
        label11.place(x = 540,y = 604)

        x16 =ctk.StringVar()
        opt5 = ctk.CTkComboBox(self.inside_scrollable_frame,variable = x16,height = 35,width = 145,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["India","New Zealand","USA","Russia"])
        opt5.place(x = 540,y = 646)

        img6 = ctk.CTkImage(dark_image = Image.open(r"pics\calendar.png"),size = (30,30))
        labimg6 = ctk.CTkLabel(self.inside_scrollable_frame,image = img6,text = "")
        labimg6.place(x = 30,y = 692)

        label12 = ctk.CTkLabel(self.inside_scrollable_frame,text = "Event Dates",text_color = "black",font = ("darkbold",23))
        label12.place(x = 67,y = 692)

        label13 = ctk.CTkLabel(self.inside_scrollable_frame,text = "Start Date",text_color = "black",font = ("thin",19))
        label13.place(x = 30,y = 732)

        x17 =ctk.StringVar()
        e12 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x17)
        e12.place(x = 30,y = 768)

        label14 = ctk.CTkLabel(self.inside_scrollable_frame,text = "Start Time",text_color = "black",font = ("thin",19))
        label14.place(x = 205,y = 732)

        x18 =ctk.StringVar()
        e13 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x18)
        e13.place(x = 205,y = 768)

        label15 = ctk.CTkLabel(self.inside_scrollable_frame,text = "End Date",text_color = "black",font = ("thin",19))
        label15.place(x = 375,y = 732)

        x19 =ctk.StringVar()
        e14 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x19)
        e14.place(x = 375,y = 768)

        label16 = ctk.CTkLabel(self.inside_scrollable_frame,text = "End Time",text_color = "black",font = ("thin",19))
        label16.place(x = 540,y = 732)

        x20 =ctk.StringVar()
        e15 = ctk.CTkEntry(self.inside_scrollable_frame,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x20)
        e15.place(x = 540,y = 768)

        img7 = ctk.CTkImage(dark_image = Image.open(r"pics\calendar (1).png"),size = (30,30))
        labimg7 = ctk.CTkLabel(e12,image = img7,text = "")
        labimg7.place(x = 105,y = 2)

        labimg8 = ctk.CTkLabel(e14,image = img7,text = "")
        labimg8.place(x = 105,y = 2)

        label17 = ctk.CTkLabel(self.inside_scrollable_frame,text = "Time Zone",text_color = "black",font = ("thin",19))
        label17.place(x = 30,y = 810)

        x21 =ctk.StringVar()
        opt6 = ctk.CTkComboBox(self.inside_scrollable_frame,variable = x21,height = 35,width = 690,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["(GMT+05:30) India","(GMT+09:05) USA","(GMT-03:40) New Zealand"])
        opt6.place(x = 30,y = 850)

        b1 = ctk.CTkButton(self.inside_scrollable_frame,text = "Submit",height = 40,width = 170,corner_radius =10,fg_color = "lightgreen",text_color = "black",command = check_x1)
        b1.place(x = 300,y = 904)
