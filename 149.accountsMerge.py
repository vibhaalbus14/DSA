class UnionFind:
    def __init__(self,n):
        self.parent=[_ for _ in range(n)]
        self.rank=[0 for _ in range(n)]

    def find(self,node):
        if self.parent[node]!=node:
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    
    
    def union(self,accounts,index1,index2):
            #here cond1:both have different roots
            root1=self.find(index1)
            root2=self.find(index2)

            if root1==root2:#it means already merged
                return 
            #cond2. indices can be merged iff they have a common mail id
            # # 1 as mail id starts from 1
            # for i in range(1,len(accounts[index1])):
            #     for j in range(1,len(accounts[index2])):
            #         if accounts[index1][i]==accounts[index2][j]:
            email1=set(accounts[index1][1:])
            email2=set(accounts[index2][1:])
            if email1 and email2:#if the intersection is atleast one
                        #common email found
                        #merge index1,index2
                        #if true, merge the indices in parents
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
                        return
            return 
    
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        uf =UnionFind(len(accounts))
        
        #create pairs, loop through accounts and for edges
        #like 0,1 0,2........
        for ptr1 in range(len(accounts)):
            for ptr2 in range(ptr1+1,len(accounts)):
                    uf.union(accounts,ptr1,ptr2)
                    

        #check obj.parent as it contains which indices is to merged with what
        #merge the current index with its root/parent
        setAccounts=[]
        for i in range(len(accounts)):
            uf.find(i) #to update all children and parent root
            
        for index in range(len(uf.parent)):#merging
            if index==uf.parent[index]:
                continue
            accounts[uf.parent[index]]+=accounts[index][1:]

        for val in set(uf.parent):
            name=accounts[val][0]
            emails=sorted(set(accounts[val][1:]))
            setAccounts.append([name]+emails)
        
        return setAccounts




