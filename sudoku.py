class Solution(object):
    # def isEmpty(self,board):
    #     for row in range(9):
    #         for col in range(9):
    #             if(board[row][col]=="."):
    #                 return (row,col)
    #     return None
    
    def isValid(self,row,col,board,num):
        #to check if number already exists in row or column
        for i in range(0,9):
            if((board[row][i]==num) or( board[i][col]==num)):
                return False
        #to check in subgrid
        startRow,startCol=(row//3)*3,(col//3)*3
        for i in range(startRow,startRow+3):
            for j in range(startCol,startCol+3):
                if(board[i][j]==num):
                    return False
        return True

    def solveSudoku(self, board,row ,col):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n=9
        if(row==n):
            return True
        elif(col==n):
            return self.solveSudoku(board,row+1,0)
        
        elif board[row][col]==".":
            for num in range(1,10):
                string_num=str(num)
                if(self.isValid(row,col,board,string_num)):
                    board[row][col]=string_num
                    if self.solveSudoku(board,row,col+1):
                        return True
                    board[row][col]="."
            return False
        else:
            return self.solveSudoku(board,row,col+1)
        

obj=Solution()
board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
obj.solveSudoku(board,0,0)
print("solved sudoku board is:-------------------")
for row in board:
    print(row)
   
        
        
        