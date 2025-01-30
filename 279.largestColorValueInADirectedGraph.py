from collections import defaultdict, deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        #approach
        #bfs + topological sort

        n = len(colors)
        adjList = defaultdict(list)
        indegree = [0] * n
        
       
        for u, v in edges:
            adjList[u].append(v)
            indegree[v] += 1
        #maintain a 2d list, each node has 26 colours
        #how to convert colour to index?
        #ord('colour')-ord('a')= number to map
        colourArray=[[0]*26 for _ in range(n)]
        dq=deque()
        visited=set()
        maxVal=0
        for i, num in enumerate(indegree):
            if num==0:
                #mark the colour in colourmap 
                colourArray[i][ord(colors[i])-ord('a')]=1
                dq.append(i)
                visited.add(i)
        #start bfs
        while dq:
            node=dq.popleft()
            #consider the max colour val for the node
            maxVal=max(maxVal,max(colourArray[node]))

            if node in adjList:
                for neighbour in adjList[node]:
                    #must not just modify the colour of neighbour
                    #but also carr forward the values from parent
                    for colour in range(26):
                        childColour=colourArray[neighbour][colour]
                        parentColour=colourArray[node][colour]
                        if ord(colors[neighbour])-ord('a')==colour:
                            curr=1
                        else:
                            curr=0
                        colourArray[neighbour][colour]=max(childColour,parentColour+curr)
                        #propogate the colours to children
                    indegree[neighbour]-=1

                    if indegree[neighbour]==0:
                        visited.add(neighbour)
                        dq.append(neighbour)
                    
            
        if len(visited)==n:
            return maxVal
        else:
            return -1

        