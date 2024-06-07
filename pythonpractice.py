'''f = open("C:\\Users\\lucky\\OneDrive\\Pictures\\Documents\\open.txt","r")
print(f.read())
#open_file = f.read()
f.close()'''


'''f1 = open("C:\\Users\\lucky\\OneDrive\\Pictures\\Documents\\open.txt","r")
open_file = f1.read()
print(open_file)
f1.close()'''


'''import pandas as pd
import matplotlib.pyplot as plt
data = {"name":["lucky","Hansraj","narayan","surendra"],"marks":[35,45,55,65]}
df = pd.DataFrame(data)
print(df)
df.plot(kind = "bar",x = "name",y = "marks",color = "blue")
plt.show()'''

'''import pandas as pd
#import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\lucky\\OneDrive\\Pictures\\Documents\\house1.csv")
print(df[df["price"]>200000])
df.plot(kind = "hist",x = "bedrooms",y = "price",color = "red")
plt.show()'''


'''f1 = open("C:\\Users\\lucky\\OneDrive\\Pictures\\Documents\\open.txt","r")
content_read = f1.readlines()
print(content_read)
f1.close()'''

'''import pandas as pd
data = {"empno":[1,2,3,4,5],"name":["Lucky","hansraj","dhruv","narayan","gautam"],"designation":['developer','HR','manager','executive','PR'],"salary":[200000,130000,500000,230000,150000]}
df = pd.DataFrame(data)
print(df[["name","salary"]])'''

#File handling....

'''files = ["database.py","dataframe.py","dsa.py","gui.py","combobox.py"]
list1 = []
module = input("Enter the name of module:")
for i in range(len(files)):
    f1 = open(files[i],"r")
    read_f1 = f1.read()
    if module in read_f1:
        list1.append(files[i])
        f1.close()
if len(list1) == 0:
    print("Your module name is not found in any python files")
print(list1)'''

#Best students Csv....

'''import csv
f1 = open("beststudents.csv","a")
csv_write = csv.writer(f1)
rollno = int(input("Enter your rollno:"))
name = input("Enter your name:")
classes = input("Enter your class:")
email = input("Enter your email:")
csv_write.writerow([rollno,name,classes,email])
f1.close()

f2 = open("beststudents.csv","r")
content = f2.read()
print(content)
f2.close()'''

'''import re
try:
    usr = input("Enter the username in only characters:")
    aadh = int(input("Enter your aadhar card number(12 digit):"))
    pan = input("Enter your pancard number:(10 digit):")
    dob = input("Enter your dob in foramt(dd/mm/yyyy):")

    x = re.match(r"^[a-zA-Z]+$",usr)
    y = re.match(r"^[0-9]{12}$",str(aadh))
    z = re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$",pan)
    p = re.match(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$",dob)

    if None in (x,y,z,p):
        raise Exception("Invalid input")

except Exception as e:
    print(e)

else:
    try:
        f1 = open("open.txt","a")
        usr_write = f1.write(usr+"\n")
        aadh_write = f1.write(str(aadh)+"\n")
        pan_write = f1.write(pan+"\n")
        dob_write = f1.write(dob+"\n")
        f1.close()
    except Exception as e:
        print("File opening error:",e)
    else:
        f2 = open("open.txt","r")
        print(f2.read())
        f2.close()'''

'''import pymysql as psql
mycon = psql.connect(host = "localhost",user = "root",password = "root",port = 3307,charset = "utf8",database = "practical")
cur = mycon.cursor()
print("1.INSERT\n 2.TOTAL")
choice = int(input("Enter your choice:"))
try:
    if choice == 1:
        rollno = int(input("Enter your rollno:"))
        name = input("Enter your name:")
        class1 = input("Enter your class:")
        qstring = f"insert into studentinfo values({rollno},'{name}','{class1}')"
        cur.execute(qstring)
        mycon.commit()
        print("Data added successfully")
        

    elif choice == 2:
        qstring1 = f'select count(*) from studentinfo'
        cur.execute(qstring1)
        x = cur.fetchall()
        print("Total number of students are:",x)
        

except Exception as e:
    print(e)

else:
    mycon.close()'''


