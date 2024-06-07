'''import tkinter as tk
from tkinter.messagebox import *
root = tk.Tk()
root.title('Simple Listbox')
root.geometry('500x500')
root.configure(bg = 'lightpink')
l1 = tk.Label(root,text = 'make your choices:',fg= 'black',bg = 'white')
l1.grid(row = 0,column = 0,pady = 10)
dish = ['Paneer tikka','Chicken Legpiece','Dal rice','Dkokala','Vada Pav']
list_var = tk.StringVar(value = dish)
menus = tk.Listbox(root,listvariable = list_var,selectmode = tk.SINGLE)
menus.grid(row = 1,column = 1,pady = 10)
def selected(event):
    index = menus.curselection()
    selected_dish = ",".join([menus.get(i) for i in index])
    showinfo(
        title = 'choosed menu',
        message = 'You selected the dish'+selected_dish
    )
menus.bind('<<ListboxSelected>>',selected)
root.mainloop()'''

'''import tkinter as tk
from tkinter.messagebox import *

root = tk.Tk()
root.title('Simple Listbox')
root.geometry('500x500')
root.configure(bg='lightpink')

l1 = tk.Label(root, text='Make your choices:', fg='black', bg='white')
l1.grid(row=0, column=0, pady=10)

dish = ['Paneer tikka', 'Chicken Legpiece', 'Dal rice', 'Dkokala', 'Vada Pav']
list_var = tk.StringVar(value=dish)
menus = tk.Listbox(root, listvariable=list_var, selectmode=tk.SINGLE)
menus.grid(row=1, column=1, pady=10)

def selected(event):
    indices = menus.curselection()
    if indices:
        selected_dishes = [menus.get(i) for i in indices]
        showinfo(
            title='Choosed menu',
            message='You selected the dish(s): ' + ', '.join(selected_dishes)
        )

menus.bind('<<ListboxSelect>>', selected)

root.mainloop()'''

'''import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

# create the root window
root = tk.Tk()
root.title('Tkinter Yes/No Dialog')
root.geometry('300x150')

# click event handler
def confirm():
    answer = askyesno(title='confirmation',
                    message='Are you sure that you want to quit?')
    

ttk.Button(
    root,
    text='Ask Yes/No',
    command=confirm).pack(expand=True)


# start the app
root.mainloop()'''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING

# create the root window
root = tk.Tk()
root.title('Tkinter Ok/Cancel Dialog')
root.geometry('300x150')

# click event handler


def confirm():
    answer = askokcancel(
        title='Confirmation',
        message='Deleting will delete all the data.',
        icon=WARNING)

    if answer:
        showinfo(
            title='Deletion Status',
            message='The data is deleted successfully')


ttk.Button(
    root,
    text='Delete All',
    command=confirm).pack(expand=True)


# start the app
root.mainloop()




