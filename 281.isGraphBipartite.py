from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #1.create adjList
        #2.assign curr node to one set and its neighbours to opposite
        #3.add the nodes not are not in visited to dq but check all nodes for its parent-child set presence
        #4.if currNode and its neighbour present in same set, false
        #5.ensure all nodes are visited
        #6.if all conds obey,return True
        n=len(graph)
        adjList={}
        setOne=set()
        setTwo=set()
        visited=set()

        for i,subList in enumerate(graph):
            adjList[i]=subList


        def bfs(node):
            nonlocal visited
            dq=deque()
            dq.append((i,1))
            visited.add(i)
            setOne.add(i)

            while dq:
                node,presentSet=dq.popleft()#node, set to which it is added
                if presentSet==1:
                    curr=setOne
                else:
                    curr=setTwo

                for neighbour in adjList[node]:
                    if neighbour in curr: #nodes in same set=> false
                        return False
                    elif neighbour not in visited:
                        visited.add(neighbour)
                        if presentSet==1:
                            setTwo.add(neighbour)
                            dq.append((neighbour,2))
                        else:
                            setOne.add(neighbour)
                            dq.append((neighbour,1))

        for i in range(n):
            if i not in visited:
                ans= bfs(i)
                if ans==False:
                    return ans
        return True
