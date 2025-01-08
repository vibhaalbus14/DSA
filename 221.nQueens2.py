#time comp:O(n*n!) #for each pos, we iterate over board to check validity
#space comp: O(n^2) #2d board storage
class Solution:
    
    def totalNQueens(self, n: int) -> int:
        def validate(row,col):
            nonlocal board,n
            #check same row
            for c in range(n):
                if board[row][c]=="Q":
                    return False
            #check same column
            for r in range(n):
                if board[r][col]=="Q":
                    return False
            #check upper left
            for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
                if board[i][j]=="Q":
                    return False
            #check upper right
            for i,j in zip(range(row,-1,-1),range(col,n)):
                if board[i][j]=="Q":
                    return False
            #check bottom left
            for i,j in zip(range(row,n),range(col,-1,-1)):
                if board[i][j]=="Q":
                    return False
            #check bottom right
            for i,j in zip(range(row,n),range(col,n)):
                if board[i][j]=="Q":
                    return False

            return True
        
        board=[["." for _ in range(n)]for _ in range(n)]
        count=0
        def placeQueens(row):
            nonlocal count,n
            if row==n:
                count+=1
                return #to find other possible solns
            
            for col in range(n):
               if validate(row,col):
                   board[row][col]="Q"
                   placeQueens(row+1)
                   #backtrack step
                   board[row][col]="."
        
        placeQueens(0)
        return count

#-------------------------------------approach 2----------------------------------------

#time comp:O(n!) #for each pos, we only check set
#space comp: O(n) #sets storage

#approach
#optimisation by using sets to track the used cols, diag and antidiagonals
#older approach uses 2D board and loops to check for another queen
#set approach ensures col, row+col and row-col are placed and hence tracked
#this row-col is followed by all queens placed across a diagonal
#row+col prop is followed by all queens placed across an antidiagonal
#so if two queens are have same sum/ difference => place alongside same antiDiag or diag => conflict
#this early loop termination and constant time addition and removal from set
class Solution:
    
    def totalNQueens(self, n: int) -> int:

        def validate(row,col):
            nonlocal cols,diagonals,antiDiagonals
            #this only checks if other queens are already present for the given pos across all 3 paths
            if col in cols or row+col in antiDiagonals or row-col in diagonals:
                return False
            return True

        
        cols=set()
        diagonals=set()
        antiDiagonals=set()
        board=[["." for _ in range(n)]for _ in range(n)]
        count=0

        def placeQueens(row):
            nonlocal count,n
            if row==n:
                count+=1
                return #to find other possible solns
            
            for col in range(n):
               if validate(row,col):
                cols.add(col)
                diagonals.add(row-col)
                antiDiagonals.add(row+col)

                placeQueens(row+1)

                #backtrack step
                cols.remove(col)
                diagonals.remove(row-col)
                antiDiagonals.remove(row+col)
        
        placeQueens(0)
        return count
        
        
        
        
        
        