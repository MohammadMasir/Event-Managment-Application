import sys
def nqueen(n):
    col = set()
    posdiag = set()
    negdiag = set()
    board = [["."]*n for i in range(n)]
    print("Empty board")
    
    for i in range(n):
        print(board[i])

    def backtrack(r):
        if r == n:
            print("Final board")
            for i in range(n):
                print(board[i])
            sys.exit()

        for c in range(n):
            if c in col or r+c in posdiag or r-c in negdiag:
                continue
        
            col.add(c)
            posdiag.add(r+c)
            negdiag.add(r-c)
            board[r][c] = 'Q'
            backtrack(r+1)

            col.remove(c)
            posdiag.remove(r+c)
            negdiag.remove(r-c)
            board[r][c] = "."
    backtrack(0)
nqueen(4)