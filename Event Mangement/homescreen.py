import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image

root = customtkinter.CTk()
root.configure(fg_color = "#F0F0F0")
root.geometry("800x800")
root.title("Home Screen")


'''f0 = customtkinter.CTkScrollableFrame(root,height = 900,width = 1300,fg_color = "#F0F0F0")
f0.place(x = 250,y = 82)
'''

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

img1 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\loupe.png"),size = (20,20))
butimg1 = customtkinter.CTkButton(f1,image = img1,fg_color = "white",width = 20,text = "",hover_color = "#3fa6fb",command = butimg1)
butimg1.place(x = 1040,y = 5)

def butimg2():
    pass 

img2 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\file.png"),size = (20,20))
butimg2 = customtkinter.CTkButton(f1,image = img2,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg2)
butimg2.place(x = 1090,y = 5)

def butimg3():
    pass

img3 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\question.png"),size = (20,20))
butimg3 = customtkinter.CTkButton(f1,image = img3,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg3)
butimg3.place(x = 1140,y = 5)

def butimg4():
    pass

img4 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\user (1).png"),size = (20,20))
butimg4 = customtkinter.CTkButton(f1,image = img4,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg4)
butimg4.place(x = 1190,y = 5)

def butimg5():
    pass

img5 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\menu.png"),size = (20,20))
butimg5 = customtkinter.CTkButton(f1,image = img5,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg5)
butimg5.place(x = 1240,y = 5)

canvas1 = Canvas(root,height = 3,width = 1920,bg = "#0061ff",relief = RAISED)
canvas1.place(x = 0,y = 56)

f2 = customtkinter.CTkFrame(root,height = 44,width = 1300,fg_color = "white")
f2.place(x = 0,y = 41)

def butimg6():
    pass

img6 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\lines.png"),size = (20,20))
butimg6 = customtkinter.CTkButton(f2,image = img6,text = "",fg_color = "white",width = 20,hover_color = "white",command = butimg6)
butimg6.place(x = 6,y = 5)

label5 = customtkinter.CTkLabel(f2,text = "DemEven",text_color = "black",font = (customtkinter.CTkFont(size = 15,weight = "normal")))
label5.place(x = 47,y = 5)

x3 = StringVar()
e1 = customtkinter.CTkEntry(f2,height = 28,width = 250,fg_color = "white",corner_radius = 15,placeholder_text = "Search this Event",placeholder_text_color = "gray",text_color = "black",textvariable = x3)
e1.place(x = 1000,y = 5)

def butimg7():
    pass

img7 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\loupe.png"),size = (20,15))
butimg7 = customtkinter.CTkButton(f2,image = img7,text = "",fg_color = "white",width = 20,border_width = 1,border_color = "black",hover_color = "#8BFAFF",command = butimg7)
butimg7.place(x = 958,y = 5)

f3 = customtkinter.CTkFrame(root,fg_color = "white",height = 600,width = 250,border_width = 1,border_color = "lightgray")
f3.place(x = 0,y = 81)

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

f4 = customtkinter.CTkFrame(root,height = 220,width = 1150,fg_color = "white",border_width = 1,border_color = "lightgray")
f4.place(x = 249,y = 82)

label7 = customtkinter.CTkLabel(f4,text = "DemEven",fg_color = "white",text_color = "black",font = customtkinter.CTkFont(size = 25,weight = "bold"))
label7.place(x = 20,y = 80)

label8 = customtkinter.CTkLabel(f4,text = "Upcoming",fg_color = "#FEEEAB",text_color = "#EB9E29",corner_radius = 3,height = 10,width = 10,padx = 2,pady = 2)
label8.place(x = 20,y = 140)

img8 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\calendar.png"),size = (20,20))
labimg8 = customtkinter.CTkLabel(f4,image = img8,text = "")
labimg8.place(x = 120,y = 137)

label9 = customtkinter.CTkLabel(f4,text = "30/7/2024  6:00 pm - 10:00 pm  IST (61 days away)",text_color = "black",font = customtkinter.CTkFont(size = 13,weight = "normal"))
label9.place(x = 150,y = 137)

img9 = customtkinter.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\Event Mangement\location.png"),size = (20,20))
labimg9 = customtkinter.CTkLabel(f4,image = img9,text = "")
labimg9.place(x = 500,y = 137)

label10 = customtkinter.CTkLabel(f4,text = "Chicago",text_color = "black",font = customtkinter.CTkFont(size = 13,weight = "normal"))
label10.place(x = 522,y = 137)

x9 = StringVar()
x9.set("Actions")
opt8 = customtkinter.CTkComboBox(f4,height = 35,width = 150,variable = x9,fg_color = "white",button_hover_color = "#4B9EFC",border_width = 1,border_color = "lightgray",corner_radius = 7,dropdown_hover_color = "#4B9EFC",button_color = "lightgray",text_color = "#4B9EFC",values = ["","","",""])
opt8.place(x = 800,y = 96)
root.mainloop()