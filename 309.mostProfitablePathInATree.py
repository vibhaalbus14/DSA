from collections import defaultdict, deque
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        #aproach
        #1.dfs to identify bob's path
        #2.store the node and the step at which bob reaches
        #3.bfs for alice by keeping track of costs
        #4.compare the steps of bob and alice in deciding the cost to be added

        #adjList
        n=len(edges)+1
        adjList=defaultdict(list)

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visitedBob=[None]*n
        
        #to find bob's path
        def helper(parent,curr,steps):
            nonlocal visitedBob
            flag=False
            if curr==0:
                visitedBob[curr]=steps
                return True

            for neighbour in adjList[curr]:
                if neighbour==parent:
                    continue
                flag=True
                if helper(curr,neighbour,steps+1):
                    visitedBob[curr]=steps
                    return True
            if not flag: #leaf node but not root
                return False
            
        helper(None,bob,0)
        visitedBob[bob]=0

        #to find alice's path with profit
        maxProfit=float("-inf")
        dq=deque()
        dq.append((0,0,0))# alice starts from 0th node with 0 steps=> (node,step,cost)
        visited=set()
        visited.add(0) #keep track of visited nodes

        while dq:
            node,stepsAlice,cost=dq.popleft()
            #amount to be considered ?
            #this will depend on steps of bob and alice

            #check if bob has visited this node
            if visitedBob[node]!=None:
                #check the steps
                if stepsAlice<visitedBob[node]: #alice visites first=> she bears the entire cost
                    amt=amount[node]
                elif stepsAlice>visitedBob[node]:#bob has already visited first
                    amt=0
                else:# both visit the node at the same time
                    amt=amount[node]//2
            else:
                amt=amount[node]
            
            #print("node,amt+cost,stepsAlice",node,amt+cost,stepsAlice)
            flag=False
            
            #check for neighbours
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    flag=True
                    visited.add(neighbour)
                    dq.append((neighbour,stepsAlice+1,cost+amt))
            #do this only if its a leaf node
            if not flag:
                maxProfit=max(maxProfit,cost+amt)

            
        return maxProfit



            


        

            






                        


        