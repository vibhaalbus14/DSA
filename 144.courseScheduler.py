#time comp of find: O(n) n=no of nodes
#time comp of union:O(n*alpha(m)) where alpha(m)=inverse ackermann function is assumed to be O(1) for all inputs
# class UnionFind:
#     def __init__(self,n):
#         self.parent=[i for i in range(n)]#initially all nodes are its parents
#         self.rank=[0 for i in range(n)] #all are at same height

#     def find(self,node):
#         if self.parent[node]!=node:
#             self.parent[node]=self.find(self.parent[node])
#         return self.parent[node] #path optimization
#     #all nodes are connected to same root, so that find works effectively

#     def union(self,u,v):
#         #check the root
#         root1=self.find(u)
#         root2=self.find(v)
#         if root1!=root2:
#             if self.rank[root1]>self.rank[root2]:#to keep the height balanced
#                 self.parent[root2]=root1
#             elif self.rank[root1]<self.rank[root2]:#to keep the height balanced
#                 self.parent[root1]=root2
#             else:
#                 if self.rank[root1]==self.rank[root2]:
#                     #anyway is fine
#                     self.parent[root2]=root1
#                     self.rank[root1]+=1

# class Solution(object):
#     def canFinish(self, numCourses, prerequisites):
#         """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#         """
#         # numCourses == num of nodes
#         #prerequisites == adjacency List
#         uf=UnionFind(numCourses)
#         for want,must in prerequisites:
#             root1=uf.find(want)
#             root2=uf.find(must)
#             if root1==root2:
#                 return False 
#             #as these nodes are already present in same component, uniting these vertices
#             #can lead to cycle formation in graph represented by unionfind
#             else:
                
#                 uf.union(must,want)
    
#         return True
        
#------------------------------approach2-----------------------------
from collections import deque
from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #numCouses=nodes
        #prerequisites=list of edges
        if not prerequisites or numCourses==0:
            return True

        #loop through wants 
        #if must there in want, do not add
        #if must empty, return false
        #else create adjacency list and do bfs
        wanted=set()
        isMust=set()

        for want,must in prerequisites:
            wanted.add(want)
            
        for want,must in prerequisites:
            if must not in wanted:
                isMust.add(must)
                
        if len(isMust)==0:
            #no place to start the graph=>circular dependency
            return False
        
        dq=deque()
        visited=set()
        d=defaultdict(list)
        #creating an adjacency list from must side
        for want,must in prerequisites:
            d[must].append(want)
        #populating the deque with must
        for num in isMust:
            dq.append(num)
            visited.add(num)
        
        #bfs traversal
        while dq:
            node=dq.popleft()
            #check for neighbours from adjacencyList==d
            if node in d:
                for neighbour in d[node]:
                    if neighbour  not in visited:
                        dq.append(neighbour)
                        visited.add(neighbour)
        #checking if all the nodes listed in prerequisites are visited
        return len(visited)==(len(wanted)+len(isMust))
    
#----------------------approach----------------------------------------------------------------

from collections import deque
from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #numCouses=nodes
        #prerequisites=list of edges
        if not prerequisites or numCourses==0:
            return True
        
        dq=deque()
        d=defaultdict(list)
        #creating an adjacency list from must side
        for want,must in prerequisites:
            d[must].append(want)

        #bfs trav
        def bfsTrav(node):
            visited=set()
            dq.append(node)
            start=node
            while dq:
                node=dq.popleft()
                if node ==start and node in visited:#cycle detection
                    return False
                elif node in visited:
                    continue
                visited.add(node)
                #check for neighbours from adjacencyList==d
                if node in d:
                    for neighbour in d[node]:
                            dq.append(neighbour)
            return True

        for key in d.keys():
            if not bfsTrav(key):
                return False
        return True
#----------------------------------approach-----------------------------------------
#topological sorting
#all the edges of the form a->b in graph is arranged such that a comes first before b
#this helps to detect cycle in graph
#applicable only for DAG


class Solution(object):
    def canFinish(self, numCourses, prerequisites):#rec soln
        if not prerequisites or numCourses==0:
                return True

        def topologicalSort(node):
            #remove the node 
            #increment the count
            self.count+=1
            output.add(node)
            #remove the indegrees to which it was pointing
            if d[node]==[]:
                pass #no neighbours
            else:
                for neighbour in d[node]:
                    indegree[neighbour]-=1
            #rec call, identify next zero
            for i in range(len(indegree)):
                if indegree[i]==0 :
                    if i not in output:
                        topologicalSort(i)
                        break
            return
                
        indegree=[0 for _ in range(numCourses)]
        d={i:[] for i in range(numCourses)}
        self.count=0
        output=set()
        #build adjacency list as well as populate the indegree
        for want,must in prerequisites:
            d[must].append(want)
            indegree[want]+=1
        for i in range(len(indegree)):
            if indegree[i]==0:
                #pass the node with indegree 0 to topological sort
                topologicalSort(i)
                break
        if self.count==numCourses:
            return True
        else:
            return False
