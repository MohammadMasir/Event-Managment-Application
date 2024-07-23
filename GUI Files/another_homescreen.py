import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

root = ctk.CTk()
root.configure(fg_color = "#ffffff")
root.geometry("800x800")
root.title("Another homescreen")

f1 = ctk.CTkFrame(root,height = 41,width = 1300,fg_color = "white")
f1.place(x = 0,y = 0)

label1 = ctk.CTkLabel(f1,text = "cvent",text_color = "black",justify = "right",font = ctk.CTkFont(size =  20,weight = "bold"))
label1.place(x = 15,y = 5)

label2 = ctk.CTkLabel(f1,text = "",width = 2,height = 20,fg_color = "black")
label2.place(x = 80,y = 9.5)

label3 = ctk.CTkLabel(f1,text = "EVENTS",text_color = "#3fa6fb",font = ctk.CTkFont(size = 17,weight = "bold"))
label3.place(x = 95,y = 5)

label4 = ctk.CTkLabel(f1,text = "All Events",text_color = "black",font = ctk.CTkFont(size = 17,weight = "normal"))
label4.place(x = 420,y = 5)

x1 = tk.StringVar()
x1.set("Calendar")
opt1 = ctk.CTkComboBox(f1,variable = x1,height = 35,width = 150,fg_color = "white",text_color = "black",border_color = "white",button_color = "white",button_hover_color = "white",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["Events calendar","Internal calendar"])
opt1.place(x = 540,y = 5)

