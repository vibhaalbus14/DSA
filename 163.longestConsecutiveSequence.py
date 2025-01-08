from typing import List
from collections import counter

class UnionFind:
    def _init__(self,nums):
        self.parent={num:num for num in nums}
        self.rank={num:0 for num in nums}
        
    def find(self,node):
        if self.parent[node]!=node:
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,root1,root2):
        if root1!=root2:
            if self.rank[root1]>self.rank[root2]:
                self.parent[root2]=root1
            if self.rank[root1]<self.rank[root2]:
                self.parent[root1]=root2
            else:
                #same rank
                self.parent[root2]=root1
                self.rank[root1]+=1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #approach=> union-find
        #1.create union find class with parent and rank as hashmaps
        #2.iterate through the nums list
        #3.left and right values of a givnen num are the edges to be connected
        #4.num,prev or num,next as long as it exists in the list
        #5.as usual, unite only if the roots are different
        # 6.return the max occurence of value in parent

        nums=set(nums) #to remove duplicates
        uf=UnionFind(nums)
        visited=set()

        for num in nums:
            if num not in visited: #to avoid redundant checks
                prev=num-1
                next=num+1
                visited.add(num)
                #check if prev exists in nums
                if prev in nums:
                    #possibility to unite only if the have different roots
                    visited.add(prev)
                    rootNum=uf.find(num)
                    rootPrev=uf.find(prev)
                    if rootNum!=rootPrev:
                        uf.union(rootNum,rootPrev)
                #check if next exists in nums
                if next in nums:
                    #possibility to unite only if the have different roots
                    visited.add(next)
                    rootNum=uf.find(num)
                    rootNext=uf.find(next)
                    if rootNum!=rootNext:
                        uf.union(rootNum,rootNext)
                
        for num in nums:#updating the parents
            uf.find(num)
            
        listOfValues=uf.parent.values()
        countMaxParents=counter(listOfValues)
        return max(countMaxParents)

