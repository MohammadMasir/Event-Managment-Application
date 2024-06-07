'''arr = []
n = int(input('Enter the number of elements you want to add in array:'))
sum = 0
for i in range(n):
    num = int(input('Enter the number:'))
    arr.append(num)
    sum = sum+arr[i]
print('The sum of array is:',sum)'''

# Finding the maximum and minimum elememt in an array

'''arr = [2,4,1,9,5,10]
max = arr[0]
min = arr[0]
for i in range(1,len(arr)):
    if arr[i]<min:
        min = arr[i]
    if arr[i]>max:
        max = arr[i]
print('The smallest element is:',min)
print('The largest element is:',max)'''

#odd and even count in an array
'''arr = [2,4,1,9,5,10]
even_count = 0
odd_count = 0
for i in range(len(arr)):
    if arr[i]%2 == 0:
        even_count+= 1
    else:
        odd_count+= 1
print('The even count is:',even_count)
print('The odd count is:',odd_count)'''

#sum of rows in an array
'''arr1 = [[1,2],[3,4]]
m = 2
n = 2
sum = 0
for i in range(m):
    for j in range(n):
        sum = sum+arr1[i][j]
    print(f'The sum of row {i} is:',sum)
    sum = 0'''

#Addition of two matrix
'''arr1 = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = [[1,2,3],[4,5,6],[7,8,9]]
arr3 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        arr3[i][j] = arr3[i][j]+arr1[i][j]+arr2[i][j]
print(f'The new matrix is {arr3}')'''

#Multiplication of two matrices
'''arr1 = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = [[1,2,3],[4,5,6],[7,8,9]]
arr3 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(arr1)):
    for j in range(len(arr2[0])):
        for k in range(len(arr2)):
            arr3[i][j]+= arr1[i][k]*arr2[k][j]
print(arr3)'''

#Binary search
'''arr = [1,2,3,4,5,6,7,8,9,10]
key = 8
low = 0
high = len(arr)
while low<=high:
    mid = low+high//2
    if key == arr[mid]:
        print(mid+1)
        break
    elif key>arr[mid]:
        low = mid+1
    elif key<arr[mid]:
        high = mid-1'''

#Bubble sort technique
'''import time
def bubble(arr):
    start_time = time.perf_counter()
    print(start_time)
    n = len(arr)
    for j in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    print(arr)
    end_time = time.perf_counter()
    total_time = end_time-start_time
    print(total_time)
arr = [7,8,2,3,5]
bubble(arr)'''

#Selection sort technique
'''def select(s):
    n = len(s)
    for i in range(n-1):
        minvalue = i
        for j in range(i+1,n):
            if s[j]<s[minvalue]:
                minvalue = j
        if minvalue!=i:
            t = s[i]
            s[i] = s[minvalue]
            s[minvalue] = t
        print(s)
seq = [3,8,1,0]
select(seq)'''


#Brute force method
'''def brute_force(text,pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n):
        if text[i:i+m] == pattern:
            print(f'The pattern {pattern} found at index {i+1}')
brute_force('ABCD','BC')'''

#optimal merge program 

'''cost = 0
def optimal_merge(files):
    files.sort()
    global cost             #global variable defined outside function
    while len(files)>1:
        merged_files = files[0]+files[1]
        cost = cost+merged_files
        files[0] = merged_files
        files.pop(1)
    return cost
files = [1,2,3,4,5]
print(optimal_merge(files))'''

'''def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
n = int(input('Enter the number:'))
print(factorial(n))'''

'''def select(arr):
    n = len(arr)
    for i in range(n-1):
        minvalue = i
        for j in range(i+1,n):
            if arr[j]<arr[minvalue]:
                minvalue = j
        arr[minvalue],arr[i] = arr[i],arr[minvalue]
    print(arr)
arr = [1,5,3,7,2]
select(arr)'''

'''def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j = j-1
arr = [3,7,2,0,1]
insertion_sort(arr)
print(arr)'''

'''def hanoi(n,a,b,c):
    if n>=1:
        hanoi(n-1,a,c,b)
        print(f{'Move disk {n} from {a} to {c}'})
        hanoi(n-2,b,a,c)
hanoi(3,'A','B','C')'''

'''def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*recursive_factorial(n-1)
print(recursive_factorial(5))'''














