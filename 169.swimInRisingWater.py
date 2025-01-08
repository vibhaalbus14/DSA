#time comp:O(n**2)+O(ElogV)
from typing import List
import math
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #approach
        #1.form a 4 adjacency list
        #2.use minHeap since minTime to reach is needed
        #3.calculate the max of  time
        #4.weights of each edge=time of adjacent square
        #5.since minimum time that acts as weight is being considered at every step,and
        #its guaranteed to make us reach destination=> greedy approach+shortest
        #dijkstra's algo to be used

        adjList=[]
        rows=cols=len(grid)
        for i in range(rows):
            adjList[i]=[]

        for i in range(rows):
            for j in range(cols):
                #left
                if i in range(rows) and j-1 in range(cols):
                    src=grid[i][j]
                    dest=grid[i][j-1]
                    weight=int(math.fabs(dest-src))
                    adjList[src].append(weight,dest)

                #right
                if i in range(rows) and j+1 in range(cols):
                    src=grid[i][j]
                    dest=grid[i][j+1]
                    weight=int(math.fabs(dest-src))
                    adjList[src].append(weight,dest)

                #top
                if i-1 in range(rows) and j in range(cols):
                    src=grid[i][j]
                    dest=grid[i-1][j]
                    weight=int(math.fabs(dest-src))
                    adjList[src].append(weight,dest)

                #bottom
                if i+1 in range(rows) and j in range(cols):
                    src=grid[i][j]
                    dest=grid[i+1][j]
                    weight=int(math.fabs(dest-src))
                    adjList[src].append(weight,dest)

        shortest={}
        minHeap=[(grid[0][0],grid[0][0])] #(time,square)
        tMax=grid[0][0]
        while minHeap:
            t1,n1=heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1]=t1 #min time to reach square n1
            #loop through its neighbours from adj list, go to that node which takes least time
            for t2,n2 in adjList[n1]:
                if n2 not in shortest:
                    t=t1+t2
                    heapq.heappush((t,n2)) #t time to reach n2 from the given start i.e grid[0][0]
                    tMax=max(t,tMax)

        return tMax