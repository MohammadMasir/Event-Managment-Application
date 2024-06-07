import pandas as pd
import matplotlib.pyplot as plt

'''a = open('hello','r')
#print('check if the file is closed:',a.closed)
print(a.read())
print('Name of the file is:',a.name)
print('Name of mode is:',a.mode)'''


#df = pd.read_csv('house.csv')
#print(df)

'''plt.plot(df['bedrooms'],df['price'])
plt.title('number of bedrooms Vs price')
plt.xlabel('number of bedrooms')
plt.ylabel('price')'''

'''plt.plot(df.sqft_living,df.bedrooms,kind='hist',color='blue')
plt.title('sqft_living Vs number of bedrooms')
plt.xlabel('sqft_living')
plt.ylabel('number of bedrooms')
plt.show()'''

#print(df[df['floors'] == 1.5])

#print(df[df['bedrooms']>2])

#print(df[df['price']>200000])

data={'empno':[1,2,3,4,5,6,7,8,9,10],'name':['lucky','khushi','manu','nidha','poonam','varsha','dilip','hansraj','gautam','vikas'],
     'designation':['hr','doctor','executive post','engineer','locopilot','chief offficer','student','IAS','storeman','pilot'],
     'salary':[25000,45000,100000,50000,34000,67000,78000,56000,12000,43000]}

df = pd.DataFrame(data)
#print(df)
#print(df[df['designation'] == 'executive post'])
'''x = df[df['salary']>50000]
print(x['name'])'''

#print(df[df['designation'] == 'executive post'])

#print(df.name,df.salary)

#print(df)


'''import re
print('U want to enter a name which start with M and end with Y')
str = input('Enter the string here:')
x = re.search(r"^M.Y$",str)

if x!=None:
    print('Your provided name is valid!!')
else:
    print('Your provided name is not valid.')'''

grouped = df.groupby(['name','salary'])
print(grouped)








