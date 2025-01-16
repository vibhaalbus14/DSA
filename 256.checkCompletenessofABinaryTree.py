from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        dq=deque()
        dq.append(root)
        while dq:
            node=dq.popleft()
            if node==None:
                if dq and dq[0]!=None:#ensures null right nodes aren't in bw
                        return False
            elif not node.left and node.right: #ensures left is there for a right
                return False
            if node:
                dq.append(node.left)
                dq.append(node.right)
        return True
        
        