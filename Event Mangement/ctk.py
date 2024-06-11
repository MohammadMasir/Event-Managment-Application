import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image

screen = customtkinter.CTk()

def onclick():
    messagebox.showinfo(title = "message",message = "Button clicked")

def close():
    screen.destroy()

screen.configure(fg_color = "#F0F0F0")
screen.geometry("800x500")

my_img = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\back.png"),size = (20,20))
labimg = customtkinter.CTkButton(screen,image = my_img,text = "",fg_color = "#F0F0F0",hover_color = "white",width = 15,border_width = 1,border_color = "#F0F0F0",command = onclick)
labimg.place(x = 8,y = 5)

l1 = customtkinter.CTkLabel(screen,text = "New event",text_color = "black",fg_color = "#F0F0F0",font = ("bold",26))
l2 = customtkinter.CTkLabel(screen,text = "Great! Tell us a little about your event.",text_color = "black",fg_color = "#F0F0F0",font = ("thin",19))
l1.place(x = 70,y = 53)
l2.place(x = 70,y = 81)

scrollable_frame = customtkinter.CTkScrollableFrame(screen,height = 470,width = 800,orientation = "vertical",fg_color = "white",border_width = 0.8,border_color = "black",scrollbar_button_color = "white",scrollbar_fg_color = "black")
f1 = customtkinter.CTkFrame(scrollable_frame,fg_color = "white",height = 950,width = 800)
scrollable_frame.place(x = 70,y = 125)
f1.pack()

img1 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\info.png"),size = (30,30))
labimg1 = customtkinter.CTkLabel(f1,image = img1,text = "")
labimg1.place(x = 30,y = 9)

l3 = customtkinter.CTkLabel(f1,text = "Basic Information",text_color = "black",font = ("darkbold",23))
l4 = customtkinter.CTkLabel(f1,text = "* Event Title",text_color = "black",font = ("thin",19))
l3.place(x = 67,y = 9)
l4.place(x = 30,y = 50)

def check_x1():
    if x1.get() == "":
        messagebox.showerror(title = "Error",message = "Please input Event Title")

    if x2.get() == "":
        messagebox.showerror(title = "Error",message = "Please choose Event Category")
    
    if x6.get() == "":
        messagebox.showerror(title = "Error",message = "Please input your last name")

    if x7.get() == "":
        messagebox.showerror(title = "Error",message = "Please input your Email")

    if x8.get() == "":
        messagebox.showerror(title = "Error",message = "Please input full Format")

    if x10.get() == "":
        messagebox.showerror(title = "Error",message = "Please input full format")

    if x14.get() == "":
        messagebox.showerror(title = "Error",message = "Please choose the state")


x1 = StringVar()
e1 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 690,textvariable = x1)
l5 = customtkinter.CTkLabel(f1,text = "* Event Category",text_color = "black",font = ("thin",19))
e1.place(x = 30,y = 82)
l5.place(x = 30,y = 128)

x2 = StringVar()
opt1 = customtkinter.CTkComboBox(f1,variable = x2,height = 35,width = 200,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["Educational","Business","Sports"])
opt1.place(x = 30,y = 165)

l6 = customtkinter.CTkLabel(f1,text = "Language",text_color = "black",font = ("thin",19))
l6.place(x = 280,y = 128)
x3 = StringVar()

opt2 =  customtkinter.CTkComboBox(f1,variable = x3,height = 35,width = 200,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["English","Spanish","Hindi"])
opt2.place(x = 280,y = 165)
l7 = customtkinter.CTkLabel(f1,text = "Locale",text_color = "black",font = ("thin",19))
l7.place(x = 520,y = 128)

x4 = StringVar()
opt3 =  customtkinter.CTkComboBox(f1,variable = x4,height = 35,width = 200,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["USA","INDIA","CANADA"])
opt3.place(x = 520,y = 165)
l8 = customtkinter.CTkLabel(f1,text = "* Planner First Name",text_color = "black",font = ("thin",19))
l8.place(x = 30,y = 220)

x5 = StringVar()
e2 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x5)
e2.place(x = 30,y = 250)
l9 = customtkinter.CTkLabel(f1,text = "* Last Name",text_color = "black",font = ("thin",19))
l9.place(x = 280,y = 220)

x6 = StringVar()
e3 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x6)
e3.place(x = 280,y = 250)
label1 = customtkinter.CTkLabel(f1,text = "* Planner Email",text_color = "black",font = ("thin",19))
label1.place(x = 520,y = 220)

x7 = StringVar()
e4 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x7)
e4.place(x = 520,y = 250)

img5 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\event-management.png"),size = (280,280))
labimg5 = customtkinter.CTkLabel(screen,image = img5,text = "")
labimg5.place(x = 900,y = 130)

label2 = customtkinter.CTkLabel(screen,text = "This is just the start..!!",text_color = "black",fg_color = "#F0F0F0",font = ("semibold",21))
label2.place(x = 900,y = 420)
label3 = customtkinter.CTkLabel(screen,text = "We can't wait to see what kind of event you put on!",text_color = "black",fg_color = "#F0F0F0",font = ("thin",16))
label3.place(x = 900,y = 450)

img2 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\location.png"),size = (30,30))
labimg2 = customtkinter.CTkLabel(f1,image = img2,text = "")
labimg2.place(x = 30,y = 310)

