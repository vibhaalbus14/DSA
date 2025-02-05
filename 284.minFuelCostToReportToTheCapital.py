from typing import List
from collections import defaultdict
import math

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        #fuel is calculated by ceil(currPeople/seats)
        #this is done at every child step and returned to parent
        #no of cars from each node=amt of fuel
        #no cars=currPeople/total seats per car

        adjList=defaultdict(list)
        for u,v in roads:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node,parent):
            nonlocal totalFuel
            currPeople=1#curr node is one person in car
            for neighbour in adjList[node]:
                if neighbour!=parent:
                    currPeople+=dfs(neighbour,node)
            totalFuel+=math.ceil(currPeople/seats) #no ofcars from each node=> amt of fuel from each node
            return currPeople
        
        totalFuel=0
        for neighbour in adjList[0]:
            dfs(neighbour,0)
        return totalFuel
