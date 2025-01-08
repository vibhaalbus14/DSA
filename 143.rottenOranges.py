from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #approach
        #1.bfs where there is 2 and mark it visited initially
        #2.search for its adjacent neighbours vert and hori
        #3.loop through and do the same for unvisited 2's
        #4.finally loop to identify if any ones are there
        #5.if so return -1 else return time

        if not grid:
            return 0

        dq=deque()
        visited=set()
        rows=len(grid)
        cols=len(grid[0])
        self.time=0
        self.grid=grid
        freshOranges=0

        #add all rotten oranges as given to produce simultaneous effect
        for i in range(rows):
            for j in range(cols):
                if self.grid[i][j]==2 and (i,j) not in visited:
                    dq.append((i,j,self.time))
                    visited.add((i,j))
                elif grid[i][j]==1:
                    freshOranges+=1
        if freshOranges==0:
            return 0
        
        while dq:
            r,c,time=dq.popleft()
            #check for neighbours 
            #left
            if r in range(rows) and c-1 in range(cols) and self.grid[r][c-1]==1 and (r,c-1) not in visited:
                dq.append((r,c-1,time+1))
                visited.add((r,c-1))
                #make it rot
                self.grid[r][c-1]=2
            #right
            if r in range(rows) and c+1 in range(cols) and self.grid[r][c+1]==1 and (r,c+1) not in visited:
                dq.append((r,c+1,time+1))
                visited.add((r,c+1))
                #make it rot
                self.grid[r][c+1]=2
            #top
            if r-1 in range(rows) and c in range(cols) and self.grid[r-1][c]==1 and (r-1,c) not in visited:
                dq.append((r-1,c,time+1))
                visited.add((r-1,c))
                #make it rot
                self.grid[r-1][c]=2
            #left
            if r+1 in range(rows) and c in range(cols) and self.grid[r+1][c]==1 and (r+1,c) not in visited:
                dq.append((r+1,c,time+1))
                visited.add((r+1,c))
                #make it rot
                self.grid[r+1][c]=2
        

        #rechecking for any leftout ones's
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return -1
        self.time=time
        return self.time