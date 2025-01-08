def check_empty(board):#termination condition
    for row in range (9):
        for col in range(9):
            if board[row][col]==0:
                return (row,col)
    return False

def is_valid(board,row,col,num):
    #checking along the row and column
    for i in range(9):
        if board[i][col]==num or board[row][i]==num:
            return False
    #checking the grid
    #//3 gets the position of 3x3 grid where the given cell is present
    #*3 converts the idex of 3x3 grid to its index in 9x9 board
    #+3 sice grid has 3 rows and 3 columns
    grid_start_row,grid_start_col=(row//3)*3,(col//3)*3
    for i in range(grid_start_row,grid_start_row+3):
        for j in range(grid_start_col,grid_start_col+3):
            if(board[i][j]==num):
                return False
    return True


def sudoku(board):
    res=check_empty(board)
    if not res:
        return True#suduko solved
    row,col=res
    for num in range(1,10):
        if is_valid(board,row,col,num):
            board[row][col]=num
            if sudoku(board):
                return True
            board[row][col]=0
    return False


board=[[0,0,0,0,0,9,3,0,2],
       [0,1,5,4,0,0,0,0,0],
       [2,0,0,0,7,0,0,9,0],
       [5,0,6,0,1,0,0,0,8],
       [0,0,8,9,0,3,1,0,0],
       [1,0,0,0,8,0,7,0,9],
       [0,5,0,0,9,0,0,0,4],
       [0,0,0,0,0,7,5,2,0],
       [7,0,4,5,0,0,0,0,0]]

if sudoku(board):
    for row in board:
        print(row)
else:
    print("cannot be solved")