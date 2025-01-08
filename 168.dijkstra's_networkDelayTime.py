from typing import List
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #approach
        #since its one node producing signal and all nodes receiveing it
        #plus the time being minimum
        #dijkstra's alogrithm is to be used

        #form adjacency list
        adjList={}
        for i in range(1,n+1):
            adjList[i]=[]

        for start,end,weight in times:
            adjList[start].append([weight,end])

        minHeap=[]
        #insert the src of graph
        heapq.heappush(minHeap,(0,k))#(wt,src)
        #create a storage hashMap
        shortest={}
        minTime=-1
        while minHeap:
            w1,n1=heapq.heappop(minHeap)
            if n1 not in shortest:
                shortest[n1]=w1
                minTime=max(minTime,w1)
            else:
                continue
            
            #traverse through n1's neighbours
            for w2,n2 in adjList[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap,(w1+w2,n2))
        #check if all nodes are reachable
        if len(shortest.values())==n: #all node's min time is identified
            return minTime
        else:
            return -1