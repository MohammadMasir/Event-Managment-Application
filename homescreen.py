import customtkinter
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from PIL import Image

root = customtkinter.CTk()
root.configure(fg_color = "#F0F0F0")
root.geometry("800x800")
root.title("Home Screen")

f1 = customtkinter.CTkFrame(root,height = 41,width = 1300,fg_color = "white")
f1.place(x = 0,y = 0)

label1 = customtkinter.CTkLabel(f1,text = "cvent",text_color = "black",justify = "right",font = customtkinter.CTkFont(size =  20,weight = "bold"))
label1.place(x = 15,y = 5)

label2 = customtkinter.CTkLabel(f1,text = "",width = 2,height = 20,fg_color = "black")
label2.place(x = 80,y = 9.5)

label3 = customtkinter.CTkLabel(f1,text = "EVENTS",text_color = "#3fa6fb",font = customtkinter.CTkFont(size = 17,weight = "bold"))
label3.place(x = 95,y = 5)

label4 = customtkinter.CTkLabel(f1,text = "All Events",text_color = "black",font = (customtkinter.CTkFont(size = 17,weight = "normal")))
label4.place(x = 420,y = 5)

x1 = StringVar()
x1.set("Calendar")
opt1 = customtkinter.CTkComboBox(f1,variable = x1,height = 35,width = 100,fg_color = "white",text_color = "black",border_color = "white",button_color = "white",button_hover_color = "white",font = customtkinter.CTkFont(size = 13,weight = "normal"),values = ["2020","2021","2022","2023"])
opt1.place(x = 540,y = 5)

