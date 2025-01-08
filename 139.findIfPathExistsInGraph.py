from collections import defaultdic
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        #approach
        #1.create adjList
        #2.do dfs or bfs of source 
        #3.after that, check if destination is in visited
        #4.if yes, path exists
        #5.else return false
        adjList=defaultdic(list)
        for start,end in edges:
            adjList[start].append(end)
            adjList[end].append(start)#bi directional
        visited=[]
        def dfsTrav(node):#rec
            visited.append(node)
            if node in adjList:
                for neighbour in adjList[node]:
                    dfsTrav(neighbour)
        dfsTrav(source)
        if destination in visited:
            return True
        else:
            return False
    



        
