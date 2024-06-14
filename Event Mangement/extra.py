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
opt8 = customtkinter.CTkComboBox(f4,height = 35,width = 150,variable = x9,fg_color = "white",button_hover_color = "#4B9EFC",border_width = 1,border_color = "lightgray",corner_radius = 7,dropdown_hover_color = "#4B9EFC",button_color = "lightgray",text_color = "#0966F1",values = ["","","",""])
opt8.place(x = 800,y = 96)
