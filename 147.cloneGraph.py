"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        #approach
        #create a new node for every node in adjacencyList
        #use a set to check the node's existence
        #if exists, add to neighbours
        #if not , create and add to neighbours
        if not node:#empty graph
            return None
        adjList={}
        visited=set()
        #do bfs
        dq=deque()
        dq.append(node)
        visited.add(node)
        while dq:
            vertex=dq.popleft()
            if vertex.val not in adjList:
                adjList[vertex.val]=[]
            if vertex.neighbors==[]:
               continue
            else:
                for neighbour in vertex.neighbors:
                    if neighbour not in visited:
                        dq.append(neighbour)
                        visited.add(neighbour)
                    adjList[vertex.val].append(neighbour.val)#undirected
        #create new graph from adjacency list
        visited.clear()
        created={}#a dictionary of val:obj
        #dq=deque()#adding actual nodes to dq
        #adding actual nodes to visited
        newNode=Node(1)#as first node will always be there
        start=newNode
        dq.append(newNode)
        visited.add(newNode)
        created[newNode.val]=newNode
        
        while dq:
            newVertex=dq.popleft()
            for other in adjList[newVertex.val]:#creating the adjacent nodes to given vertex
                if other not in created:
                    neighbourVertex=Node(other)
                    created[other]=neighbourVertex
                else:
                    neighbourVertex=created[other]
                newVertex.neighbors.append(neighbourVertex)
            for newNeighbour in newVertex.neighbors:
                    if newNeighbour not in visited:
                        visited.add(newNeighbour)
                        dq.append(newNeighbour)
        return start
                

            