x2 = StringVar()
x2.set("More")
opt2 = customtkinter.CTkComboBox(f1,variable = x2,height = 35,width = 90,fg_color = "white",text_color = "black",border_color = "white",button_color = "white",button_hover_color = "white",font = customtkinter.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
opt2.place(x = 670,y = 5)

def butimg1():
    pass

img1 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\loupe.png"),size = (20,20))
butimg1 = customtkinter.CTkButton(f1,image = img1,fg_color = "white",width = 20,text = "",hover_color = "#3fa6fb",command = butimg1)
butimg1.place(x = 1040,y = 5)

def butimg2():
    pass 

img2 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\file.png"),size = (20,20))
butimg2 = customtkinter.CTkButton(f1,image = img2,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg2)
butimg2.place(x = 1090,y = 5)

def butimg3():
    pass

img3 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\question.png"),size = (20,20))
butimg3 = customtkinter.CTkButton(f1,image = img3,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg3)
butimg3.place(x = 1140,y = 5)

def butimg4():
    pass

img4 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\user (1).png"),size = (20,20))
butimg4 = customtkinter.CTkButton(f1,image = img4,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg4)
butimg4.place(x = 1190,y = 5)

def butimg5():
    pass

img5 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\menu.png"),size = (20,20))
butimg5 = customtkinter.CTkButton(f1,image = img5,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg5)
butimg5.place(x = 1240,y = 5)

canvas1 = Canvas(root,height = 3,width = 1920,bg = "#0061ff",relief = RAISED)
canvas1.place(x = 0,y = 56)

f2 = customtkinter.CTkFrame(root,height = 44,width = 1300,fg_color = "white")
f2.place(x = 0,y = 41)

def butimg6():
    pass 
    
img6 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\lines.png"),size = (20,20))
butimg6 = customtkinter.CTkButton(f2,image = img6,text = "",fg_color = "white",width = 20,hover_color = "white",command = butimg6)
butimg6.place(x = 6,y = 5)

label5 = customtkinter.CTkLabel(f2,text = "DemEven",text_color = "black",font = (customtkinter.CTkFont(size = 15,weight = "normal")))
label5.place(x = 47,y = 5)

x3 = StringVar()
e1 = customtkinter.CTkEntry(f2,height = 28,width = 250,corner_radius = 15,fg_color = "#ffffff",text_color = "black",placeholder_text = "Search this event",placeholder_text_color = "black",textvariable = x3)
e1.place(x = 1000,y = 5)

def butimg7():
    pass

img7 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\loupe.png"),size = (20,15))
butimg7 = customtkinter.CTkButton(f2,image = img7,text = "",fg_color = "white",width = 20,border_width = 1,border_color = "black",hover_color = "#8BFAFF",command = butimg7)
butimg7.place(x = 958,y = 5)

f3 = customtkinter.CTkFrame(root,fg_color = "white",height = 600,width = 250,border_width = 1,border_color = "lightgray")
f3.place(x = 0,y = 81)

#sidebar_frame = customtkinter.CTkFrame(f3,height = 300,width = 500,fg_color = "lightgray")
#sidebar_frame.place(x = -500,y = 50)

label6 = customtkinter.CTkLabel(f3,text = "HOME",text_color = "#3fa6fb",font = (customtkinter.CTkFont(size = 20,weight = "bold")))
label6.place(x = 13,y = 17)

x4 = StringVar()
x4.set("General")
opt3 = customtkinter.CTkOptionMenu(f3,variable = x4,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = customtkinter.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
opt3.place(x = 5,y = 50)

x5 = StringVar()
x5.set("Marketing")
opt4 = customtkinter.CTkOptionMenu(f3,variable = x5,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = customtkinter.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
opt4.place(x = 5,y = 100)

x6 = StringVar()
x6.set("Email")
opt5 = customtkinter.CTkOptionMenu(f3,variable = x6,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = customtkinter.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
opt5.place(x = 5,y = 150)

x7 = StringVar()
x7.set("Attendees")
opt6 = customtkinter.CTkOptionMenu(f3,variable = x7,button_color = "white",button_hover_color = "white",height = 35,width = 230,fg_color = "white",text_color = "black",dropdown_hover_color = "lightblue",font = customtkinter.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
opt6.place(x = 5,y = 200)

x8 = StringVar()
x8.set("Reports")
opt7 = customtkinter.CTkOptionMenu(f3,height = 35,width = 230,variable = x8,fg_color = "white",dropdown_hover_color = "lightblue",text_color = "black",button_color = "white",button_hover_color = "white",values = ["","","",""])
opt7.place(x = 5,y = 250)

b1 = customtkinter.CTkLabel(f3,text = "Integrations",fg_color = "white",text_color = "black")
b1.place(x = 10,y = 300)

f0 = customtkinter.CTkScrollableFrame(root,height = 700,width = 1010,fg_color = "#F0F0F0")
f0.place(x = 250,y = 82)

f01 = customtkinter.CTkFrame(f0,height = 1050,width = 1010,fg_color = "#F0F0F0")
f01.grid(row = 0,column = 0)

f4 = customtkinter.CTkFrame(f01,height = 200,width = 1010,fg_color = "#ffffff")
f4.place(x = 0,y = 0)

label7 = customtkinter.CTkLabel(f4,text = "DemEven",fg_color = "white",text_color = "black",font = customtkinter.CTkFont(size = 25,weight = "bold"))
label7.place(x = 20,y = 80)

label8 = customtkinter.CTkLabel(f4,text = "Upcoming",fg_color = "#FEEEAB",text_color = "#EB9E29",corner_radius = 5,height = 10,width = 9,padx = 2,pady = 2,font = ctk.CTkFont(size = 19))
label8.place(x = 20,y = 140)

img8 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\calendar.png"),size = (20,20))
labimg8 = customtkinter.CTkLabel(f4,image = img8,text = "")
labimg8.place(x = 130,y = 137)

label9 = customtkinter.CTkLabel(f4,text = "30/7/2024  6:00 pm - 10:00 pm  IST (61 days away)",text_color = "black",font = customtkinter.CTkFont(size = 13,weight = "normal"))
label9.place(x = 150,y = 137)

img9 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\location.png"),size = (20,20))
labimg9 = customtkinter.CTkLabel(f4,image = img9,text = "")
labimg9.place(x = 500,y = 137)

label10 = customtkinter.CTkLabel(f4,text = "Chicago",text_color = "black",font = customtkinter.CTkFont(size = 13,weight = "normal"))
label10.place(x = 522,y = 137)

x9 = StringVar()
x9.set("Actions")
opt8 = customtkinter.CTkComboBox(f4,height = 35,width = 150,variable = x9,fg_color = "white",button_hover_color = "#4B9EFC",border_width = 1,border_color = "lightgray",corner_radius = 7,dropdown_hover_color = "#4B9EFC",button_color = "lightgray",text_color = "#0966F1",values = ["","","",""])
opt8.place(x = 800,y = 96)

img10 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\light-bulb.png"),size = (50,50))
labimg10 = customtkinter.CTkLabel(f0,image = img10,text = "")
labimg10.place(x = 8,y = 205)

label11 = customtkinter.CTkLabel(f0,text = "Up next for your event",text_color = "black",font = customtkinter.CTkFont(size = 18,weight = "bold"))
label11.place(x = 50,y = 215)

f5 = customtkinter.CTkFrame(f01,height = 150,width = 265,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
f5.place(x = 8,y = 255)

img11 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\features.png"),size = (38,38))
labimg11 = customtkinter.CTkLabel(f5,image = img11,text = "")
labimg11.place(x = 15,y = 48)

label12 = customtkinter.CTkLabel(f5,text = "Add Event Features",text_color = "#000000",font = customtkinter.CTkFont(size = 17,weight = "bold"))
label12.place(x = 75,y = 20)

label13 = customtkinter.CTkLabel(f5,text = "Make sure you have all the\nfeatures you need for your event",text_color = "#000000",font = customtkinter.CTkFont(size = 12,weight = "normal"))
label13.place(x = 75,y = 55)

def funbut1():
    pass

button1 = customtkinter.CTkButton(f5,text = "Add features",corner_radius = 5,border_width = 1,width = 6,hover_color = "lightgray",border_color = "#3fa6fb",fg_color = "#ffffff",border_spacing = 3,text_color = "#3fa6fb",command = funbut1)
button1.place(x = 75,y = 100)

def skip1():
    pass

button2 = customtkinter.CTkButton(f5,text = "Skip",width = 6,fg_color = "#ffffff",text_color = "#3fa6fb",hover_color = "#ffffff",command = skip1)
button2.place(x = 185,y = 100)

f6 = customtkinter.CTkFrame(f01,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
f6.place(x = 290,y = 255)

img12 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\registration.png"),size = (42,38))
labimg12 = customtkinter.CTkLabel(f6,image = img12,text = "")
labimg12.place(x = 15,y = 48)

label14 = customtkinter.CTkLabel(f6,text = "Set up registration types",text_color = "#000000",font = customtkinter.CTkFont(size = 17,weight = "bold"))
label14.place(x = 45,y = 20)

label15 = customtkinter.CTkLabel(f6,text = "Add registration types to\ncustomize the registration...",text_color = "#000000",font = customtkinter.CTkFont(size = 12,weight = "normal"))
label15.place(x = 75,y = 55)

def funbut2():
    pass

button3 = customtkinter.CTkButton(f6,text = "Get Started",corner_radius = 5,border_width = 1,width = 6,hover_color = "lightgray",border_color = "#3fa6fb",fg_color = "#ffffff",border_spacing = 3,text_color = "#3fa6fb",command = funbut2)
button3.place(x = 75,y = 100)

def skip2():
    pass

button4 = customtkinter.CTkButton(f6,text = "Skip",width = 6,fg_color = "#ffffff",text_color = "#3fa6fb",hover_color = "#ffffff",command = skip2)
button4.place(x = 185,y = 100)

label16 = customtkinter.CTkLabel(f0,text = "Event Overview",text_color = "black",font = customtkinter.CTkFont(size = 18,weight = "bold"))
label16.place(x = 8,y = 420)

f7 = customtkinter.CTkFrame(f01,height = 150,width = 270,fg_color = "#ffffff",border_width = 1,border_color = "lightgray")
f7.place(x = 8,y = 460)

label17 = customtkinter.CTkLabel(f7,text = "Registration",fg_color = "#ffffff",text_color = "#000000",font = customtkinter.CTkFont(size = 17,weight = "bold"))
label17.place(x = 20,y = 20)

label18 = customtkinter.CTkLabel(f7,text = "Invitee Conversion Rate",text_color = "#000000",font = customtkinter.CTkFont(size = 12,weight = "normal"))
label18.place(x = 20,y = 50)

label19 =  customtkinter.CTkLabel(f7,text = "0.0%",fg_color = "#ffffff",text_color = "#000000",font = customtkinter.CTkFont(size = 17,weight = "bold"))
label19.place(x = 20,y = 75)

img13 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\light-bulb.png"),size = (30,30))
labimg13 = customtkinter.CTkLabel(f7,image = img13,text = "")
labimg13.place(x = 15,y = 105)

label20 = customtkinter.CTkLabel(f7,text = "Set your event's deadline\nand capacity",text_color = "#3fa6fb",font = customtkinter.CTkFont(size = 12,weight = "normal"))
label20.place(x = 60,y = 105)

def butimg14():
    pass 

img14 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\ellipsis.png"),size = (30,20))
butimg14 = customtkinter.CTkButton(f7,image = img14,text = "",command = butimg14,width = 20,fg_color = "#ffffff",hover_color = "#ffffff")
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

f02 = ctk.CTkFrame(f01,height = 1050,width = 500,fg_color = "#F0F0F0")
f02.place(x = 567,y = 200)

def butimg16():
    pass 

img16 = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\right-arrow.png"),size = (30,30))
butimg16 = ctk.CTkButton(f02,image = img16,text = "",command = butimg16,fg_color = "#C8C6F3",hover_color = "#ffffff",width = 20)
butimg16.place(x = 400,y = 0)

label25 = ctk.CTkLabel(f02,text = "Feature Status",text_color = "black",fg_color = "#F0F0F0",font = ctk.CTkFont(size = 17,weight = "bold"))
label25.place(x = 15,y = 40)

img17 = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\pending.png"),size = (30,25))
labimg17 = ctk.CTkLabel(f02,image = img17,text = "")
labimg17.place(x = 150,y = 40)

label26 = ctk.CTkLabel(f02,text = "Registration",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 19,weight = "normal"))
label26.place(x = 15,y = 80)

label27 = ctk.CTkLabel(f02,text = "Pending",fg_color = "#FEEEAB",text_color = "#EB9E29",corner_radius = 3,height = 10,width = 10,padx = 2,pady = 2,font = ctk.CTkFont(size = 19))
label27.place(x = 350,y = 80)

canvas2 = Canvas(f02,height = 3,width = 620,bg = "gray",relief = RAISED)
canvas2.place(x = 15,y = 190)

label28 = ctk.CTkLabel(f02,text = "Search for attendees",text_color = "black",fg_color = "#F0F0F0",font = ctk.CTkFont(size = 17,weight = "bold"))
label28.place(x = 15,y = 150)

x10 = StringVar()
e2 = ctk.CTkEntry(f02,height = 30,width = 270,corner_radius = 15,fg_color = "#ffffff",text_color = "black",placeholder_text = "Enter a name or email",placeholder_text_color = "black",textvariable = x10)
e2.place(x = 15,y = 190)

def butimg18():
    pass 

img18 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\loupe.png"),size = (10,10))
butimg18 = customtkinter.CTkButton(e2,image = img7,text = "",fg_color = "white",hover_color = "#ffffff",corner_radius = 3,height = 10,width = 10,command = butimg18)
butimg18.place(x = 228,y = 3)

canvas3 =  Canvas(f02,height = 3,width = 620,bg = "gray",relief = RAISED)
canvas3.place(x = 15,y = 360)

label29 = ctk.CTkLabel(f02,text = "Event Information",text_color = "black",fg_color = "#F0F0F0",font = ctk.CTkFont(size = 17,weight = "bold"))
label29.place(x = 15,y = 260)

label30 = ctk.CTkLabel(f02,text = "Event Code",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
label30.place(x = 15,y = 310)

x11 = StringVar()
x11.set("BAMMCYD")
label31 = ctk.CTkLabel(f02,fg_color = "#F0F0F0",text_color = "#000000",textvariable = x11,font = ctk.CTkFont(size = 12,weight = "bold"))
label31.place(x = 15,y = 330)

label32 = ctk.CTkLabel(f02,text = "Event Format",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
label32.place(x = 15,y = 380)

x12 = StringVar()
x12.set("Hybrid")
label33 = ctk.CTkLabel(f02,fg_color = "#F0F0F0",text_color = "#000000",textvariable = x12,font = ctk.CTkFont(size = 12,weight = "bold"))
label33.place(x = 15,y = 400)

label34 = ctk.CTkLabel(f02,text = "Registration Capacity",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
label34.place(x = 15,y = 450)

x13 = StringVar()
x13.set("In Person:Unlimited | Virtual:Unlimited")
label35 = ctk.CTkLabel(f02,fg_color = "#F0F0F0",text_color = "#000000",textvariable = x13,font = ctk.CTkFont(size = 12,weight = "bold"))
label35.place(x = 15,y = 472)

label36 = ctk.CTkLabel(f02,text = "Registration Deadline",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
label36.place(x = 15,y = 520)

x14 = StringVar()
x14.set("30/7/2024 9:59 pm IST")
label37 = ctk.CTkLabel(f02,fg_color = "#F0F0F0",text_color = "#000000",textvariable = x14,font = ctk.CTkFont(size = 12,weight = "bold"))
label37.place(x = 15,y = 542)

label38 = ctk.CTkLabel(f02,text = "Planner",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
label38.place(x = 15,y = 590)

x15 = StringVar()
x15.set("Lucky Tungariya")
label39 = ctk.CTkLabel(f02,fg_color = "#F0F0F0",text_color = "#000000",textvariable = x15,font = ctk.CTkFont(size = 12,weight = "bold"))
label39.place(x = 15,y = 610)

label40 = ctk.CTkLabel(f02,text = "Planner's Email",fg_color = "#F0F0F0",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
label40.place(x = 15,y = 660)

x16 = StringVar()
x16.set("send@gmail.com")
label41 = ctk.CTkLabel(f02,fg_color = "#F0F0F0",text_color = "#000000",textvariable = x16,font = ctk.CTkFont(size = 12,weight = "bold"))
label41.place(x = 15,y = 680)

root.mainloop()