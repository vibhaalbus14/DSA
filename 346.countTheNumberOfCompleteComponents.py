from typing import List
from collections import defaultdict 
import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        #every node in a comp must have n-1 edges
        #i.e find no of components
        #identify no of nodes in a comp
        #let no of nodes be n
        #then, every node must have n-1 edges
        #=> every comp must have n(n-1) edges
        #every node alone is a connected comp

        #=>bfs over evry component, find no of edges and nodees in that comp

        adjList=defaultdict(list)
        givenNodes=set()
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            givenNodes.add(u)
            givenNodes.add(v)

        #check if there are any individual nodes 
        comp=0
        visited=set()


        def bfs(node):
            compNodes=set()
            visited.add(node)
            dq=deque()
            dq.append(node)
            compNodes.add(node)
            edges=0
        
            while dq:
                currNode=dq.popleft()
                if currNode in adjList:
                    for neighbour in adjList[currNode]:
                        edges+=1
                        compNodes.add(neighbour)
                        if neighbour not in visited:
                            visited.add(neighbour)
                            dq.append(neighbour)
            
            n=len(compNodes)
            return edges==n*(n-1)

        #bfs over every node and mark them visited
        for i in range(n):
            if i not in visited:
                if bfs(i):
                    comp+=1
        
        return comp



        