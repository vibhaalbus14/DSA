from typing import List
from collections import defaultdict
from functools import lru_cache

class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        if k==0:
            return 0
        adjList=defaultdict(list)

        for u,v,w in edges:
            adjList[u].append([v,w])

        total=-1
        @lru_cache(None)
        def dfs(node,currSum,edges):
            nonlocal total
            # print(node,currSum,edges)
            if edges==k and currSum<t:
                total=max(currSum,total)

            if node in adjList:
                for neigh,wt in adjList[node]:
                    # if neigh not in visited:
                    if edges+1>k or currSum+wt>=t:
                            #dont continue with this path
                        continue
                    else:
                        dfs(neigh,currSum+wt,edges+1)

        for i in range(n):
            dfs(i,0,0)

        return total 
                                

                            
                    
                    
        