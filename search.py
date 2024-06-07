'''def search_string(text,substring):
    count = 0
    if len(text)>len(substring):
        for i in range(len(text)):
            for j in range(len(substring)):
                if text[i] == substring[j]:
                    count = count+i
                    print('sunstring found at index',count)
                    count = 0
    #print('len of substring more than required')
search_string('ABCD','BC')'''

'''def brute_force(text,pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n-m+1):
        j = 0
        while j<m and text[i+j] == pattern[j]:
             j = j+1
        if j == m:
            return i+1
        return False
print(brute_force('ABCD','D'))'''

def optimize_files(files):
    files.sort()
    count = 0
    while len(files)>1:
        a = files[0]+files[1]
        count = count+a
        files[0] = a
        files.pop(1)
    return count
files = [1,2,3,4,5]
print(optimize_files(files))

        