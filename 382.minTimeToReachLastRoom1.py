from typing import List
from collections import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        #cannot use bfs as weights to each cell is different
        #dijkstra's
        m=len(moveTime)
        n=len(moveTime[0])
        directions=[(-1,0),(1,0),(0,1),(0,-1)]

        visited=set()
        minHeap=[]
        minHeap.append((0,0,0)) #(t,r,c)
        visited.add((0,0))

        while minHeap:
            t,r,c=heapq.heappop(minHeap)
            if r==m-1 and c==n-1:
                return t
            #go over adjacent 4 neighbours

            for tr,tc in directions:
                nr=tr+r
                nc=tc+c

                if nr>=0 and nr<m and nc>=0 and nc<n and (nr,nc) not in visited:
                    if moveTime[nr][nc]>t:
                        nextTime=moveTime[nr][nc]
                    else:
                        nextTime=t
                    #can move only if that time i reached
                    visited.add((nr,nc))
                    heapq.heappush(minHeap,(1+nextTime,nr,nc))
        
        