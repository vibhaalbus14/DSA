class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #approach
        #1.dfs where there is 0
        #2.neighbours are considered horz,vert and diagonally
        #3.since 8 options for each cell, choose the min and add one to prev to pass to the parent
        #note: backtracking is done and nodes from visited are popped
        if not grid or grid[0][0]!=0 or grid[-1][-1]!=0:
            return -1
        
        def dfsTrav(r,c):
            #however we do have a base case
                
            self.visited.add((r,c))
            if r==self.rows-1 and c==self.cols-1 :
                self.visited.remove((r,c))
                return 1
            # elif r>self.rows-1 or c>self.cols-1 :
            #     return 0
            else:
                valueList=[]
                #look for neighbours
                #left,right,top,bottom,top-left,top-right,bottom-left,bottom-right
                positions=[(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
                #check for conditions
                for nr,nc in positions:
                    if r+nr in range(self.rows) and c+nc in range(self.cols) and grid[r+nr][c+nc]==0 and (r+nr,c+nc) not in self.visited :
                        val=dfsTrav(r+nr,c+nc)
                        if val!=float('inf'):
                            valueList.append(val)
                            
                self.visited.remove((r,c))

                if len(valueList)==0:
                    res= float('inf')
                else:
                    res= min(valueList)+1

                return res

        self.rows=len(grid)
        self.cols=len(grid[0])
        self.grid=grid
        self.visited=set()
        #passing only the source to dfs
        shortestPath=dfsTrav(0,0)
        return shortestPath if shortestPath!=float('inf') else -1
    

#---------------------------bfs approach--------------------------------
#why bfs?
#bfs considers all its neighbours before the children
#the first one to reach the destination will be the  shortest
#other neighbours will also reach the destination
#but the destination will be marked visited and hence once the dest is reached , we return the result immediately
#in dfs, we explored all possible paths, even the longest paths, hence time limit exceeded

from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or grid[0][0]!=0 or grid[-1][-1]!=0:
            return -1
        
        rows=len(grid)
        cols=len(grid[0])
        visited=set()

        dq=deque()
        dq.append((0,0,1)) #length is 1 since the origin zero is used up
        visited.add((0,0))

        while dq:
            r,c,length=dq.popleft()
            if r==rows-1 and c==cols-1 :
                return length
            #look for neighbours
            #left,right,top,bottom,top-left,top-right,bottom-left,bottom-right
            positions=[(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
            #check for conditions
            for nr,nc in positions:
                if r+nr in range(rows) and c+nc in range(cols) and grid[r+nr][c+nc]==0 and (r+nr,c+nc) not in visited:
                    dq.append((r+nr,c+nc,length+1))
                    visited.add((r+nr,c+nc))
            
        return -1
        
