from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]],src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for u, v, w in flights:
            adjList[u].append((v, w))

        minHeap = [(0, src, 0)]  # (price, node, stops)
        visited = {} #node= [price]

        while minHeap:
            price, node, stops = heapq.heappop(minHeap)

            if node == dst:
                return price

            # track the visit of every node,along with the steps it took to visit
            #if node is already visited with less stop than current stop, skip this iteration
            if node in visited and visited[node] <= price:
                continue
            visited[node] = price

            if stops <= k:
                for neighbor, nextCost in adjList[node]:
                    heapq.heappush(minHeap, (price + nextCost, neighbor, stops + 1))

        return -1
