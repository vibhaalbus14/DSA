# Definition for a binary tree node.
from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #recursive approacxh by passing along the pre and post order lists
        #1.indentify the position of left child
        #2.indentify the length of left sub tree
        #3. pass the arrays acc.

        def helper(pre,post):
            if not pre:
                return None

            root=TreeNode(pre[0])

            if len(pre)==1:
                return root
            
            #identify immediate left child
            leftSubtreeRoot=pre[1]
            #get the size of this tree from postorder
        
            leftSize=post.index(leftSubtreeRoot)+1 #including the leftSubTreeRoot

            root.left=helper(pre[1:leftSize+1],post[:leftSize])#for preorder it is leftSize+1, to create the root, but for postOrder it is leftSize only
            root.right=helper(pre[leftSize+1:],post[leftSize:-1])

            return root

        return helper(preorder,postorder)
