# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #approach
        #identiy the maxDepth
        #return the depth of each node to parent
        #if parent receives ans from childern and that is equal to maxDepth=> send lca to this parent
        #else keep sending the maxDepth further up towards root

        maxDepth=float("-inf")
        lca=None

        def dfs(node,currDepth):
            nonlocal maxDepth,lca
            maxDepth=max(maxDepth,currDepth)
            rightDepth,leftDepth=0,0
            if node.left:
                leftDepth=dfs(node.left,currDepth+1)
            if node.right:
                rightDepth=dfs(node.right,currDepth+1)
            if currDepth==maxDepth:
                lca=node
            elif rightDepth==leftDepth==maxDepth:
                lca=node
                
            return max(rightDepth,leftDepth,currDepth)
        dfs(root,0)
        return lca