'''import pymysql as psql
mycon = psql.connect(host = "localhost",user = "root",password = "root",charset = "utf8",port = 3307,database = "practical")
cur = mycon.cursor()
print("1.REGISTER\n 2.LOGIN")
try:
    main = int(input("enter your choice here:"))
    if main == 1:
        user = input("Enter your username:")
        password = input("Enter your password:")
        repass = input("Enter your password again:")
        qstring = f"select user from customer where user = '{user}'"
        cur.execute(qstring)
        x = cur.fetchall()
        print(x)
        if x:
            print(f"Username {user} already exist")
        elif password!=repass:
            print("Your password and confirm password are not same")
        else:
            qstring1 = f"insert into customer values('{user}','{password}','{repass}')"
            cur.execute(qstring1)
            print("Data added successfully")
            mycon.commit()

    elif main == 2:
        user = input("Enter your username:")
        password = input("Enter your password:")
        qstring = f"select user,password from customer where user = '{user}' and password = '{password}'"
        cur.execute(qstring)
        x = cur.fetchall()
        if x:
            print("Your data exist in table")
        else:
            print("Your data does not exist in table")

except Exception as e:
    print(e)

else:
    mycon.close()'''

#Tkinter....
'''from tkinter import *
from tkinter.messagebox import *
def onclick():
    p = var1.get()
    n = var2.get()
    r = var3.get()
    p1 = int(p)
    n1 = int(n)
    r1 = int(r)
    SI = (p1*n1*r1)/100
    showinfo(title = "calculated SI",
    message = "Your SI is amount"+str(SI))
screen = Tk()
screen.title("simple Interest calculator")
screen.configure(bg = "#F36A88")
screen.geometry("500x500")
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
l1 = Label(screen,text = "Principal amount:",fg = "black",bg = "white")
entry1 = Entry(screen,textvariable = var1)
l2 = Label(screen,text = "Rate of interest:",fg = "black",bg = "white")
entry2 = Entry(screen,textvariable = var2)
l3 = Label(screen,text = "Time period:",fg = "black",bg = "white")
entry3 = Entry(screen,textvariable = var3)
b1 = Button(screen,text = "Calculate",fg = "black",bg = "white",command = onclick)
l1.grid(row = 0,column = 0)
entry1.grid(row = 0,column = 1)
l2.grid(row = 1,column = 0,pady = 10)
entry2.grid(row = 1,column = 1,pady = 10)
l3.grid(row = 3,column = 0,pady = 20)
entry3.grid(row = 3,column = 1,pady = 20)
b1.grid(row = 4,columnspan = 2)
screen.mainloop()'''

'''from tkinter import *
def clickme():
    var.set("PYTHON")
    e1.configure(font = "Bold")
    b1.configure(state = "disabled")
root = Tk()
root.geometry("500x500")
root.configure(bg = "#F36A88")
var = StringVar()
e1 = Entry(root,textvariable = var)
var.set("LUCKY")
b1 = Button(root,text = "Click me!!",fg = "black",bg = "white",command = clickme)
e1.pack()
b1.pack()
root.mainloop()'''

'''from tkinter import *
from tkinter.messagebox import *
def sel():
    selection = "You selected the option" +str(var.get())
    showinfo(title = "Message",
    message = selection)
screen = Tk()
screen.geometry("500x500")
screen.configure(bg = "#F36A88")
screen.title("Radio button")
var = IntVar()
r1 = Radiobutton(screen,text = "FYCS",variable = var,value = 1,command = sel)
r2 = Radiobutton(screen,text = "SYCS",variable = var,value = 2,command = sel)
r3 = Radiobutton(screen,text = "TYCS",variable = var,value = 3,command = sel)
r1.pack()
r2.pack()
r3.pack()
screen.mainloop()'''

'''from tkinter import *
from tkinter.messagebox import showinfo
def sel():
    showinfo(title = "Message",
    message = "You selected the option"+str(var1.get))
screen = Tk()
screen.geometry("500x500")
screen.configure(bg = "#F36A88")
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
c1 = Checkbutton(screen,text = "PIZZA",variable = var1,onvalue = 1,offvalue = 0,command = sel)
c2 = Checkbutton(screen,text = "MAGGI",variable = var2,onvalue = 1,offvalue = 0,command = sel)
c3 = Checkbutton(screen,text = "VEG EXTRAVAGANDE",variable = var3,onvalue = 1,offvalue = 0,command = sel)
c1.pack()
c2.pack()
c3.pack()
screen.mainloop()'''

