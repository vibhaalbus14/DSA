# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #the no of edges n longest path=diameter
        #identify diameter for every subtree since the longest path needn't necessarily be from root
        #return the max edges of the subtree from left or right to parent

        
        #to support nonlocal function, make this a list
        #wrap the value in mutable container to make make chnages in nested functions
        maxDiameter=[0]
        def helper(node):
            #nonlocal not supported by python 2 which leetcode uses,henc make it a list
            #nonlocal maxDiameter
            
            if not node:
                return 0

            #identify current Diameter and maxDiameter
            left=helper(node.left)
            right=helper(node.right)
            currDiameter=left+right
            maxDiameter[0]=max(currDiameter,maxDiameter[0])

            #return the longest path to parent,i.e longest path from parent to leaf node 
            return 1+max(left,right)
        helper(root)
        return maxDiameter[0]