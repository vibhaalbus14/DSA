from collections import defaultdict, deque
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        #1.loop through all ones , bfs ,identify all islands,
        #2.map each cell to island it belongs to in cellMap
        #3.use islandGroups to count no of islands and length of each island
        #4.go through all zeroes, visit only the neighbouring cells ,
        #if one , add that the length of the island to which it belongs and mark it visited this allows us from adding same islands length again and again.

        rows=cols=len(grid)
        flag=True #no zeroes => true
        maxLength=float("-inf")
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        globalVisited=set()
        cellMap=defaultdict(int)
        islandGroups=[]
        zeroes=set()
        
        #go through all the land cells
        #increment the length of island to which they belong
        #in cellmap, map them to the island group they belong
        def bfs(r,c):
            visited=set()
            dq=deque()
            dq.append((r,c))
            visited.add((r,c))
            group=len(islandGroups)-1
            cellMap[(r,c)]=group

            while dq:
                r,c=dq.popleft()
                islandGroups[-1]+=1

                for tr,tc in directions:
                    nr=tr+r
                    nc=tc+c

                    if nr>=0 and nr<rows and nc>=0 and nc<cols and (nr,nc) not in visited and grid[nr][nc]==1:
                        globalVisited.add((nr,nc))
                        visited.add((nr,nc))
                        cellMap[(nr,nc)]=group
                        dq.append((nr,nc))
                        
        def findLength(r,c):
            currLength=1
            groupsAdded=set()
            for tr,tc in directions:
                nr=tr+r
                nc=tc+c

                if nr>=0 and nr<rows and nc>=0 and nc<cols and  grid[nr][nc]==1:
                    group=cellMap[(nr,nc)]
                    if not groupsAdded or group not in groupsAdded:
                        groupsAdded.add(group)
                        currLength+=islandGroups[group]
                    
            return currLength

        
        
        #prepare cache for all ones
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in globalVisited:
                    islandGroups.append(0)
                    bfs(i,j)
                if grid[i][j]==0:
                    zeroes.add((i,j))
        
        for i,j in zeroes:
            if flag:
                flag=False
            #can at max make one change
            #change this zero to one
            #do bfs to all ones from here
            maxLength=max(maxLength,findLength(i,j))


        if flag:
            return rows*cols
        else:
            return maxLength