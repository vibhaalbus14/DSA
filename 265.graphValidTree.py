from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #cycles in directed=> topological sort
        #cycles in undirected=> union find
        #if not a parent but in visted=> dfs
        #and also connect components!
        parent=[]
        rank=[]
        for i in range(n):
            parent.append(i)
            rank.append(0)
        
        def find(node):
            while parent[node]!=node:
                node=parent[node]
            return parent[node]
        
        def union(u,v):
            root1=find(u)
            root2=find(v)
            
            if root1==root2:#cycles
                return False
            if rank[root1]>rank[root2]:
                parent[root2]=root1

            elif rank[root1]<rank[root2]:
                parent[root1]=root2
            else:
                parent[root2]=root1
                rank[root1]+=1
            return True

        for u,v in edges:
            if not union(u,v):
                return False
        
        #now check if all nodes are connected
        parentSet=set(parent)
        if len(parentSet)>1:
            return False
        return True

            


        