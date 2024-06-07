'''from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("python for GUI")
root.configure(bg = "orange")
root.geometry("700x500")
label1 = Label(root,text = 'hello world!',fg = 'navyblue',bg = 'grey')
def onclick():
    str = input('enter the string here:')
    label1.configure(text = str)
button = Button(root,text = 'click here',fg = 'hotpink',bg = 'black',command = onclick)
label1.pack()
button.pack()
root.mainloop()'''


'''from tkinter import *
mainwindow = Tk()

mainwindow.configure(bg = 'pink')
mainwindow.geometry('500x500')

label3 = Label(mainwindow,text = 'Try it',fg = 'blue')
label1 = Label(mainwindow,text = 'enter the username:')
entry1 = Entry(mainwindow)
label2 = Label(mainwindow,text = 'enter the password:')
entry2 = Entry(mainwindow)

label1.grid(row = 0,column = 0)
entry1.grid(row = 0,column = 1)
label2.grid(row = 1,column = 0)
entry2.grid(row = 1,column = 1)
def onclick():
    if entry2 == 'admin':
        label3 = Label(mainwindow,text = 'login successful',fg = 'blue')
button = Button(mainwindow,fg ='white',bg = 'black',command = onclick)
label3.pack()
button.pack()

mainwindow.mainloop()'''

'''from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('500x500')
root.configure(bg = 'white')
def sel():
    messagebox.showinfo(title = 'message',message = 'user selected option'+str(x.get()))
x = IntVar()
r1 = Radiobutton(root,text = 'FYCS',fg = 'black',variable = x,value = 1,command = sel)
r2 = Radiobutton(root,text = 'SYCS',fg = 'black',variable = x,value = 2,command = sel)
r3 = Radiobutton(root,text = 'TYCS',fg = 'black',variable = x,value = 3,command = sel)
r1.pack(anchor = W)
r2.pack(anchor = W,pady = 50)
r3.pack(anchor = W,pady = 80)
root.mainloop()'''

'''from tkinter import *
#import tkinter as ttk
screen = Tk()
screen.title('Simple Checkbox')
screen.geometry('500x500')
screen.configure(bg = 'lightblue')
f1 = Frame(screen,bg = 'gray',height = 30,cursor = 'hand2')
f1.pack(anchor = N,fill = 'x',expand = True)
l1 = Label(f1,text = "Menu selection",fg = 'navy blue',bg = 'white')
l1.pack(side = LEFT,padx = 10,pady = 10)
c1 = Checkbutton(screen,text = 'Paneer tikka',fg = 'black')
c1.pack(anchor = SW,padx = 10,pady = 250)
c2 = Checkbutton(screen,text = 'Chicken legpiece',fg = 'black')
c2.pack(anchor = SW,padx = 10,pady = 50)
screen.mainloop()'''

'''from tkinter import *
screen = Tk()
screen.title('Simple Checkbox')
screen.geometry('500x500')
screen.configure(bg='lightblue')

# Create c1 Checkbutton
c1 = Checkbutton(screen, text='Paneer tikka', fg='black')
c1.pack(anchor=SW, padx=10, pady=250)

# Create c2 Checkbutton
c2 = Checkbutton(screen, text='Chicken legpiece', fg='black')
c2.pack(anchor=NW, padx=10, pady=10)

screen.mainloop()'''






