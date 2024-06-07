'''def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))'''

'''def fibonacci(n):
    if (n<=1):
        raise ValueError('Atleast range should be of 2 numbers')
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))'''


'''#Numbers in ascending order
t = 0
def select(seq):
    for i in range(len(seq)-1):
        if seq[i]>seq[i+1]:
            t = seq[i]
            seq[i] = seq[i+1]
            seq[i+1] = t
    print(seq)

seq = [2,9,4,5]
select(seq)   #function call'''

'''#Numbers in descending order
t = 0
def select(seq):
    for i in range(len(seq)-1):
        if seq[i]<seq[i+1]:
            t = seq[i]
            seq[i] = seq[i+1]
            seq[i+1] = t
    print(seq)

seq = [2,9,4,5]
select(seq)   #function call'''

#Program to arrange numbers in ascending order
'''def select(seq):
    t = 0              #local variable used inside function
    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]:
            t = seq[i]
            seq[i]= seq[i+1]
            seq[i+1] = t
    print(seq)
seq = [3,56,9,8]
select(seq)            #Function call/Drivers code'''

'''def fact(n):
    fact = 1
    if n == 0 or n == 1:
        return 1
    else:
        while n>0:
            fact = fact*n 
            n = n-1
        return fact
print(fact(5))'''

'''def fiboiterate(n):
    pre = 0
    current = 1
    if n == 0:
        return pre
    elif n == 1:
        return current
    else:
        while n>1:
            prepre = pre
            pre = current
            current = prepre+pre
            n = n-1
        return current
print(fiboiterate(7))'''

'''def fiborecursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiborecursion(n-1)+fiborecursion(n-2)
print(fiborecursion(7))'''

'''def bubble_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr
arr = [0,8,1,-5,7,-1]
print(bubble_sort(arr))'''

'''def selection_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        for i in range(len(arr)-1):
            minval = i
            for j in range(i+1,len(arr)):
                if arr[minval]>arr[j]:
                    minval = j
            arr[minval],arr[i] = arr[i],arr[minval]
        return arr
arr = [0,7,89,-34,78,-0.09,0.007]
print(selection_sort(arr))'''

'''def insertion(arr):
    if len(arr) == 1:
        return arr
    else:
        for i in range(1,len(arr)):
            while arr[i-1]>arr[i] and i>0:
                arr[i-1],arr[i] = arr[i],arr[i-1]
                i = i-1
        return arr
arr = [0,5,-0.5,7,0.99]
print(insertion(arr))'''

'''def pattern_matching(text,pattern):
    m = len(text)
    n = len(pattern)
    for i in range(m):
        if text[i:i+n] == pattern:
            print(f'Pattern {pattern} found at {i}')
        else:
            print(f'Pattern not found')
pattern_matching('ABCD','AB')'''

'''def linear_search(arr,key):
    flag = 0
    for i in range(len(arr)):
        if key == arr[i]:
            print(f'Element {key} found at index {i+1}')
            flag = 1
            break
        if flag!=0:
            print(f'Element not found')
arr = [0,1,2,3,4,5]
linear_search(arr,5)'''

'''def binary_search(arr,key):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = low+(high-low)//2
        if key == arr[mid]:
            return mid+1
        elif key>arr[mid]:
            low = mid+1
        elif key<arr[mid]:
            high = mid-1
arr = [0,1,2,3,4,5]
print(binary_search(arr,5))'''

'''def hanoi(n,a,b,c):
    if n == 1:
        print(f'Move disk {n}  from {a} to {c}')
    if n>1:
        hanoi(n-1,a,c,b)
        print(f'Move disk {n} from {a} to {c}')
        hanoi(n-1,b,a,c)
hanoi(15,'A','B','C')'''

'''def selection_sort(arr):
    if len(arr) == 1:
        return arr
    elif len(arr)>1:
        for i in range(len(arr)):
            minval = i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[minval]:
                    minval = j
            arr[minval],arr[i] = arr[i],arr[minval]
        return arr
arr = [-3,0,-0.08,76,1,0]
print(selection_sort(arr))'''

'''def insertion_sort(arr):
    if len(arr) == 1:
        return arr
    elif len(arr)>1:
        for i in range(len(arr)):
            j = i
            while arr[j-1]>arr[j] and j>0:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                j = j-1
        return arr
arr = [-3]
print(insertion_sort(arr))'''

'''def optimal_merge(files):
    cost = 0
    merged_files = 0
    files.sort()
    while len(files)>1:
        merged_files = files[0]+files[1]
        cost = cost+merged_files
        files[0] = merged_files
        files.pop(1)
    return cost
files = [3,7,2,1]
print(optimal_merge(files))'''

'''def divide(arr):
    if len(arr) == 1:
        return arr
    elif len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        nleft = divide(left)
        nright = divide(right)
        return merge_sort(nleft,nright)

def merge_sort(nleft,nright):
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

arr = [1,-1,0,9,3,6]
print(divide(arr))'''


'''a = 0
b = 1
def fibonacci(n):
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n>1:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))'''

def lcs(X,Y,m,n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1+lcs(X,Y,m-1,n-1)
    else:
        return max(lcs(X,Y,m,n-1),lcs(X,Y,m-1,n))
print(lcs('bcddaaaaafgha','ac',len('abc'),len('ac')))