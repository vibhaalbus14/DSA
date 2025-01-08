# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        res=set()
        def helper(sum,node):
            
            #base case, if the node is null, leaf node is reached=>add the sum along the path
            if not node.left and not node.right:
                res.add(sum+node.val)
                return
            else:
                if node.left:
                    helper(sum+node.val,node.left)
                if node.right:
                    helper(sum+node.val,node.right)
        helper(0,root)
        print(res)
        if targetSum in res:
            return True
        else:
            return False
            