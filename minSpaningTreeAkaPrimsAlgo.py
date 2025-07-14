from typing import List
import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #classic min spanning tree
        #min cost=> min edges=> n-1
        #use minHeap


        n=len(points)
        adjList=defaultdict(list)
        visitedVertex=set()
        visitedEdges=set()
        cost=0

        #use another dict to name all the given points
        nameHashmap={}
        name=0
        for i in range(n):
            nameHashmap[(points[i][0],points[i][1])]=name #(x,y)=some number as name
            name+=1

        # print("names",nameHashmap)
        for i in range(n):
            srcName=nameHashmap[(points[i][0],points[i][1])]
            for j in range(i+1,n):
                destName=nameHashmap[(points[j][0],points[j][1])]
                dist=abs(points[i][0]-points[j][0])+ abs(points[i][1]-points[j][1])
                adjList[srcName].append((dist,destName))
                adjList[destName].append((dist,srcName))

        #start from any vertex, here, lets start from 0
        # print()
        # print("adjList",adjList)
        minHeap=[]
        visitedVertex.add(0)

        for dist,dest in adjList[0]:
            minHeap.append((dist,0,dest)) #dist,start,end
        
        heapq.heapify(minHeap)

        while len(visitedVertex)<n:
            dist,start,end=heapq.heappop(minHeap)

            if end in visitedVertex:
                continue

            #add the current edge to visitededges
            visitedEdges.add((start,end))
            cost+=dist
            # print()
            # print("correct edges",visitedEdges)
            # print("cost",cost)
            # print()
            #add the end to visitedvertex
            visitedVertex.add(end)

            #add the neighbours of end into minHeap
            for dist,neigh in adjList[end]:
                if neigh not in visitedVertex:
                    heapq.heappush(minHeap,(dist,end,neigh))
        
        return cost

        