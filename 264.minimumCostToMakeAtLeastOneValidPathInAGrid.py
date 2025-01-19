import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        #dp approach
        #change the given cell to all possible signs
        m=len(grid)
        n=len(grid)
        hashMap={}
        hashMap[1]=(0,1)
        hashMap[2]=(0,-1)
        hashMap[3]=(1,0)
        hashMap[4]=(-1,0)

        
        def dfs(row,col,visited):
            currCost=float("inf")
            if row==m-1 and col==n-1:
                return 0
            if row not in range(m) or col not in range(n):
                return float("inf")
            
            visited.add((row,col))

            for i in range(1,5):#possible movements
                if (row+hashMap[i][0],col+hashMap[i][1]) not in visited:
                    if grid[row][col]==i :
                        currCost=min(currCost,dfs(row+hashMap[i][0],col+hashMap[i][1],visited))
                    else:
                        currCost=min(currCost,dfs(hashMap[i][0],hashMap[i][1],visited)+1) #cost of changing
            visited.remove((row,col))
            return currCost
        
        return dfs(0,0,set())

#--------------------------------------------approach 2---------------------------------
# import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        #dijkstra's algorithm
        m=len(grid)
        n=len(grid[0])

        hashMap={}
        hashMap[1]=(0,1)#right
        hashMap[2]=(0,-1)#left
        hashMap[3]=(1,0)#bottom
        hashMap[4]=(-1,0)#top

        minHeap=[]
        visited=set()

        heapq.heappush(minHeap,(0,0,0))#(cost,row,col)

        while minHeap:
            cost,row,col=heapq.heappop(minHeap)

            if row==m-1 and col==n-1:
                return cost
            
            if (row,col) in visited:#by doing this same instance adding its neighbours with higher cost is avoided
                continue
            
            visited.add((row,col))#low cost instance is popped

            #choose all possible directions
            for i in range(1,5):
                nr=row+hashMap[i][0]
                nc=col+hashMap[i][1]

                if nr>=0 and nr<m and nc>=0 and nc<n:
                    if i==grid[row][col]:
                        heapq.heappush(minHeap,(cost,nr,nc))#no cost as we are using whats given in cell
                    else:
                        heapq.heappush(minHeap,(cost+1,nr,nc))
            '''
            The priority queue ensures that the cell with the lowest cost is processed first.
            When a cell is popped, it represents the shortest path to that cell found so far.
            If a better (lower-cost) path to a cell is found after it was already pushed with 
            a higher cost, the better cost is added to the heap.Once the cell is processed, 
            any entries for the same cell with a higher cost become redundant.'''

                

