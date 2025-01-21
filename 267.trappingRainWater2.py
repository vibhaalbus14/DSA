import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows=len(heightMap)
        cols=len(heightMap[0])

        #create a matrix to ensure same cell is not visted again
        visited=set()

        #push all the boundary cells to minheap cause they dont hold water
        #regardless of the height

        #now why minheap?
        #we know that in a range of cells, the neighbour that has the lowest height decides amount of water to hold
        #thus we use minheap to identify the contributing neighbour easily
        #here, a cells water holding cap depend on 4 adjacent neighbours
        minHeap=[]
        for i in range(rows):
            for j in range(cols):
                if i==rows-1 or j==cols-1 or i==0 or j==0:
                    
                    heapq.heappush(minHeap,(heightMap[i][j],i,j))#the height of cell,r,c
                    visited.add((i,j))
                    
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        water=0

        while minHeap:
            currHeight,r,c=heapq.heappop(minHeap)

            for tr,tc in directions:
                nr=r+tr
                nc=c+tc

                if nr>=0 and nr<rows and nc>=0 and nc<cols and (nr,nc) not in visited:
                    #it helps in holding water only if its height <= currheight             
                    if heightMap[nr][nc]<currHeight:
                        water+=(currHeight-heightMap[nr][nc])
                    
                    heapq.heappush(minHeap,(max(heightMap[nr][nc],currHeight),nr,nc))
                    visited.add((nr,nc))
                    #why max?because nearest max that decides is considered
                    #highlight on nearest
        return water