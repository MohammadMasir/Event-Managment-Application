from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
screen = Tk()
screen.geometry('500x500')
screen.title('PIZZA HUT')
screen.configure(bg = 'lightblue')
l0 = Label(screen,text = 'PIZZA HUT',fg = "black",bg = 'white')
l0.grid(row = 0,column = 2,padx = 0 ,pady = 0)
l1 = Label(screen,text = 'Prices : [Normal Pizza:100 , Cheese Pizza:200 , Gravy Pizza:300 , Non veg pizza:500]',fg = 'black',bg = 'white')
l1.grid(row = 1,column = 1,padx = 10,pady = 10)
l2 = Label(screen,text = 'Select your favourite pizza:',fg = 'black',bg = 'gray')
l2.grid(row = 2,column = 0,padx = 10,pady = 10)
var = StringVar()
combo = ttk.Combobox(screen,textvariable = var)
combo['values'] = ['Normal Pizza','CheesePizza','Gravy Pizza','Non veg pizza']
combo['state'] = 'readonly'
combo.grid(row = 2,column = 1,padx = 5)
l3 = Label(screen,text = 'Extra Toppings:',fg = 'black',bg = 'gray')
l3.grid(row = 3,column = 0,padx = 10,pady = 10)
var1 = IntVar()
c1 = Checkbutton(screen,text = 'Extra cheese',onvalue = 20,offvalue = 0,variable = var1,bg = 'gray')
c1.grid(row = 3,column = 1,padx = 10,pady = 10)
var2 = IntVar()
c2 = Checkbutton(screen,text = 'Extra pepper',onvalue = 10,offvalue = 0,variable = var2,bg = 'gray')
c2.grid(row = 3,column = 2,padx = 0,pady = 10)
l4 = Label(screen,text = 'Quantity Of Pizza:',fg = 'black',bg = 'gray')
l4.grid(row = 4,column = 0,padx = 10,pady = 10)
var3 = IntVar()
quantity = Entry(screen,textvariable = var3)
quantity.grid(row = 4,column = 1)
l5 = Label(screen,text = 'Total Bill',fg = 'black',bg = 'gray')
l5.grid(row = 5,column = 0,padx = 10,pady = 10)
var4 = IntVar()
bill = Entry(screen,textvariable = var4)
bill.grid(row = 5,column = 1,padx = 10,pady = 10)
def click():
    return selected()
b1 = Button(screen,text = 'Calculate bill',fg = 'black',bg = 'white',cursor = 'hand2',command = click)
b1.grid(row = 6,column = 1)
def selected():
    t1 = var.get()
    if t1 == 'Normal pizza':
        m1 = var3.get()
        p1 = 100*m1
        q1 = (18/100)*p1
        p1 = p1+q1
        var4.set(p1)
        if var1.get():
            p1 = p1+var1.get()
            q1 = p1*(18/100)
            p1 = p1+q1
            var4.set(p1)
        if var2.get():
            p1 = p1+var2.get()
            q1 = p1*(18/100)
            p1 = p1+q1
            var4.set(p1)
    elif t1 == 'CheesePizza':
        m2 = var3.get()
        p2 = 200*m2
        q2 = p2*(18/100)
        p2 = p2+q2
        var4.set(p2)
        if var1.get():
            p2 = p2+var1.get()
            q2 = p2*(18/100)
            p2 = p2+q2
            var4.set(p2)
        if var2.get():
            p2 = p2+var2.get()
            q2 = p2*(18/100)
            p2 = p2+q2
            var4.set(p2)
    elif t1 == 'Gravy Pizza':
        m3 = var3.get()
        p3 = 300*m3
        q3 = p3*(18/100)
        p3 = p3+q3
        var4.set(p3)
        if var1.get():
            p3 = p3+var1.get()
            q3 = p3*(18/100)
            p3 = p3+q3
            var4.set(p3)
        if var2.get():
            p3 = p3+var2.get()
            q3 = p3*(18/100)
            p3 = p3+q3
            var4.set(p3)
    else:
        m4 = var3.get()
        p4 = 500*m4
        q4 = p4*(18/100)
        p4 = p4+q4
        var4.set(p4)
        if var1.get():
            p4 = p4+var1.get()
            q4 = p4*(18/100)
            p4 = p4+q4
            var4.set(p4)
        if var2.get():
            p4 = p4+var2.get()
            q4 = p4*(18/100)
            p4 = p4+q4
            var4.set(p4)
combo.bind('<<ComboboxSelected>>',selected)
screen.mainloop()