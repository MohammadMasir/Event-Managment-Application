'''import pymysql as psql

try:
    mycon = psql.connect(host = "localhost",user = "root", password = "root",port = 3307,charset='utf8',db = 'student')
    cur = mycon.cursor()
    #uname = input('enter the username:')
    #upass = input('enter the password:')
    #qinsert = "insert into login values('"+uname+"','"+upass+"')"
    #select = select = "SELECT * FROM login WHERE uname='" +'lucky'+ "' AND upass='" +'luck@123'+ "'"
    select = "select * from customer_details where cust_id = 1"
    cur.execute(select)
    mycon.commit()
    result = cur.fetchall()
    for i in result:
        print(i)
   # print(result)
except Exception as e:
    print('something error',e)
finally:
    mycon.close()'''




'''a = ["data.py","data1.py","database.py","dataframe.py","employees.py"]
mod = input("enter the module name here:")
for i in a:
    if "numpy" in i:
        print("numpy files are",i)
    elif "pandas" in i:
        print("pandas files are",i)'''

'''rollno = int(input("enter the roll number:"))
name = input("enter your name:")
cl = input("enter your class:")
email = input("enter your email:")'''



'''import re
a = []
username = input("enter the username:")
dob = input("enter the date in foramt dd/mm/yyyy")
pan = input("enter your pan card number:")
adhar = int(input("enter the adhar card number:"))

if re.search(r"^[0-9]{1}[1-9]{1}/[0-9]{1}[1-2]{1}/[1000-2050]{4}$",dob):
    a.append(dob)
else:
    print("format not matches")
    
if re.search(r"^[A-Z]{5}[0-9]{4}[A-Z]$",pan):
    a.append(pan)
else:
    print("not matches")
    
if re.search(r"^[0-9]{12}$",adhar):
    a.append(adhar)
else:
    print("not matches")'''



'''import os
a = os.getcwd()
b = os.listdir()
mod = input('enter the module name:')
for i in b:
    if mod in i:
        print(mod,"files are:",i)
    else:
        print("no module files")'''




'''import os

current_directory = os.getcwd()
files = os.listdir(current_directory)

mod = input('Enter the module name: ')

found_module_files = False

for file in files:
    if mod in file:
        print(mod, "file found:", file)
        found_module_files = True

if not found_module_files:
    print("No module files found in the directory.")'''


'''import pymysql as psql
mycon = psql.connect(host = 'localhost',user = 'root',password = 'root',port = 3307,charset = 'utf8',db = 'student')
cur = mycon.cursor()
try:
    print('1.insert','2."Total')
    user = int(input('Enter your choice:'))
    if user == 1:
        i = 0
        while i<=5:
            rollno = int(input('enter your rollno:'))
            roll_str = str(rollno)
            name = input('Enter your name:')
            standard = input('Enter your class:')
            qstring = "insert into students values('"+roll_str+"','"+name+"','"+standard+"')"
            cur.execute(qstring)
            i=i+1
        mycon.commit()
        print('inserted successfully')
    elif user == 2:
        qstring1 = "select count(*) from students"
        cur.execute(qstring1)
        count = cur.fetchall()
        mycon.commit()
        print('The count of students is:',count)
except psql.Error as e:
    print('something issue',e)
finally:
    mycon.close()'''


'''import pymysql as psql
mycon = psql.connect(host = 'localhost',user = 'root',password = 'root',port = 3307,charset = 'utf8',db = 'student')
cur = mycon.cursor()
print('1.Register','2.Login')
try:
    user = int(input('Enter your choice:'))
    if user == 1:
        usr = input('Enter your username:')
        password = input('Enter your password:')
        re_pass = input('Re-enter your password:')
        qstring = f"insert into customers values('{usr}','{password}','{re_pass}')"
        cur.execute(qstring)
        mycon.commit()
        print('Username,Password and Confirm password added successful')
    elif user == 2:
        username = input('Enter the username:')
        pas = input('Enter the password:')
        qstring1 = f"select * from customers where usr ='{username}' AND password ='{pas}'"
        cur.execute(qstring1)
        x = cur.fetchall()
        if x!= None:
            print('Success')
        else:
            print('Error')
        mycon.commit()
except psql.Error as e:
    print('Something error occured',e)
finally:
    mycon.close()'''

'''import re
username = input('Enter 8 digit username(only characters):')
dob = input('Enter date of birth in the format dd/mm/yyyy:')
pan = input('Enter your pancard number:')
anum = input('Enter your aadhar card number:')
try:
    if re.match(r"^[A-Za-z]{8}$",username):
        f1 = open("lucky","a")
        f1.write(username+"\n")
    if re.match(r"^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$",dob):
        f1 = open('lucky','a')
        f1.write(dob+"\n")
    if re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$",pan):
        f1 = open('lucky','a')
        f1.write(pan+"\n")
    if re.match(r"^[0-9]{12}$",anum):
        f1 = open('lucky','a')
        f1.write(anum+"\n")
except Exception as e:
    print('The error is:',e)
finally:
    f1.close()'''


'''def binary_search(arr,k):
    low = 0
    high = len(arr)
    while low<=high:
        mid = low+(high-low)//2
        if k == arr[mid]:
            return mid+1
        elif k<arr[mid]:
            high = mid-1
        elif k>arr[mid]:
            low = mid+1
arr = [1,2,3,4,5]
print(binary_search(arr,4))'''

'''from tkinter import *
screen = Tk()
def read():
    print(x.get())
def write():
    str = input('Enter the new string:')
    x.set(str)
screen.title('Data binding')
screen.geometry('500x500')
screen.configure(bg = 'lightblue')
x = StringVar()
x.set('Hello')
entry1 = Entry(screen,textvariable = x)
entry1.grid(row = 0,column = 0,padx = 20)
b1 = Button(screen,text = 'Read',command = read)
b1.grid(row = 1,column = 0,padx = 10,pady = 10)
b2 = Button(screen,text = 'Write',command = write)
b2.grid(row = 1,column = 1,padx = 10,pady = 10)
screen.mainloop()'''

board = [["."]*4 for i in range(4)]
print(board)
for i in range(4):
    print(board[i])

    