x2 = tk.StringVar()
x2.set("More")
opt2 = ctk.CTkComboBox(f1,variable = x2,height = 35,width = 150,fg_color = "white",text_color = "black",border_color = "white",button_color = "white",button_hover_color = "white",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","",""])
opt2.place(x = 700,y = 5)

def butimg1():
    pass

img1 = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\loupe.png"),size = (20,20))
butimg1 = ctk.CTkButton(f1,image = img1,fg_color = "white",width = 20,text = "",hover_color = "#3fa6fb",command = butimg1)
butimg1.place(x = 1040,y = 5)

def butimg2():
    pass 

img2 = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\file.png"),size = (20,20))
butimg2 = ctk.CTkButton(f1,image = img2,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg2)
butimg2.place(x = 1090,y = 5)

def butimg3():
    pass

img3 = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\question.png"),size = (20,20))
butimg3 = ctk.CTkButton(f1,image = img3,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg3)
butimg3.place(x = 1140,y = 5)

def butimg4():
    pass

img4 = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\user (1).png"),size = (20,20))
butimg4 = ctk.CTkButton(f1,image = img4,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg4)
butimg4.place(x = 1190,y = 5)

def butimg5():
    pass

img5 = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\menu.png"),size = (20,20))
butimg5 = ctk.CTkButton(f1,image = img5,text = "",fg_color = "white",width = 20,hover_color = "#3fa6fb",command = butimg5)
butimg5.place(x = 1240,y = 5)

canvas1 = tk.Canvas(root,height = 3,width = 1920,bg = "#0061ff",relief = tk.RAISED)
canvas1.place(x = 0,y = 56)

label15 = ctk.CTkLabel(root,text = "Events",text_color = "#000000",font = ctk.CTkFont(size = 20,weight = "bold"))
label15.place(x = 15,y = 65)

def create_event():
    pass

create_event_button = ctk.CTkButton(root,text = "Create Event",height = 30,width = 40,fg_color = "#2380D2",text_color = "#ffffff",corner_radius = 7,command = create_event)
create_event_button.place(x = 1140,y = 65)

main_frame = ctk.CTkFrame(root,height = 520,width = 1280,fg_color = "#E6E6E6")
main_frame.place(x = 0,y = 130)

x3 = tk.StringVar()
x3.set("Current Events")
current_events_opt = ctk.CTkComboBox(main_frame,variable = x3,height = 35,width = 140,fg_color = "#E6E6E6",text_color = "black",button_color = "#E6E6E6",border_color = "#E6E6E6",button_hover_color = "#E6E6E6",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
current_events_opt.place(x = 30,y = 30)

def create_view():
    pass

create_view_button = ctk.CTkButton(main_frame,text = "Create View",text_color = "#000000",hover_color = "#A4A4A4",width = 100,fg_color = "#E6E6E6",command = create_view)
create_view_button.place(x = 180,y = 35)

advanced_search_label = ctk.CTkLabel(main_frame,text = "Advanced Search",text_color = "#000000")
advanced_search_label.place(x = 1140,y = 35)

child_frame = ctk.CTkFrame(main_frame,fg_color = "#ffffff",height = 250,width = 1235)
child_frame.place(x = 20,y = 130)

inner_frame1 = ctk.CTkFrame(child_frame,height = 130,width = 1175,fg_color = "#ffffff",border_width = 0.8,border_color = "#919191")
inner_frame1.place(x = 30,y = 20)

title_label = ctk.CTkLabel(inner_frame1,text = "Title",text_color = "#000000",font = ctk.CTkFont(size = 14,weight = "normal"))
title_label.place(x = 20,y = 10)

x4 = tk.StringVar()
x4.set("Code")
code_dropdown = ctk.CTkComboBox(inner_frame1,variable = x4,height = 35,width = 100,fg_color = "#ffffff",text_color = "#000000",button_color = "#ffffff",border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
code_dropdown.place(x = 450,y = 10)

x5 = tk.StringVar()
x5.set("Event Status")
event_status_dropdown = ctk.CTkComboBox(inner_frame1,variable = x5,height = 35,width = 140,fg_color = "#ffffff",text_color = "#000000",button_color = "#ffffff",border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
event_status_dropdown.place(x = 590,y = 10)

x6 = tk.StringVar()
x6.set("Start Date")
start_date_dropdown = ctk.CTkComboBox(inner_frame1,variable = x6,height = 35,width = 140,fg_color = "#ffffff",text_color = "#000000",button_color = "#ffffff",border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
start_date_dropdown.place(x = 750,y = 10)

x7 = tk.StringVar()
x7.set("Yes")
yes_dropdown = ctk.CTkComboBox(inner_frame1,variable = x7,height = 35,width = 90,fg_color = "#ffffff",text_color = "#000000",button_color = "#ffffff",border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["","","","",""])
yes_dropdown.place(x = 920,y = 10)

img6 = ctk.CTkImage(dark_image = Image.open(r"C:\Users\lucky\OneDrive\Desktop\python programs\pics\question.png"),size = (20,20))
labimg6 = ctk.CTkLabel(inner_frame1,image = img6,text = "")
labimg6.place(x = 1050,y = 10)

no_label = ctk.CTkLabel(inner_frame1,text = "No",text_color = "#000000",font = ctk.CTkFont(size = 12,weight = "normal"))
no_label.place(x = 1090,y = 10)

canvas2 = tk.Canvas(inner_frame1,height = 3,width = 1900,bg = "#858585",relief = tk.SUNKEN)
canvas2.place(x =  -2,y = 70)

inner_frame2 = ctk.CTkFrame(inner_frame1,height = 78,width = 1172,fg_color = "#E6E6E6")
inner_frame2.place(x = 1,y = 50)

x8 = tk.StringVar()
text = "There are no events in this view."
x8.set(text)
data_label = ctk.CTkLabel(inner_frame2,text_color = "#000000",textvariable = x8,font = ctk.CTkFont(size = 15,weight = "bold"))
data_label.place(x = 500,y = 10)

result_per_page_label = ctk.CTkLabel(child_frame,text = "Results per page",fg_color = "#ffffff",text_color = "#000000",font = ctk.CTkFont(size = 13,weight = "normal"))
result_per_page_label.place(x = 30,y = 170)

x9 = tk.IntVar()
result_per_page_dropdown = ctk.CTkComboBox(child_frame,variable = x9,height = 35,width = 60,fg_color = "#ffffff",text_color = "#000000",border_width = 0.6,button_color = "#ffffff",corner_radius = 5,border_color = "#ffffff",button_hover_color = "#ffffff",font = ctk.CTkFont(size = 13,weight = "normal"),values = ["25","30","35","40"])
result_per_page_dropdown.place(x = 180,y = 170)

x10 = tk.StringVar()
text = "Displaying result 0 of 0"
x10.set(text)
displaying_result_label = ctk.CTkLabel(child_frame,textvariable = x10,text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
displaying_result_label.place(x = 600,y = 170)

down_line = tk.Canvas(main_frame,height = 9,width = 1920,bg = "#858585",relief = tk.SUNKEN)
down_line.place(x = -2,y = 768)
root.mainloop()