from typing import List
from collections import deque
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #approach
        #bfs
        m=len(grid)
        n=len(grid[0])
        dq=deque()
        minSum=float("inf")
        def bfs(r,c):
            nonlocal dq,minSum
            dq.append((r,c,grid[r][c]))
            while dq:
                r,c,pathSum=dq.popleft()
                if r==m-1 and c==n-1:
                    minSum=min(minSum,pathSum)
                #neighbours
                #right
                if r in range(m) and c+1 in range(n):
                    dq.append((r,c+1,pathSum+grid[r][c+1]))
                #bottom
                if r+1 in range(m) and c in range(n) and (r+1,c):
                    dq.append((r+1,c,pathSum+grid[r+1][c]))

            return minSum
                
                
        return bfs(0,0)
    
#----------------------------------------dp-dfs--------------------------------------------
from typing import List
from collections import deque
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #approach
        
        m=len(grid)
        n=len(grid[0])
        memo={}

        def helper(r,c):
            nonlocal memo
            if r==m-1 and c==n-1:
                return grid[r][c]

            if r>=m or c>=n:
                return float("inf")
            if (r,c)  in memo:
                return memo[(r,c)]

            left=helper(r,c+1)+grid[r][c]
            down=helper(r+1,c)+grid[r][c]

            memo[(r,c)]=min(left,down)
            return memo[(r,c)]
      
        return helper(0,0)