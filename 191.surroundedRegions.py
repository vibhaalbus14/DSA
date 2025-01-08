from typing import List
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #approach
        #1.loop through the bondary cells , over O values
        #2.do a bfs serach and identify the cells to which this is connected and mark in visited
        #3.the cells that are marked in visited cannot be changed since they are connected to boundary cells 'O'
        #4.therefore, change the celles that are not in visited
        #5.this is a complimentary approach
        m=len(board)
        n=len(board[0])
        dq=deque()
        visited=set()

        def bfsSearch(i,j):
            nonlocal dq,visited
            dq.append((i,j))
            visited.add((i,j))
            while dq:
                r,c=dq.popleft()
                #check 4 adjacency
                #left 0,-1
                if r in range(m) and c-1 in range(n) and (r,c-1) not in visited and board[r][c-1]=="O":
                    dq.append((r,c-1))
                    visited.add((r,c-1))
                #right 0,+1
                if r in range(m) and c+1 in range(n) and (r,c+1) not in visited and board[r][c+1]=="O":
                    dq.append((r,c+1))
                    visited.add((r,c+1))
                #top -1,0
                if r-1 in range(m) and c in range(n) and (r-1,c) not in visited and board[r-1][c]=="O":
                    dq.append((r-1,c))
                    visited.add((r-1,c))
                #bottom +1,0
                if r+1 in range(m) and c in range(n) and (r+1,c) not in visited and board[r+1][c]=="O":
                    dq.append((r+1,c))
                    visited.add((r+1,c))

        #looping through boundaries to check connected O's that are not to be changed
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    if board[i][j]=="O" and (i,j) not in visited:
                        bfsSearch(i,j)
        #changing all O's that are not in visited
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and board[i][j]=="O":
                    board[i][j]="X"
        return board
obj=Solution()
print(obj.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))

                    

            
