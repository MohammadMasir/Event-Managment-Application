'''alist = [7,4,5,9,8]
try:
    a = int(input('enter the first index:'))
    b = int(input('enter the second index:'))
    c = alist[a]/alist[b]

except IndexError as ie:
    print(ie)

except:
    print('unknown error')

else:
    print(c)

finally:
    print('hello world')'''


'''import re
a = ['a khan','s khan','r khanna','khandekar k','r kapoor']
for i in range(0,len(a)):
    x = re.search(r'khan',a[i])
    if x!= None:
        print(a[i],'matches')
    else:
        print(a[i],'not matches')'''


import re
a = 'lucky'
x = re.search(r'uc',a)
if x!=None:
    print('there')
else:
    print('not there')

 



