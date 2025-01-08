# Definition for a binary tree node.

#time complexity:O(n) as every node is visited only once and constant time operation done on every node
#space complexity:O(ht), max ht of the tree ,rec call stack


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    
        #see if every node is within the range as how we insert
        def helper(node,min,max):
            if not node:
                return True
            #can call its children only if the node value is valid
            if node.val>min and node.val<max:

                left=helper(node.left,min,node.val)
                right=helper(node.right,node.val,max)
                #to tell the parent that im valid and my subtree is valid
                return left and right
            else:
                return False
        return helper(root,float("-inf"),float("inf"))