label4 = customtkinter.CTkLabel(f1,text = "Location",text_color = "black",fg_color = "white",font = ("darkbold",23))
label4.place(x = 67,y = 310)
label5 = customtkinter.CTkLabel(f1,text = "* Format",text_color = "black",font = ("thin",19))
label5.place(x = 30,y = 352)

x8 = StringVar()
e5 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x8)
e5.place(x = 30,y = 394)

x9 = StringVar()
e6 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x9)
e6.place(x = 280,y = 394)

x10 = StringVar()
e7 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 200,textvariable = x10)
e7.place(x = 520,y = 394)

label6 = customtkinter.CTkLabel(f1,text = "Venue",text_color = "black",font = ("thin",19))
label6.place(x = 30,y = 436)

x11 = StringVar()
e8 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 690,textvariable = x11)
e8.place(x = 30,y = 478)

img3 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\close.png"),size = (20,20))
labimg3 = customtkinter.CTkButton(screen,image = img3,text = "",fg_color = "#F0F0F0",hover_color = "white",width = 15,border_width = 1,border_color = "#F0F0F0",command = close)
labimg3.place(x = 1225,y = 5)

img4 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\mall.png"),size = (20,20))
labimg4 = customtkinter.CTkLabel(e8,image = img4,text = "")
labimg4.place(x = 653,y = 3)

label7 = customtkinter.CTkLabel(f1,text = "Address",text_color = "black",font = ("thin",19))
label7.place(x = 30,y = 520)

x12 = StringVar()
e9 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 690,textvariable = x12)
e9.place(x = 30,y = 562)

label8 = customtkinter.CTkLabel(f1,text = "City",text_color = "black",font = ("thin",19))
label8.place(x = 30,y = 604)

x13 = StringVar()
e10 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x13)
e10.place(x = 30,y = 646)

label9 = customtkinter.CTkLabel(f1,text = "* State",text_color = "black",font = ("thin",19))
label9.place(x = 205,y = 604)

x14 = StringVar()
opt4 = customtkinter.CTkComboBox(f1,variable = x14,height = 35,width = 145,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["Maharashtra","Rajasthan","Uttar Pradesh","Gujarat","Punjab"])
opt4.place(x = 205,y = 646)

label10 = customtkinter.CTkLabel(f1,text = "ZIP/Postal code",text_color = "black",font = ("thin",19))
label10.place(x = 375,y = 604)

x15 = StringVar()
e11 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x15)
e11.place(x = 375,y = 646)

label11 = customtkinter.CTkLabel(f1,text = "Country",text_color = "black",font = ("thin",19))
label11.place(x = 540,y = 604)

x16 = StringVar()
opt5 = customtkinter.CTkComboBox(f1,variable = x16,height = 35,width = 145,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["India","New Zealand","USA","Russia"])
opt5.place(x = 540,y = 646)

img6 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\calendar.png"),size = (30,30))
labimg6 = customtkinter.CTkLabel(f1,image = img6,text = "")
labimg6.place(x = 30,y = 692)

label12 = customtkinter.CTkLabel(f1,text = "Event Dates",text_color = "black",font = ("darkbold",23))
label12.place(x = 67,y = 692)

label13 = customtkinter.CTkLabel(f1,text = "Start Date",text_color = "black",font = ("thin",19))
label13.place(x = 30,y = 732)

x17 = StringVar()
e12 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x17)
e12.place(x = 30,y = 768)

label14 = customtkinter.CTkLabel(f1,text = "Start Time",text_color = "black",font = ("thin",19))
label14.place(x = 205,y = 732)

x18 = StringVar()
e13 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x18)
e13.place(x = 205,y = 768)

label15 = customtkinter.CTkLabel(f1,text = "End Date",text_color = "black",font = ("thin",19))
label15.place(x = 375,y = 732)

x19 = StringVar()
e14 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x19)
e14.place(x = 375,y = 768)

label16 = customtkinter.CTkLabel(f1,text = "End Time",text_color = "black",font = ("thin",19))
label16.place(x = 540,y = 732)

x20 = StringVar()
e15 = customtkinter.CTkEntry(f1,corner_radius = 5,text_color = "black",fg_color = "white",height = 35,width = 145,textvariable = x20)
e15.place(x = 540,y = 768)

img7 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\calendar (1).png"),size = (30,30))
labimg7 = customtkinter.CTkLabel(e12,image = img7,text = "")
labimg7.place(x = 105,y = 2)

labimg8 = customtkinter.CTkLabel(e14,image = img7,text = "")
labimg8.place(x = 105,y = 2)

label17 = customtkinter.CTkLabel(f1,text = "Time Zone",text_color = "black",font = ("thin",19))
label17.place(x = 30,y = 810)

x21 = StringVar()
opt6 = customtkinter.CTkComboBox(f1,variable = x21,height = 35,width = 690,corner_radius = 5,border_width = 1,border_color = "gray",fg_color = "white",text_color = "black",button_hover_color = "#7D6D6D",font = ("semibold",17),values = ["(GMT+05:30) India","(GMT+09:05) USA","(GMT-03:40) New Zealand"])
opt6.place(x = 30,y = 850)

b1 = customtkinter.CTkButton(f1,text = "Submit",height = 40,width = 170,corner_radius =10,fg_color = "lightgreen",text_color = "black",command = check_x1)
b1.place(x = 300,y = 904)

screen.mainloop()