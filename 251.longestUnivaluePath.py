from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        maxLength=0
        if not root:
            return maxLength

        def helper(node):
            nonlocal maxLength
            
            leftCall,leftChildCall=0,0
            rightCall,rightChildCall=0,0

            if node.left:
                leftChildCall=helper(node.left)
            if node.right:
                rightChildCall=helper(node.right)
            
            if node.left and node.left.val==node.val:
                leftCall=leftChildCall+1
            if node.right and node.right.val==node.val:
                rightCall=rightChildCall+1
            
            maxLength=max(maxLength,leftCall+rightCall)
            return max(leftCall,rightCall)
        
        helper(root)
        return maxLength