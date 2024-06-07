#Factorial using iterative  approach
'''def factiterate(n):
    fact = 1
    if n == 0 or n == 1:                As input size n grows the running time increases gradually
        return 1                        hence the time complexity is O(n)
    else:
        while n>1:
            fact = fact*n
            n = n-1
        return fact
print(factiterate(51))'''

#using recursive approach
'''def factrecursion(n):                Time complexity = O(n)
    if n == 0 or n == 1:
        return 1
    else:
        return n*factrecursion(n-1)
print(factrecursion(5))'''

#Fibonacci series using iterative  approach
'''def fiboiteration(n):
    prev = 0
    current = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n>2:
        for i in range(2,n+1):
            prevpre = prev
            prev = current
            current = prev+prevpre
        return current
print(fiboiteration(7))'''

#using recursive approach
'''def fibrecursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibrecursion(n-1)+fibrecursion(n-2)
print(fibrecursion(7))'''

#Bubble sort algorithm
'''def bubble(arr):
    m = len(arr)
    for i in range(m-1):
        for j in range(m-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
arr = [7,3,0,5,1]
print(bubble(arr))'''

#selection sort algorithm
'''def selection(arr):
    m = len(arr)
    for i in range(m):
        minval = i
        for j in range(i+1,m):
            if arr[j]<arr[minval]:
                minval = j
            arr[minval],arr[i] = arr[i],arr[minval]
    return arr
arr = [7,0,2,9,3,0]
print(selection(arr))'''

#Insertion sort algorithm
'''def insertion(arr):
    m = len(arr)
    for i in range(1,m):
        while arr[i]<arr[i-1] and i>0:
            arr[i],arr[i-1] = arr[i-1],arr[i]
            i = i-1
    return arr
arr = [7,0,2,9,3,0]
print(insertion(arr))'''

#Pattern matching
'''def brute_force(text,pattern):
    m = len(text)
    n = len(pattern)
    for i in range(m):
        flag = 0
        if text[i:i+n] == pattern:
            print(f'The pattern {pattern} found at index {i+1}')
            flag = 1
            break
        if flag == 0:
            print('Element not found')
brute_force('ABCD','E')'''

# Testing the function with n discs  Tower of hanoi
'''def tower_of_hanoi(n, a, b,c):
    if n == 1:
        print(f'Move disc {n} from {a} to {c}')
    elif n>1:
        tower_of_hanoi(n-1,a,c,b)
        print(f'Move {n} disk from {a} to {c}')
        tower_of_hanoi(n-1,b,a,c)
tower_of_hanoi(2,'A','B','C')'''

#File merging
'''
def optimal_merge(files):
    cost = 0
    files.sort()
    while len(files)>1:   
        merged_files = files[0]+files[1]
        cost = cost+merged_files
        files[0] = merged_files
        files.pop(1)
    return cost
files = [1,2,3,4,5]
print(optimal_merge(files))'''

'''def lcs(X, Y, m, n):
 
    if m == 0 or n == 0:
       return 0
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1)
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
 
 
# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X, Y, len(X), len(Y)))'''

#Merge sort
'''def sort(nleft,nright):
    i = j = 0
    result = []
    while i<len(nleft) and j<len(nright):
        if nleft[i]<nright[j]:
            result.append(nleft[i])
            i = i+1
        else:
            result.append(nright[j])
            j = j+1
    result = result+nleft[i:]
    result = result+nright[j:]
    return result

def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        nleft = mergesort(left)
        nright = mergesort(right)
        return sort(nleft,nright)
    else:
        return arr
   
arr = [7,2,3,1,-1,0,46,78]
print(mergesort(arr))'''

'''def colrow(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            sum = sum + arr[j][i]
        print(f'Sum of {i} column is {sum}')
        sum = 0
arr = [[1,2,3],[4,5,6],[7,8,9]]
colrow(arr)'''

'''def diagonal(arr):
    sum = 0
    sum1 = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                sum = sum + arr[i][j]
            if i+j == len(arr)-1:
                sum1 = sum1 + arr[i][j]
    print(f'Sum of diagonal element is {sum}')
    print(f'sum of antidiagonal element is {sum1}')
arr = [[1,2,3],[4,5,6],[7,8,9]]
diagonal(arr)'''


'''def addition_of_matrix(arr1,arr2,arr3):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            arr3[i][j] = arr3[i][j]+arr1[i][j]+arr2[i][j]
    return arr3
arr1 = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = [[1,2,3],[4,5,6],[7,8,9]]
arr3 = [[0,0,0],[0,0,0],[0,0,0]]
print(addition_of_matrix(arr1,arr2,arr3))'''

'''def matrix_multiplication(arr1,arr2,res):
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                res[i][j]+=arr1[i][k]*arr2[k][j]
    return res
arr1 = [[1,2,3],[4,5,6],[7,8,9]]
arr2=[[2,3,4],[6,7,8],[1,2,3]]
res=[[0,0,0],[0,0,0],[0,0,0]]
print( matrix_multiplication(arr1,arr2,res))'''

'''def minmax(arr):
    min = arr[0]
    max = arr[0]
    for i in range(1,len(arr)):
        if arr[i]<min:
            min = arr[i]
        elif arr[i]>max:
            max = arr[i]
    print(min,max)
arr = [1,2,3,4,5,6,7,8,9]
minmax(arr)'''

