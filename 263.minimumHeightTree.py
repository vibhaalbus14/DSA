from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #construct adj list
        #make every node as root and start
        #bfs such that all nodes are reached
        adjList=defaultdict(list)
        for u,v in edges:
           adjList[u].append(v)
           
           adjList[v].append(u)
           
        #arrange the nodes in descending order of their values/children

        def bfs(node):
            dq=deque()
            visited=set()
            maxHeight=0

            dq.append((node,0)) #root,height
            visited.add(node)
            flag=0
            while dq:
                node,height=dq.popleft()
                maxHeight=max(height,maxHeight)
                if maxHeight>finalHeight:
                    flag=1
                    break
                for neighbour in adjList[node]:
                    if neighbour not in visited:
                        dq.append((neighbour,height+1))
                        visited.add(node)
            if not flag:
                return maxHeight
            else:
                return float("inf")


        finalRoots=[] #root,height obt
        correspondingHeights=[]
        finalHeight=float("inf")
        
        for i in range(n):
            currHeight=bfs(i)
            if currHeight<finalHeight:
                finalHeight=currHeight
                #traverse the list and pop all larger heights
                while finalRoots and correspondingHeights[-1]>currHeight:
                    correspondingHeights.pop()
                    finalRoots.pop()
                finalRoots.append(i)
                correspondingHeights.append(currHeight)
            elif currHeight==finalHeight:
                finalRoots.append(i)
                correspondingHeights.append(currHeight)

        return finalRoots
#----------------------------approach 2-------------------------------------
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #approach1 
        #construct adj list
        #make every node as root and start
        #bfs such that all nodes are reached
        #-------------------------------------------
        #approach 2
        #1.start from nodes with indegree 1 as they def dont make min Height
        #2.remove its neighbours indegree and append to dq if it is also 1 indegree
        #3. most imp question , why 2nd loop on line 30?
        #ans. because , eventually all the nodes after deleting its indegrees
        #will have 1 indegree and get popped ou
        #there's theory saying that max root like nodes can only be 1 or 2
        #to ensure we dont pop all out or to ensure that we dont
        #say its 2 nodes when the answer is 1, we initially capture the 
        #length of leaf nodes added to dq , and for every pop, we dec remNodes
        #when the initial count is reached, we check if remNodes<=2, if not
        #proceed deleting next set of nodes already appended in dq
        if not edges:
            return [0] #this means only one node 
        adjList=defaultdict(list)
        indegree=[0 for _ in range(n)]
        for u,v in edges:
           adjList[u].append(v)
           indegree[v]+=1
           adjList[v].append(u)
           indegree[u]+=1
        
        dq=deque()
        for i,val in enumerate(indegree):
            if val==1:
                dq.append(i)
        
        nodesRem=n
        while dq:
            initialLength=len(dq)
            if nodesRem<=2:
                return list(dq)
            for i in range(initialLength):
                node=dq.popleft()
                nodesRem-=1
                for neigh in adjList[node]:
                    indegree[neigh]-=1
                    if indegree[neigh]==1:
                        dq.append(neigh)



