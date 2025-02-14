# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not subRoot and root) or (subRoot and not root):
            return False
        if not subRoot and not root:
            return True

        def helper(nodeMain,nodeSub):
            if not nodeMain and  not nodeSub:
                return True
            if not nodeMain or not nodeSub:
                return False

            if nodeMain.val!=nodeSub.val:
                return False
            if nodeMain.val==nodeSub.val:
                #traverse both the trees 
                leftCallMatch=helper(nodeMain.left,nodeSub.left)
                rightCallMatch=helper(nodeMain.right,nodeSub.right)

            return leftCallMatch and rightCallMatch

        def traverse(nodeMain):
            if not nodeMain:
                return False
            if helper(nodeMain,subRoot):
                return True
            else:
                leftCall=traverse(nodeMain.left)
                rightCall=traverse(nodeMain.right)

            return leftCall or rightCall
        
        return traverse(root)
        