from collections import deque
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        def bfs(count):
            while self.dq:
                r,c=self.dq.popleft()
                #identify its neighbours

                #left
                if r in range(self.rows) and c-1 in range(self.cols) and self.grid[r][c-1]==1 and (r,c-1) not in self.visited:
                    self.dq.append((r,c-1))
                    self.visited.add((r,c-1))
                    count+=1
                #right
                if r in range(self.rows) and c+1 in range(self.cols) and self.grid[r][c+1]==1 and (r,c+1) not in self.visited:
                    self.dq.append((r,c+1))
                    self.visited.add((r,c+1))
                    count+=1
                
                #top
                if r-1 in range(self.rows) and c in range(self.cols) and self.grid[r-1][c]==1 and (r-1,c) not in self.visited:
                    self.dq.append((r-1,c))
                    self.visited.add((r-1,c))
                    count+=1
                
                #bottom
                if r+1 in range(self.rows) and c in range(self.cols) and self.grid[r+1][c]==1 and (r+1,c) not in self.visited:
                    self.dq.append((r+1,c))
                    self.visited.add((r+1,c))
                    count+=1
            return count
            

        self.rows=len(grid)
        self.cols=len(grid[0])
        maxCount=0
        noIslands=0
        self.visited=set()
        self.grid=grid
        self.dq=deque()

        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j]==1 and (i,j) not in self.visited:
                    self.dq.append((i,j))
                    self.visited.add((i,j))#adding the start
                    count=bfs(1)#count is 1 as already "one" is added to dq
                    noIslands+=1
                    maxCount=max(maxCount,count)
        return maxCount