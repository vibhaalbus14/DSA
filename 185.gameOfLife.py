from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #rules
        #<2=>die
        #2/3=>continue
        #==3 => revive
        #>3=>die

        #approach
        #1.first loop through the matrix and keep a track of the cells that are to be changed
        #2.revisit the cells and make changes
        rows=len(board)
        cols=len(board[0])
        toBeChanged=set()
        for i in range(rows):
            for j in range(cols):
                #8 neighbours
                presentState=board[i][j]
                top,bottom,left,right,top_right,top_left,bottom_right,bottom_left=0,0,0,0,0,0,0,0
                #top -1,0
                if i-1 in range(rows) and j in range(cols):
                    top=board[i-1][j]
                #bottom +1,0
                if i+1 in range(rows) and j in range(cols):
                    bottom=board[i+1][j]
                #left 0,-1
                if i in range(rows) and j-1 in range(cols):
                    left=board[i][j-1]
                #right 0,+1
                if i in range(rows) and j+1 in range(cols):
                    right=board[i][j+1]
                #top-left -1,-1
                if i-1 in range(rows) and j-1 in range(cols):
                    top_left=board[i-1][j-1]
                #top-right -1,+1
                if i-1 in range(rows) and j+1 in range(cols):
                    top_right=board[i-1][j+1]
                #bottom-left +1,-1
                if i+1 in range(rows) and j-1 in range(cols):
                    bottom_left=board[i+1][j-1]
                #bottom-right +1,+1
                if i+1 in range(rows) and j+1 in range(cols):
                    bottom_right=board[i+1][j+1]
                
                res=top+bottom+left+right+top_left+top_right+bottom_left+bottom_right
                if res<2:#die
                    if presentState!=0:
                        toBeChanged.add((i,j))
                elif res==3:#revive
                    if presentState==0:
                        toBeChanged.add((i,j))
                elif res==2 or res==3:
                    #continue with present state
                    pass
                elif res>3:#die
                    if presentState!=0:
                        toBeChanged.add((i,j))
            
        for i in range(rows):
            for j in range(cols):
                if (i,j) in toBeChanged:
                    board[i][j]=int(not board[i][j])
        