'''def oddeven(arr):
    even = 0
    odd = 0
    for i in range(len(arr)):
        if i%2 == 0:
            even = even+1 
        else:
            odd = odd+1
    return even,odd
arr = [1,2,3,4,5,6,7]
print(oddeven(arr))'''

'''def linear_search(arr,key):
    m = len(arr)
    flag = 0
    for i in range(m):
        if arr[i] == key:
            print(f'Element found at position {i+1}')
            flag = 1
            break
    if flag == 0:
        print('Element not found')
arr = [1,5,7,9,7]
linear_search(arr,7)'''

'''def binary_search(arr,key):
    low = 0
    high = len(arr)
    while low<=high:
        mid = low+(high - low)//2
        if arr[mid] == key:
            return mid
        elif arr[mid]>key:
            low = mid+1
        elif arr[mid]<key:
            high = mid-1
arr = [1,2,3,4,5,6,7]
print(binary_search(arr,4))'''

'''def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
arr = [0,5,-1,3]
print(bubblesort(arr))'''

'''def selectionsort(arr):
    for i in range(len(arr)):
        minval = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minval]:
                minval = j
        arr[i],arr[minval] = arr[minval],arr[i]
    return arr
arr = [0,5,-4,-0.008,0.3]
print(selectionsort(arr))'''

'''def insertionsort(arr):
    for i in range(1,len(arr)):
        while arr[i-1]>arr[i] and i>0:
            arr[i-1],arr[i] = arr[i],arr[i-1]
            i = i-1
    return arr
arr = [0,5,-4,-0.008,0.3]
print(insertionsort(arr))'''

#Brute force
'''def brute_force(text,pattern):
    m = len(text)
    n = len(pattern)
    flag = 0
    for i in range(m):
        if text[i:i+n] == pattern:
            print(f'Pattern {pattern} found at {i+1}')
            flag = 1
    if flag == 0:
        print(f'Pattern {pattern} not found')
brute_force('ABCD','BC')'''
        
'''def hanoi(n,a,b,c):
    if n == 1:
        print(f'Move the disk {n} from {a} to {c}')
    else:
        hanoi(n-1,a,c,b)
        print(f'Move the disk {n} from {a} to {c}')
        hanoi(n-1,b,a,c)
hanoi(3,'A','B','C')'''

'''def factorial_using_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial_using_recursion(n-1)
print(factorial_using_recursion(2))'''

'''def factorial_using_iteration(n):
    fact = 1
    if n == 0 or n == 1:
        return 1
    else:
        while n>=1:
            fact = fact*n
            n = n-1
        return fact
print(factorial_using_iteration(5))
'''

'''def fibo_using_recursion(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibo_using_recursion(n-1)+fibo_using_recursion(n-2)
print(fibo_using_recursion(7))'''

'''def fibonacci(n):
    prev = 0
    curr = 1
    if n == 0:
        return prev
    elif n == 1:
        return curr
    else:
        while n>1:
            prevprev = prev
            prev = curr
            curr = prev + prevprev
            n = n-1
        print(curr)
fibonacci(7)'''

'''def optimal_merge(files):
    cost = 0
    merged_files = 0
    files.sort()
    n = len(files)
    while n>1:
        merged_files = files[0]+files[1]           #GREEDY ALGORITHM
        cost = cost+merged_files
        files[0] = merged_files
        files.pop(1)
        n = n-1
    return cost
files = [5,4,1,2,3]
print(optimal_merge(files))'''

'''def coin_change(arr,input):
    arr.sort(reverse = True)
    res = []
    for i in range(len(arr)):
        while input>=arr[i]:
            input = input - arr[i]
            res.append(arr[i])
    return res
arr = [1,10,50,100]
print(coin_change(arr,60))'''

#Merge sort algorithm

'''def divide_arr(arr):
    if len(arr) == 1:
        return arr
    else:
        while len(arr)>1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            nleft = divide_arr(left)
            nright = divide_arr(right)
            return merge_sort(nleft,nright)

def merge_sort(nleft,nright):
    i = j = 0
    res = []
    while i<len(nleft) and j<len(nright):
        if nleft[i]<nright[j]:
            res.append(nleft[i])
            i = i+1
        else:
            res.append(nright[j])
            j = j+1
    res = res+nleft[i:]
    res = res+nright[j:]
    return res

arr = [0,6,-1,2,-0.9]
print(divide_arr(arr))
'''

#Backtrack algorithm

'''import sys
def nqueen(n):
    col = set()
    posdiag = set()
    negdiag = set()
    board = [["."]*n for i in range(n)]
    print('Empty board')
    for i in range(n):
        print(board[i])

    def backtrack(r):
        if r == n:
            print('Final board')
            for i in range(n):
                print(board[i])
            sys.exit()        
        for c in range(n):
            if c in col or r+c in posdiag or r-c in negdiag:
                continue

            col.add(c)
            posdiag.add(r+c)
            negdiag.add(r-c)
            board[r][c] = "Q"
            backtrack(r+1)

            col.remove(c)
            posdiag.remove(r+c)
            negdiag.remove(r-c)
            board[r][c] = "."
    backtrack(0)
nqueen(4)'''

'''import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Themed Frame Example")

# Create a themed frame
frame = ttk.Frame(root, padding=(10, 10, 10, 10))
frame.pack()

# Add widgets to the frame
label = ttk.Label(frame, text="This is a themed frame.")
label.pack()

button = ttk.Button(frame, text="Click Me")
button.pack()

root.mainloop()'''





        





            

 

        
            
        