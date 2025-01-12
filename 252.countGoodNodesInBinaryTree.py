# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes=1

        def helper(node,maxVal):
            nonlocal goodNodes

            if node.val>=maxVal:
                maxVal=max(maxVal,node.val)
                goodNodes+=1
            if node.left:
                helper(node.left,maxVal)
            if node.right:
                helper(node.right,maxVal)

        if root.left:
            helper(root.left,root.val)
        if root.right:
            helper(root.right,root.val)

        return goodNodes