import heapq
from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minHeap=[]
        for i in range(len(dist)):
            heapq.heappush(minHeap,(dist[i]/speed[i],i)) #dist/speed,dist,speed
            #if (2,2) and (2,1) i.e 2 monsters at 2 dist with 2 and 1 speed are present, the fast
            #moving monster must be killed first
        count=0
        while minHeap:# and minHeap[0][1]>0:
            time,i=heapq.heappop(minHeap)
            currDist=dist[i]
            currSpeed=speed[i]
            #update the distance
            updatedDist=currDist-(count*currSpeed)
            if updatedDist<=0:
                break
            count+=1
            #update all the distances
            # for i in range(len(minHeap)):
            #     minHeap[i][1]=minHeap[i][1]-(minHeap[i][2]) #dist-speed since time to recharge is 1
            # heapq.heapify(minHeap)
        return count



        