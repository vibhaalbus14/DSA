#space complexity: O(n)=rec call stack , O(n^2)= to store state of board ,O(s*n^2) where s represents the no of solutions in res=> O(s* n^2)
#time complexity: O(n!)=first row=n choices(cols),2nd row (n-2) choices....hence n! as tree is pruned using validity
import copy
def outer(n):
    res=[]
    board=[["."]*n for i in range(n)]

    def isValid(row,col,board,n):
        for i in range(n):
            if((board[row][i]=='Q') or (board[i][col]=='Q')):#along row and column
               return False
        for i,j in zip(range(row,-1,-1),range(col,n)):#upper right 
            if board[i][j]=="Q":
                return False
        
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):#upper left
            if board[i][j]=="Q":
                return False
            
        for i,j in zip(range(row,n),range(col,-1,-1)):#lower left
            if board[i][j]=="Q":
                return False
        
        for i,j in zip(range(row,n),range(col,n)):
            if board[i][j]=="Q":
                return False

        # if( 0<=row-1<n and 0<=col-1<n):
        #     if(board[row-1][col-1]=='Q'):#upper left diagonal
        #         return False
    
        # if( 0<=row+1<n and 0<=col+1<n):
        #     if(board[row+1][col+1]=='Q'):#lower right diagonal
        #         return False
    
        # if( 0<=row-1<n and 0<=col+1<n):
        #     if(board[row-1][col+1]=='Q'):#upper right diagonal
        #         return False

        # if( 0<=row+1<n and 0<=col-1<n):
        #     if(board[row+1][col-1]=='Q'):#lower left diagonal
        #         return False
        
        return True
    

        
    def solveNQueens(row,board,n):
        nonlocal res
        max_index=n
        if(row==max_index):
            #res.append(board.copy())
            #res.append(["".join(row) for row in board])
            res.append(copy.deepcopy(board))
            return
            
        
        for col in range(n):
            if(board[row][col]=="."):
                if(isValid(row,col,board,n)):
                    board[row][col]='Q'
                    if solveNQueens(row+1,board,n):
                        pass    
                    board[row][col]='.'
        
        
    solveNQueens(0,board,n)
    return res

value=int(input("enter the no of queens:"))
if 4<=value<=9:
    ans=outer(value)
    count=0
    for queenBoard in ans:
        count+=1
        for row in queenBoard:
            str="".join(row)
            print(str)
    print(count)
    # n=4
# board = [["."] * n for _ in range(n)]# board=[["."*n] ]*n
# print(board)
# row,col=1,0
# for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#     print(i,j)

'''1.In n queens problem,while copying the board using board.copy(), a shallow copy is created that stores 
references to rows.Everytime the board values are changed,the values in shallow copy also change as both 
refer to same address .After solving the problem,the final state of the board is empty with "." and thus 
the result stored will also be empty with "."Hence deepcopy is preferred

2.board initialization: [["."]*n for i in range(n)]
this creates independent copies of rows rather than
[["."]*n]*n
'''
