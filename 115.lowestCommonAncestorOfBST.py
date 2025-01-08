# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        minVal=min(p.val,q.val)
        maxVal=max(p.val,q.val)
        
        while True:
            if root.val<minVal: #is less than both=> not the  lowest common ancestor as not in bw node
                root=root.right
            elif root.val>maxVal: #greater than both, not lcs
                root=root.left
            else:
                return root #if greater than one and less than the other,lcs found
        