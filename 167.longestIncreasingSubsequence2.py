from typing import List
#approach:
#1.construct a segment tree for all the nums given
#2.traverse the tree to identify Longest consecutive number with diff in value uptill k
#3.wherever the condition fails, start traversing from the next node
#4.return the max count
class SegmentTree:
    def __init__(self,L,R):
        self.right=None
        self.L=L #left Range
        self.R=R #right Range

    def insert(self,node,L,R):
        #gonna be right skewed since its strictly increasing
        curr=node
        while curr.right:
            curr=curr.right
        curr.right=SegmentTree(L,R)
                
    def treeTraversal(self,node,visited):
        curr=node
        count=0
        while curr:
            if curr not in visited:
                visited.add(curr)
                start=curr
                count=1
                print(curr.right)
                while curr.right:
                    print(curr.L)
                    if curr.right.L<=start.R and curr.right.L>start.L:
                        count+=1
                        curr=curr.right
                        start=curr
                    else:
                        curr=curr.right
                print("count : ",count)
                return count
            else:
                curr=curr.right
    


class Solution:
    def __init__(self):
        self.root=None

    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        for num in nums:
            if  self.root==None:
                self.root=SegmentTree(num,num+k)
            #create tree
            else:
                self.root.insert(self.root,num,num+k)
        #check the longest sequence
        #traverse the tree
        visited=set()
        maxCount=0
        for i in range(len(nums)):
            maxCount=max(self.root.treeTraversal(self.root,visited),maxCount)
        return maxCount


        