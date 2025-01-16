from typing import List
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #approach
        #1.loop through every cell
        #2.bfs 4 ways only if value of the cell is <= given cell
        #3.once the edge cells of both pacific and atlantic are met, add the curr cell to res

        #why bfs? reach pacific and atlantic at the earliest

        #border cells
        borderCellsPacific=set()
        borderCellsAtlantic=set()
        m=len(heights)
        n=len(heights[0])

        for col in range(n):
            borderCellsPacific.add((0,col))
            borderCellsAtlantic.add((m-1,col))
        for row in range(m):
            borderCellsPacific.add((row,0))
            borderCellsAtlantic.add((row,n-1))
        res=[]

        def bfs(r,c):
            pacific=False
            atlantic=False

            dq=deque()
            visited=set()
            start=[r,c]
            dq.append((r,c))
            visited.add((r,c))
            while dq:
                currR,currC=dq.popleft()
                if (currR,currC) in borderCellsPacific and not pacific:
                    pacific=True
                if (currR,currC) in borderCellsAtlantic and not atlantic:
                    atlantic=True
                if pacific and atlantic:
                    res.append(start)
                    break
                #check neighbours
                #top
                if currR-1 in range(m) and (currR-1,currC) not in visited and heights[currR-1][currC]<=heights[currR][currC]:
                    dq.append((currR-1,currC))
                    visited.add((currR-1,currC))
                
                #bottom
                if currR+1 in range(m) and (currR+1,currC) not in visited and heights[currR+1][currC]<=heights[currR][currC]:
                    dq.append((currR+1,currC))
                    visited.add((currR+1,currC))

                #left
                if currC-1 in range(n) and (currR,currC-1) not in visited and heights[currR][currC-1]<=heights[currR][currC]:
                    dq.append((currR,currC-1))
                    visited.add((currR,currC-1))

                #right
                if currC+1 in range(n) and (currR,currC+1) not in visited and heights[currR][currC+1]<=heights[currR][currC]:
                    dq.append((currR,currC+1))
                    visited.add((currR,currC+1))
        
        for row in range(m):
            for col in range(n):
                bfs(row,col)
        
        return res
    
#-------------------------approach2---------------------------------------------
from typing import List
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #approach
        #start from borders
        #see if border cell can reach other cells >= height
        #why? because all the cell must meet  the border cell to touch the ocean
        #=? optimised

        borderCellsPacific=set()
        borderCellsAtlantic=set()
        m=len(heights)
        n=len(heights[0])

        for col in range(n):
            borderCellsPacific.add((0,col))
            borderCellsAtlantic.add((m-1,col))
        for row in range(m):
            borderCellsPacific.add((row,0))
            borderCellsAtlantic.add((row,n-1))
    
        visitedPacific=set()
        visitedAtlantic=set()

        def bfs(r,c,nameSet):
            dq=deque()
            visited=set()
            dq.append((r,c))
            visited.add((r,c))
            while dq:
                currR,currC=dq.popleft()
                nameSet.add((currR,currC))
                #check neighbours
                #top
                if currR-1 in range(m) and (currR-1,currC) not in visited and heights[currR-1][currC]>=heights[currR][currC]:
                    dq.append((currR-1,currC))
                    visited.add((currR-1,currC))
                
                #bottom
                if currR+1 in range(m) and (currR+1,currC) not in visited and heights[currR+1][currC]>=heights[currR][currC]:
                    dq.append((currR+1,currC))
                    visited.add((currR+1,currC))

                #left
                if currC-1 in range(n) and (currR,currC-1) not in visited and heights[currR][currC-1]>=heights[currR][currC]:
                    dq.append((currR,currC-1))
                    visited.add((currR,currC-1))

                #right
                if currC+1 in range(n) and (currR,currC+1) not in visited and heights[currR][currC+1]>=heights[currR][currC]:
                    dq.append((currR,currC+1))
                    visited.add((currR,currC+1))
        
        for r,c in borderCellsPacific:
            bfs(r,c,visitedPacific)
        for r,c in borderCellsAtlantic:
            bfs(r,c,visitedAtlantic)
        
        intersection = visitedPacific & visitedAtlantic
        res=list(map(list,intersection))
        return res