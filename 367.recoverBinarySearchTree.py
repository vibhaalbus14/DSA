# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #approach
        #1.inorder traversal, store (node address, node val)
        #2.sort the node address acc to node val and compare both
        #3.nodes that dont match are swapped
        #4.interchange the values in these 2 nodes

        inorderTrav=[]

        def inorder(node):
            if node.left:
                inorder(node.left)
            inorderTrav.append((node,node.val))
            if node.right:
                inorder(node.right)
        
        if root:
            inorder(root)
        
        sortedNodes=inorderTrav[:]
        sortedNodes.sort(key=lambda x: x[1])
        
        for i in range(len(sortedNodes)):
            if sortedNodes[i][1]!=inorderTrav[i][1]:
                #swap these nodes
                sortedNodes[i][0].val,inorderTrav[i][0].val=inorderTrav[i][1],sortedNodes[i][1]
                break

