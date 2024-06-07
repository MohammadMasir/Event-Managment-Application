'''from tkinter import * 
screen = Tk()
screen.title('SIMPLE INTEREST CALCULATOR')
screen.configure(bg = 'pink')
screen.geometry('500x500')
l1 = Label(screen,text = "Enter principal amount:",fg = 'black',bg = 'orange',font = ('Arial',20))
l2 = Label(screen,text = "Enter rate of interest:",fg = 'black',bg = 'orange',font = ('Arial',20))
l3 = Label(screen,text = "Enter time period:",fg = 'black',bg = 'orange',font = ('Arial',20))
entry1 = Entry(screen)
entry2 = Entry(screen)
entry3 = Entry(screen)
l1.grid(row = 0,column = 0,padx = 10,pady = 10)
l2.grid(row = 1,column = 0,padx = 10,pady =10)
l3.grid(row = 2,column = 0,padx = 10,pady = 10)
entry1.grid(row = 0,column = 1,padx = 20,pady = 10)
entry2.grid(row = 1,column = 1,padx = 20,pady = 10)
entry3.grid(row = 2,column = 1,padx = 20,pady = 10)
l4 = Label(screen,text = 'answer will be displayed here',fg = 'blue',bg = 'white',font = ('Arial',20))
l4.grid(row = 4,column = 1,padx = 10)
def onclick():
    p = float(entry1.get())
    n = float(entry2.get())
    r = float(entry3.get())
    ans = (p*n*r)/100
    l4.configure(text = ans)
def m_onclick():
    p = float(entry1.get())
    n = float(entry2.get())
    r = float(entry3.get())
    ans = (p*n*r)/100
    ans1 = p+ans
    l4.configure(text = ans1)   
b1 = Button(screen,text = 'Simple interest',command = onclick,bg = 'orange',font = ('Arial',20))
b2 = Button(screen,text = 'Maturity amount',command = m_onclick,bg = 'orange',font = ('Arial',20))
b1.grid(row = 3,column = 0,padx = 10,pady = 10)
b2.grid(row = 3,column = 1,padx = 20,pady = 10)
screen.mainloop()'''

'''import os
print(os.getcwd())
def module_search(module):
    a = os.listdir()
    l1 = []
    for i in a:
        if i.endswith(".py"):
            l1.append(i)
    print(l1)
    module_found = False
    for j in l1:
        if module in j:
            print(module,'name found in file',j)
            module_found = True
        if module_found == False:
            print(module,'name not found')
module = input('enter the module name here:')
module_search(module)'''


