from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        #must consider nodes even if they dont have apple , but lead to apple
        #dfs is effective
        #graph approach
        #only cycle is parent-> child and vice versa
        #track parent and child so that this cycle is avoided

        adjList={}
        for i in range(n):
            adjList[i]=[]
        
        for parent,child in edges:
            adjList[parent].append(child)
            adjList[child].append(parent)

        def dfs(node,parent):
            time=0
            subtreeTime=0
            for neigh in adjList[node]:
                if neigh ==parent:
                    continue
                subtreeTime+=dfs(neigh,node)
                
                #subtreetime check must hape
            if subtreeTime :  #if my path contains apples, then i have to submit the time taken
                #to reach me
                if node!=0:
                    time+=subtreeTime+2
                else:
                    time=subtreeTime
            
            elif hasApple[node]:#consider time taken to reach me only if i have an apple
                if node!=0:
                    time+=2
                
            
            return time #dont consider me nor my subtree, we dont have apples to collect
        
        return dfs(0,-1)
    
#case where bidirectional edges are necessary
#edges=[[0,2],[0,3],[1,2]]
#hasApple=[false,true,false,false]








        