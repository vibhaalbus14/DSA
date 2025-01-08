# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        #swap the left and right nodes of a tree
        if not root:
            return None
        def helper(node):
            if not node.right and not node.left: #base case=>leaf node
                return node
            if not node: #null node
                return 
            
            temp=node.left #swap using temp
            node.left=helper(node.right)
            node.right=helper(temp)
            return node
        return helper(root)
         
        