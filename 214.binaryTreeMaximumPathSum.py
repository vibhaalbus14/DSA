from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #pre order traversal
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        maxVal=float("-inf")

        #@cache
        def helper(node):
            nonlocal maxVal
            if not node:
                return 0
            
            includeAll=node.val+helper(node.left)+helper(node.right)
            includeLeft=node.val+helper(node.left)
            includeRight=node.val+helper(node.right)

            maxVal=max(maxVal,includeAll,includeLeft,includeRight,node.val)
            return max(includeLeft,includeRight,node.val)
        
        helper(root)
        return maxVal            
#-----------------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #pre order traversal
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        maxVal=float("-inf")

        
        def helper(node):
            nonlocal maxVal
            leftNode=float("-inf")
            rightNode=float("-inf")
            if node.left:
                leftNode=helper(node.left)
            if node.right:
                rightNode=helper(node.right)
            
            maxVal=max(maxVal,rightNode+leftNode+node.val,rightNode+node.val,leftNode+node.val,node.val)
            return max(leftNode+node.val,rightNode+node.val,node.val)
        
        helper(root)
        return maxVal            

        