class UnionFind:
    def __init__(self,n):
        self.parent=[_ for _ in  range(n)]
        self.rank=[0 for _ in range (n)]

    def find(self,node):
        #nodes range from(1,n) but array is 0 indexed
        if self.parent[node]!=node:
            self.parent[node]=self.find(self.parent[node])#optimisation of path
        return self.parent[node]
    
    def union(self,u,v):
        root1=self.find(u-1)
        root2=self.find(v-1)
        if root1!=root2:
            #check rank to maintain proper height
            if self.rank[root1]>self.rank[root2]:
                #merge the nodes
                #assign parents
                self.parent[root2]=root1
            elif self.rank[root1]<self.rank[root2]:#doesnt change the rannk/height of the tree structure
                self.parent[root1]=root2
            else:#same rank, any merge works
                self.parent[root2]=root1
                self.rank[root1]+=1


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        #identify no of nodes 
        setEdges=set()
        for u,v in edges:
            setEdges.add(u)
            setEdges.add(v)
        n=len(setEdges)
        uf=UnionFind(n) #create an object to UnionFind class
        for u,v in edges:
            if uf.find(u-1)==uf.find(v-1):
                #adding this edge will cause cycle
                #store in latest
                latest=[u,v]
                continue
            
            uf.union(u,v)
        return latest