from typing import List
from collections import defaultdict
import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #create an adjacent list
        #every var represents a node
        #similar to dijkstra's algo
        #try every possibility till a numeric value is found


        finalList=[]
        adjList=defaultdict(list)
        #build adj list
        for i,fraction in enumerate(equations):
            numerator,denominator=fraction
            val=values[i]
            adjList[numerator].append([denominator,val])
            adjList[denominator].append([numerator,(1/val)])
        
        #bfs approach
        for numerator,denominator in queries:
            if numerator not in adjList:
                finalList.append(-1)
                continue
            dq=deque()
            visited=set()
            dq.append([numerator,1])
            visited.add(numerator)
            totalVal=1
            flag=0
            while dq:
                variable,value=dq.popleft()
                #print(totalVal)
                if variable==denominator:
                    finalList.append(value)
                    flag=1
                    break
                for neighbour,neighVal in adjList[variable]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        dq.append([neighbour,neighVal*value]) #dont change the value globally, but pass
                        #this change for every node u visit
            if not flag:
                finalList.append(-1)

        return finalList

        
       
                

                


            
            

        