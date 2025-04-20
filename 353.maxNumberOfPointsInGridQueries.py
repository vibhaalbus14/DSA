import heapq
from collections import defaultdict,deque
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        #approach
        #1.rather than visiting top left cell for every query
        #2.we will sort the query
        #3.so that i+1th query will obviously have points obt by ith query and extra 
        #4.we do so by using a global visited, and minheap,
        #5.minheap is to ensure that the value added to dq is always lesser than ith query

        m=len(grid)
        n=len(grid[0])
        hashMap=defaultdict(set)
        for i, num in enumerate(queries):
            hashMap[num].add(i)
        
        res=[0]*len(queries)
        queries.sort()

        visited=set()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        minHeap=[(grid[0][0],0,0)] #num,r,c
        total=0

        def bfs(val):
            nonlocal total,visited,minHeap
            dq=[]
            
            while minHeap and minHeap[0][0]<val:
                node,r,c=heapq.heappop(minHeap)
                # if (r,c)  in visited:#since dup instances can be added to minHeap
                #     continue
                dq.append((r,c))
                visited.add((r,c))
            
            while dq:
                r,c=dq.pop()
                total+=1
                for tr,tc in directions:
                    nr=tr+r
                    nc=tc+c

                    if nr>=0 and nr<m and nc>=0 and nc<n and (nr,nc) not in visited:
                        if grid[nr][nc]<val:
                            dq.append((nr,nc))
                            
                        else:
                            heapq.heappush(minHeap,(grid[nr][nc],nr,nc))
                        visited.add((nr,nc))
            return total
        
        for num in queries:
            ans=bfs(num)
            for index in hashMap[num]:
                res[index]=ans
        
        return res
            
        

        

        