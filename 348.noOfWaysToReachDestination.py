from typing import List
import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #identify shortest amount of time using dijkstra's
        #identify no of ways it can be reached
        adjList=defaultdict(list)
        for u,v,w in roads:
            adjList[u].append([v,w])
            adjList[v].append([u,w])

        visited=set()
        minHeap=[(0,0)]
        visited.add(0)
        minTime=float("inf")

        while minHeap:
            currWt,currNode=heapq.heappop(minHeap)
            if currNode==n-1:
                minTime=currWt
            for neighbour,time in adjList[currNode]:
                if neighbour not in visited:
                    heapq.heappush(minHeap,(time+currWt,neighbour))
                    visited.add(neighbour)
        
        # @cache
        # def dfs(prev,curr,time):
        #     if curr==n-1 and time==minTime:
        #         return 1
        #     if time>minTime:
        #         return 0
            
        #     total=0
        #     for neighbour,wt in adjList[curr]:
        #         if neighbour!=prev:
        #             total+=dfs(curr,neighbour,time+wt)


        #     return (total%(10**9 + 7))
        def backtrack(curr,time):
            if curr==n-1 and time==minTime:
                return 1
            if time>minTime:
                return 0
            
            total=0
            for neighbour,wt in adjList[curr]:
                if neighbour not in nodeVisited:
                    nodeVisited.add(neighbour)
                    total+=backtrack(neighbour,time+wt)
                    nodeVisited.remove(neighbour)


            return (total%(10**9 + 7))
              
        nodeVisited=set()
        nodeVisited.add(0)
        return backtrack(0,0)
            
#--------------------------------------optimal approach-------------------------------------------------------------------
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #identify shortest amount of time using dijkstra's
        #identify no of ways it can be reached

        #slight modification
        #1.keep an array called i=min_cost => keeps track of min cost to reach each node
        #2.keep track of no of waysto reach a node with min cost using another array called ways_to_reach
        #3. only if the cost to reach a node from parent is min comapred to min cost of that node, reiniialize the cost of node and ways to reach that node will be ways to reach parent node
        #4.if the cost to reach node from parent is same as min_cost, then increment the no of ways to reasch that node by parent's count
        #5.add into heap only if min_cost is changed
        #6.else, dont add to heap, this will make it directed graph

        adjList=defaultdict(list)
        for u,v,w in roads:
            adjList[u].append([v,w])
            adjList[v].append([u,w])

        
        minHeap=[(0,0)]#cost,node
        minCost=[float("inf")]*n
        waysToReach=[0]*n
        #only one way to reach 0th node, i.e only if we begin with it
        waysToReach[0]=1
        #cost to reach 0 since we start with it is also 0
        minCost[0]=0
        MOD=10**9 +7

        while minHeap:
            currWt,currNode=heapq.heappop(minHeap)
            for neighbour,time in adjList[currNode]:
                if time+currWt < minCost[neighbour]:
                    #reinitialise the ways_to_reach neighbour node since new min is found
                    #add to minheap 
                    minCost[neighbour]=time+currWt
                    heapq.heappush(minHeap,(minCost[neighbour],neighbour))
                    waysToReach[neighbour]=waysToReach[currNode]

                elif time + currWt==minCost[neighbour]:
                    #this will only inc the no of ways to reach the nei with min cost
                    #=> add the no of ways
                    waysToReach[neighbour]+=waysToReach[currNode]

        return waysToReach[n-1]%MOD







        





        