import copy

class Solution(object):

    def __init__(self,n):
        self.res=[]
        self.board=[["."]*n for _ in range(n)]

    def isValid(self,row,col,n):
        for i in range(n):
            if((self.board[row][i]=='Q') or (self.board[i][col]=='Q')):#along row and column
               return False
        for i,j in zip(range(row,-1,-1),range(col,n)):#upper right 
            if self.board[i][j]=="Q":
                return False
        
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):#upper left
            if self.board[i][j]=="Q":
                return False
            
        for i,j in zip(range(row,n),range(col,-1,-1)):#lower left
            if self.board[i][j]=="Q":
                return False
        
        for i,j in zip(range(row,n),range(col,n)):#lower right diagonal
            if self.board[i][j]=="Q":
                return False
        
        return True
    

    def solveNQueens(self,row,n):
        if(row==n):
            self.res.append(copy.deepcopy(self.board))
            return
        for col in range(n):
            if(self.isValid(row,col,n)):
                self.board[row][col]='Q'
                self.solveNQueens(row+1,n)    
                self.board[row][col]='.'

    def solve(self):
        self.solveNQueens(0,len(self.board))
        return self.res
    

obj=Solution(8)
count=0
ans=obj.solve()
for queenBoard in ans:
    count+=1
    for row in queenBoard:
        str="".join(row)
        print(str)
    print()
print(count)