'''from tkinter import *
from tkinter.messagebox import *
from datetime import date
def sel():
    today = date.today()
    current_year = int(today.strftime("%Y"))
    current_date = int(today.strftime("%d"))
    current_month = int(today.strftime("%m"))
    n1 =  var1.get()
    y1 = var4.get()
    d1 = var2.get()
    m1 = var3.get()
    age = current_year - y1
    if age>18:
        showinfo(title = "Message",
        message = "Your age is :" +str(age))
    else:
        showerror(title = "Message",
        message = "Your age is below 18")
    
    if (d1 == current_date) and (m1 == current_month):
        showinfo(title = "wishings",
        message = "Happy Birthday "+n1) 
root = Tk()
root.configure(bg = "#F36A88")
root.geometry('500x500')
var1 = StringVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
l1 = Label(root,text = "Name:",fg = "black",bg = "white")
e1 = Entry(root,textvariable = var1)
l2 = Label(root,text = "Enter the date:",fg = "black",bg = "white")
e2 = Entry(root,textvariable = var2)
l3 = Label(root,text = "Enter the month:",fg = "black",bg = "white")
e3 = Entry(root,textvariable = var3)
l4 = Label(root,text = "Enter the year(YYYY):",fg = "black",bg = "white")
e4 = Entry(root,textvariable = var4)
b1 = Button(root,text = "Submit",fg = "black",bg = "white",command = sel)
l1.place(x = 100,y = 10)
e1.place(x = 150,y = 10)
l2.place(x = 100,y = 50)
e2.place(x = 200,y = 50)
l3.place(x = 100,y = 100)
e3.place(x = 200,y = 100)
l4.place(x = 100,y = 150)
e4.place(x = 220,y = 150)
b1.place(x = 180,y = 180)
root.mainloop()'''

'''from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
root = Tk()
root.geometry("500x500")
root.configure(bg = "#F36A88")
root.resizable("True","True")
var = StringVar()
c1 = ttk.Combobox(root,textvariable = var,state = "readonly",height = 5)
c1['values'] = ['JAN','FEB','MAR','APR','MAY']
def select(event):
    showinfo(title = "Message",
    message = "You selected the month"+var.get())
c1.bind("<<ComboboxSelected>>",select)
c1.pack()
root.mainloop()'''

'''from tkinter import *
from tkinter.messagebox import showinfo
root = Tk()
root.geometry("500x500")
values = ['PYTHON','JAVA','C++','GO']
var = StringVar(value = values)
listbox = Listbox(root,listvariable = var,selectmode = EXTENDED)
def items_selected(event):
    selection = listbox.curselection()
    values_selected = ",".join([listbox.get(i) for i in selection])
    showinfo(title = "Message",
    message = "You selected the languages"+values_selected)
listbox.pack()
listbox.bind("<<ListboxSelect>>",items_selected)
root.mainloop()'''

'''from tkinter import *
from tkinter.messagebox import askyesno
screen = Tk()
screen.geometry("200x200")
screen.configure(bg = "white")
def sel():
    answer = askyesno(title = "Ask question",
    message = "Do you want to quit?")
    if answer:
        screen.destroy()
b1 = Button(screen,text = "ASk YES/NO",command = sel)
b1.pack(anchor = E,fill = X)
screen.mainloop()

import socket             
 
# next create a socket object 
s = socket.socket()         
print ("Socket successfully created")
 
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345               
 
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
 
# put the socket into listening mode 
s.listen(5)     
print ("socket is listening")            
 
# a forever loop until we interrupt it or 
# an error occurs 
while True: 
 
# Establish connection with client. 
  c, addr = s.accept()     
  print ('Got connection from', addr )
 
  # send a thank you message to the client. encoding to send byte type. 
  c.send('Thank you for connecting'.encode()) 
 
  # Close the connection with the client 
  c.close()
   
  # Breaking once connection closed
  break


#client....
import socket             
 
# Create a socket object 
s = socket.socket()         
 
# Define the port on which you want to connect 
port = 12345               
 
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
 
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection 
s.close()'''   














