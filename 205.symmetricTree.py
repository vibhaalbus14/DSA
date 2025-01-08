#-------------------------------approach 1= iterative-------------------------------------
from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #approach
        #1.bfs
        #2.everytime a new level is reached, check if the remaining node 
        #value in dq form a palindrom, 
        #3.if yes,proceed adding next level nodes
        #4.if no, return false

        if not root:
            return True
        dq=deque()
        res=[]
        dq.append((root,0))
        overallLevel=0
        while dq:
            node,currLevel=dq.popleft()
            if node:
                res.append((node.val,currLevel))
            else:
                res.append((None,currLevel))
            if node:
                dq.append((node.left,currLevel+1))
                dq.append((node.right,currLevel+1))
            
        def checkPalindrome(i,j):
            while i<j:
                if res[i][0]==res[j][0]:
                    i+=1
                    j-=1
                else:
                    return False
            return True

        #traverse through the res array
        l,r=0,0
        while l<=r and r<len(res):
            if res[l][1]==res[r][1]:#traverse across levels
                r+=1
            else:
                if checkPalindrome(l,r-1):
                    l=r
                else:
                    return False
        return True

#---------------------------------approach2= recursive-------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #approach
        #1.dfs
        #2.pass the nodes whose values u wanna compare

        def helper(leftNode,rightNode):
            #if both children exists
            if leftNode and rightNode:
                if leftNode.val==rightNode.val:
                    return helper(leftNode.left,rightNode.right) and helper(leftNode.right,rightNode.left)
                else:
                    return False
            elif not leftNode and not rightNode:#both nodes dont exist
                #is palindromic/symmetric by default
                return True
            else:
                return False
        
        return helper(root.left,root.right)