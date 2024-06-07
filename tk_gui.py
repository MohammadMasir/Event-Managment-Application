'''from tkinter import *
root = Tk()
root.title('Distance converter')
root.geometry('500x500')
root.configure(bg = 'lightgreen')
def ftin_converter():
    num1 = x.get()
    num2 = y.get()
    foot_convert = num2*0.0833
    add_of_no = num1+foot_convert
    ans1 = add_of_no*30.48
    z.set(ans1)
def centimeter_converter():
    num3 = z.get()
    ans2 = num3/30.48
    ans3 = num3/2.54
    x.set(ans2)
    y.set(ans3)
x = IntVar()
x.set(100)
y = IntVar()
y.set(100)
z = IntVar()
z.set(100)
l1 = Label(root,text = 'ft:',fg = 'white',bg = 'black')
entry1 = Entry(root,textvariable = x)
l2 = Label(root,text = 'inch:',fg = 'white',bg = 'black') 
entry2 = Entry(root,textvariable = y)
l3 = Label(root,text = 'centi',fg = 'white',bg = 'black')
entry3 = Entry(root,textvariable = z)
b1 = Button(root,text = 'ft,inches to centimeters',command = ftin_converter)
b2 = Button(root,text = 'centimeters to ft,inches',command = centimeter_converter)
l1.grid(row = 0,column = 0,padx =20)
entry1.grid(row = 0,column = 1)
l2.grid(row = 0,column = 2,padx = 20)
entry2.grid(row = 0,column = 3)
l3.grid(row = 1,column = 1,pady = 20)
entry3.grid(row = 1,column = 2,padx = 0)
b1.grid(row = 2,column = 1)
b2.grid(row = 2,column = 2,padx = 20)
root.mainloop()'''
#------------------------------------------------------------------------------------>
 #Write a  program to accept user's name in text box.
 #Also accept date of birth using three text boxes containing date, month and year values.
 #Calculate age of user in years.
 #If user is above 18, display appropriate message or display error message.
 #Also display happy birthday message if users date of birth matches today's date.

'''2. Design a Sports Registration Form with following elements - 
(i) textboxes for Name, roll & class 
(ii) List box containing names of sports events
(iii) Radio button for Team Name 
On click of button, this information should be stored in a sql table
called SportsReg containing columns like roll, name, class, team, sports'''

'''from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo,askokcancel,showerror
def operation():
    selected_value = []
    import pymysql as psql
    myconn = psql.connect(host = 'localhost',user = 'root',password = 'root',port = 3307,charset = 'utf8')
    cur = myconn.cursor()
    cur.execute(f'use lucky')
    name1 = x.get()
    roll1 = y.get()
    class1 = z.get()
    selected_radio_button = var.get()
    selected_index = lb.curselection()
    selected_game = ",".join(lb.get(i) for i in selected_index)
    qstring = f"select name,roll_no,division from sportreg where name = '{name1}' and roll_no = {roll1} and division = '{class1}'"
    qstring1 = f"insert into SportReg values('{name1}',{roll1},'{class1}','{selected_radio_button}','{selected_game}')"
    answer = askokcancel(title = "Confirm",
    message = "Do we insert this data?")
    if answer:
        cur.execute(qstring)
        x1 = cur.fetchall()
        if x1:
            showerror(title = "warning",
            message = "Sorry your data can't be inserted its already exist")
        else:
            cur.execute(qstring1)
            myconn.commit()
            myconn.close()
    else:
        showinfo(title = "Message",
        message = "OK,Your data is not inserted.")
root = Tk()
root.geometry("500x500")
f1 = Frame(root,bg = 'hotpink',height = 400,width = 350)
f2 = Frame(f1,bg = 'darkgray',height = 50,width = 250)
l1 = Label(f2,text = "SPORT REGISTRATION",fg = 'black',font = ("Arial"))
l2 = Label(f1,text = "NAME:",fg = 'black',font = ('Arial'),height = 1)
l3 = Label(f1,text = "ROLL NO:",fg = 'black',font = ('Arial'),height = 1)
l4 = Label(f1,text = "CLASS:",fg = 'black',font = ('Arial'),height = 1)
l5 = Label(f1,text = "CHOOSE THE GAME:",fg = 'black',font = ('Arial'),height = 1)
l6 = Label(f1,text = "CHOOSE YOUR TEAM:",fg = 'black',font = ("Arial",13))
x = StringVar()
y = IntVar()
z = StringVar()
var = StringVar()
r1 = Radiobutton(f1,text = "AGNI HOUSE",fg = 'black',font = ('Arial',9),height = 1,variable = var,value = "AGNI HOUSE")
r2 = Radiobutton(f1,text = "PRITHVI HOUSE",fg = 'black',font = ('Arial',9),height = 1,variable = var,value = "PRITHVI HOUSE")
r3 = Radiobutton(f1,text = "TIGER HOUSE",fg = 'black',font = ('Bold',9),height = 1,variable = var,value = "TIGER HOUSE")
entry1 = Entry(f1,textvariable = x)
entry2 = Entry(f1,textvariable = y)
entry3 = Entry(f1,textvariable = z)
values = ["Cricket","Hockey","Football","Chess","Carrom","Kabbaddi"]
var1 = StringVar(value = values)
lb = Listbox(f1,listvariable = var1,selectmode = MULTIPLE,width = 12)
l1.place(x = 10,y = 10)
l2.place(x = 50,y = 68)
l3.place(x = 50,y = 105)
l4.place(x = 50,y = 143)
l5.place(x = 50,y = 180)
l6.place(x = 50,y = 217)
f1.place(x = 75,y = 50)
f2.place(x = 50,y = 10)
entry1.place(x = 130,y = 68)
entry2.place(x = 157,y = 105)
entry3.place(x = 130,y = 143)
lb.place(x = 270,y = 180)
r1.place(x = 50,y = 253)
r2.place(x = 50,y = 283)
r3.place(x = 50,y = 312)
b1 = Button(f1,text = 'SUBMIT',fg = 'black',font = ('Arial',10),height = 1,command = operation)
b1.place(x = 50,y = 349)
root.mainloop()'''

'''b = print(print("a"))
print(b)'''

def add(a,b):
    return a+b
print(add(3,2))

def add(a,b,c):
    return a+b+c
print(add(2,3,4))



