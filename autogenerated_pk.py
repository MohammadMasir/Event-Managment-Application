'''import pymysql as psql
mycon = psql.connect(host = "localhost",user = "root",password = "root",port = 3307,charset = "utf8",db = "lucky")
cur = mycon.cursor()
from tkinter import *
from tkinter.messagebox import *
screen = Tk()
screen.title("GUI PROGRAMMING")
screen.geometry("500x500")
f1 = Frame(screen,bg = "gray",height = 100,width = 473)
f1.place(x = 12,y = 10)
l1 = Label(f1,text = "SBI REGISTRATION",fg = "blue",bg = "pink",font = ("Arial",35))
l1.place(x = 14,y = 18)
f2 = Frame(screen,bg = "#31B8C9",height = 300,width = 473)
f2.place(x = 12,y = 130)
l2 = Label(f2,text = "CUSTOMER ID:",fg = "black",bg = "white",height = 1,width = 17)
l2.place(x = 10,y = 30)
x = IntVar()
entry1 = Entry(f2,textvariable = x,state = "disabled")
entry1.place(x = 150,y = 30)
l3 = Label(f2,text = "CUSTOMER NAME:",fg = "black",bg = "white",height = 1,width = 17)
l3.place(x = 10,y = 120)
y = StringVar()
entry2 = Entry(f2,textvariable = y)
entry2.place(x = 150,y = 120)
def process():
    if y.get():
        id = x.get()
        name = y.get()
        qstring1 = f"insert into customer_details values({id},'{name}')"
        cur.execute(qstring1)
        showinfo(
            title = "Successful message",
            message = "Your data inserted successfully"
            )
        entry1.configure(state = "disabled")
        entry2.configure(state = "disabled")
        b1.configure(state = "disabled")
    else:
        showerror(
            title = "Error",
            message = "Please fill full details"
            )
b1 = Button(f2,text = "SUBMIT",fg = "black",bg = "white",cursor = "hand2",height = 1,width = 7,command = process)
b1.place(x = 150,y = 220)
screen.mainloop()'''


import pymysql as psql
from tkinter import *
from tkinter.messagebox import *

mycon = psql.connect(host="localhost", user="root", password="root", port=3307, charset="utf8", db="lucky")
cur = mycon.cursor()

screen = Tk()
screen.title("GUI PROGRAMMING")
screen.geometry("500x500")

f1 = Frame(screen, bg="gray", height=100, width=473)
f1.place(x=12, y=10)
l1 = Label(f1, text="SBI REGISTRATION", fg="blue", bg="pink", font=("Arial", 35))
l1.place(x=14, y=18)

f2 = Frame(screen, bg="#31B8C9", height=300, width=473)
f2.place(x=12, y=130)

l2 = Label(f2, text="CUSTOMER ID:", fg="black", bg="white", height=1, width=17)
l2.place(x=10, y=30)
x = IntVar()
entry1 = Entry(f2, textvariable=x)
entry1.place(x=150, y=30)

l3 = Label(f2, text="CUSTOMER NAME:", fg="black", bg="white", height=1, width=17)
l3.place(x=10, y=80)
y = StringVar()
entry2 = Entry(f2, textvariable=y)
entry2.place(x=150, y=80)

def process():
    if y.get():
        id = x.get()
        name = y.get()
        # Insert the record into the database
        cur.execute(f"INSERT INTO customer_details (id, name) VALUES ({id}, '{name}')")
        mycon.commit()
        entry1.delete(0, END)
        entry2.delete(0, END)
        showinfo(
            title="Successful message",
            message="Your data inserted successfully"
        )
    else:
        showerror(
            title="Error",
            message="Please fill in all details"
        )

b1 = Button(f2, text="SUBMIT", fg="black", bg="white", cursor="hand2", height=1, width=7, command=process)
b1.place(x=150, y=220)

screen.mainloop()

