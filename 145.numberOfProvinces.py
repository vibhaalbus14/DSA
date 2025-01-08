from collections import deque
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        #no of components in given matrix == no of provinces
        #do bfs
        #no of times u cal bfs==no of provinces
        rows=cols=len(isConnected)
        if rows==0 : 
            return 0
        elif rows==1:
            return 1

        def bfsTrav(node):
            dq=deque()
            dq.append(node)
            visited.add(node)
            while dq:
                node=dq.popleft()
                #check its neighbours
                #4 adjacency
                #left, right,top,bottom
                if d[node]==[]:
                    continue
                else:
                    for neighbour in d[node]:
                        if neighbour not in visited: 
                            dq.append(neighbour)
                            visited.add(neighbour)

        d={i:[] for i in range(rows)}
        provinces=0
        visited=set()

        #creating adjcency list
        for i in range (rows):
            for j in range(cols):
                if isConnected[i][j]==1 :
                    d[i].append(j)
                    
        for node in range(rows):
            if node not in visited:
                bfsTrav(node)
                provinces+=1
        return provinces
        