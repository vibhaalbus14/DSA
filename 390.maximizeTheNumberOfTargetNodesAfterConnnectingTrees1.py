import heapq
from typing import List
from collections import defaultdict
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        #approach
        #identify max number of nodes that node 'u' can reach from tree1 such that 'v' is present in both tree1 and tree2 and can be recahed by traversing edges <=k
        #to reach nodes in tree 2, additional edge needs to be added
        #every node is a target to itself with k=0
        n=len(edges1)+1
        m=len(edges2)+1
        

        #build up the adjList for both trees
        adjListTree1=defaultdict(set)
        adjListTree2=defaultdict(set)

        for u,v in edges1:
            adjListTree1[u].add(v)
            adjListTree1[v].add(u)
            

        for u,v in edges2:
            adjListTree2[u].add(v)
            adjListTree2[v].add(u)

        #identify max reachable nodes from every node
        #cannot dfs and memoize. why?
        #because if node 'a' can reach say 4 targets within k steps , it is not guaranteed that node 'b' will also reach these 4 targets with same k steps
        #in example 1, node 0 of tree1  can reach 1,2,3,4 of same tree1  in <=2 steps
        #but node 0 in tree1 cannot reach node 3 in <=2 steps, so cant use the soln of node 0

        
        # def bfs(node,adjList,initial):
        #     visited=set()
        #     count=0
        #     minHeap=[]
            
        #     minHeap.append((initial,node)) #steps,node

        #     while minHeap and minHeap[0][0]<=k:
        #         steps,node=heapq.heappop(minHeap)
        #         count+=1
        #         visited.add(node)

        #         #add its neighbours

        #         for neigh in adjList[node]:
        #             if neigh not in visited:
        #                 heapq.heappush(minHeap,(steps+1,neigh))
        #     return count

        def dfs(node,adjList,initial):

            def helper(node ,prev,steps):
                if steps>k:
                    return 0
                count=1 #include itself
                for neigh in adjList[node]:
                    if neigh == prev:
                        continue
                    count+=helper(neigh,node,steps+1)
                        
                return count

            return helper(node,None,initial)
                    

        #calc max Count for tree2 
        #since to reach any node from tree1 to tree2, an extra edge needs to be added
        #we make use of initial arg

        maxCountTree2=float("-inf")

        for i in range(m):
            maxCountTree2=max(maxCountTree2,dfs(i,adjListTree2,1))
        
        #store all nodes reachabale by a node in tree1 within tree1 in <=k steps
        reachableTree1=[]

        for i in range(n):
            reachableTree1.append(dfs(i,adjListTree1,0))
        
        return list(map(lambda x : x+maxCountTree2,reachableTree1))





        
        