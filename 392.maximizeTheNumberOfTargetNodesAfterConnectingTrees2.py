from collections import defaultdict, deque
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        #same as 1
        #but in tree2 identify  how many nodes can be reached in even steps till the end
        #store the max
        #like wise for tree1
        #finally add it up

        #if we check, the nodes are grouped together be it  even or odd
        #this will make us pick the largest group from tree2 to maximise
        #in tree1, make note of both groups and nodes present in each grp and use that accordingly
        n=len(edges1)+1
        m=len(edges2)+1

        adjListTree1=defaultdict(set)
        adjListTree2=defaultdict(set)

        for u,v in edges1:
            adjListTree1[u].add(v)
            adjListTree1[v].add(u)
        
        for u,v in edges2:
            adjListTree2[u].add(v)
            adjListTree2[v].add(u)

        odd=set()
        even=set()

        def findGroups(node,adjList,initial):
            nonlocal odd,even

            #start from this node
            #maintain 2 sets odd and even and a visited set
            odd,even,visited=set(),set(),set()

            #if a node is reached in odd steps=> add to odd
            #like wise for even

            #since this is solely for tree2, imaginary edge from tree1 to tree2
            #as connecting edge is already used
            #so this has to be taken into account

            dq=deque()
            dq.append((initial,node)) #steps,node

            while dq:
                steps,node=dq.popleft()
                visited.add(node)
                if steps%2==0:
                    even.add(node)
                else:
                    odd.add(node)

                for neigh in adjList[node]:
                    if neigh not in visited:
                        dq.append((steps+1,neigh))

            #return the larger grp size
            return max(len(odd),len(even))
            
        #identiyy largest grp taht can be reached in tree2
        #initial=1 because edge used toconnect tree1 and tree2
        maxGrpSizeTree2=findGroups(0,adjListTree2,1) 

        odd=set()
        even=set()

        res=[]
        findGroups(0,adjListTree1,0)
        p=len(even)
        q=len(odd)

        for i in range(n):
            if i in even:
                res.append(p+maxGrpSizeTree2)
            else:
                res.append(q+maxGrpSizeTree2)
        return res

        