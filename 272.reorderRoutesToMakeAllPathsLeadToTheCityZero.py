from collections import defaultdict
from typing import List
from collections import deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #dfs 
        #make the edges bidirectional and then decide what to do
        #bfs also possible

        #approach
        #1.since all nodes must be able to reach zero, start from reverse
        #2.make all the edges bidirectional
        #3.start from 0th node and see its neighbours, if this (dest,start) edge is present in given 
        #connections, no change, else, increment change, add the preset node in visited
        #4.continue to do this
        
        
        adjList=defaultdict(list)
        given=set()

        for start,dest in connections:
            adjList[dest].append(start)
            adjList[start].append(dest)

            given.add((dest,start))

        visited=set()
        changes=0
        
        def helper(node):
            nonlocal changes,visited
            visited.add(node)
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    if (node, neighbour) not in given:
                        #make no changes
                        changes+=1
                    helper(neighbour)
                   

        helper(0)
        return changes


        
#------------------------------------bfs approach------------------------------------------
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #1.since all nodes have to reach 0,lets start from 0 and check if other nodes can reach zero and proceed outwards
        #2.we have a choice of using one side of edge, but it must help us reach the destination, create acjacency list with bidirectional edges
        #3. check if a node can reach b, if yes and if this edge is given in input, no chnage ele , increment chnage by one

        adjList=defaultdict(list)
        givenEdges=set()

        for source,dest in connections:
            adjList[source].append(dest)
            adjList[dest].append(source)

            givenEdges.add((dest,source))

        #we have to start from 0, and see the nodes taht zero can reach in adjList
        dq=deque()
        visited=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        dq.append(0) #(city)
        visited.add(0)
        totalChanges=0

        while dq:
           
            node=dq.popleft()
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    if (node,neighbour) not in givenEdges:
                        dq.append(neighbour)
                        totalChanges+=1
                    else:
                        dq.append(neighbour)
                    visited.add(neighbour)
        return totalChanges
                





        




        