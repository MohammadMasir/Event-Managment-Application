import sys
def NQueen(n):
    col=set()
    print("Col set: ",col)
    posDiag=set()
    print("Positive Diag set: ",posDiag)
    negDiag=set()
    print("Negative Diag set: ",negDiag)
    board=[["."] * n for i in range(n)]
    print("Empty Board->")
    for i in range(n):
        print(board[i])

    def backtrack(r):
        print("r=",r)
        if r==n:
            print("Final Board->")
            for i in range(n):
                print(board[i])
            sys.exit()
        for c in range(n):
            print("c=",c)
            if c in col or r+c in posDiag or r-c in negDiag:
                continue

            col.add(c)
            print("Col set: ",col)
            posDiag.add(r+c)
            print("Positive Diag set: ",posDiag)
            negDiag.add(r-c)
            print("Negative Diag set: ",negDiag)
            board[r][c]="Q"
            print("Placing Q at r=",r,"c=",c)
            backtrack(r+1)
            print("Cannot place Queen in current row")
            print("Returning to the recursion where r is still",r," and c is stuck at ",c)
            col.remove(c)
            print("Col set: ",col)
            posDiag.remove(r+c)
            print("Positive Diag set: ",posDiag)
            negDiag.remove(r-c)
            print("Negative Diag set: ",negDiag)
            print("Removing Q from r=",r,"c=",c)
            board[r][c]="."
    backtrack(0)
        
NQueen(4)