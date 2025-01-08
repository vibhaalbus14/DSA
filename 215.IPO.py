import heapq
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap=[] #-cap,profit
        minHeap=[] #cap,-profit

        for i in range(len(capital)):
            heapq.heappush(minHeap,(capital[i],profits[i]))
        

        while k!=0:

            while minHeap and minHeap[0][0]<=w:
                #pop all capital <=w 
                cap,profit=heapq.heappop(minHeap)
                #push only the profits and index to maxHeap
                heapq.heappush(maxHeap,-profit)
            
            if not maxHeap:#if maxHeap is empty=>no more projects left
                #nothing to add to w
                break
            
            #topmost project will have the max profit within capital limit
            #add it
            profit=heapq.heappop(maxHeap)
            w+=(-profit)
            k-=1

        return w