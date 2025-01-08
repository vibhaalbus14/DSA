from typing import List
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #cycle detection => can be completed or not
        #ordering=> topological sorting
        #=> topological sorting for directed graph does both
        #keep track of indegree

        indegreeList=[0 for _ in range(numCourses)]#initially populate all nodes with 0 indegree
        adjList={}
        for i in range(numCourses):
            adjList[i]=[]
        
        for take,must in prerequisites:
            indegreeList[take]+=1
            adjList[must].append(take)
        
        res=[]
        visited=set()

        def topologicalSorting():    
            nonlocal res,visited
            dq=deque()
            for i in range(len(indegreeList)):
                if indegreeList[i]==0 and i not in visited:
                    dq.append(i)
                    visited.add(i)
            while dq:
                node=dq.popleft()
                res.append(node)
                #reduce the indegrees of its neighbour nodes
                for neighbour in adjList[node]:
                    indegreeList[neighbour]-=1
                    if indegreeList[neighbour]==0:
                        dq.append(neighbour)

        topologicalSorting()    
        if len(res)==numCourses:
            return res#if all can be completed=> no cycle
        else:
            return []



