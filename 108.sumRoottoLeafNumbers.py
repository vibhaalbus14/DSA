# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res=[]
        def helper(root,tempList):
            if not root.left and not root.right:#leaf node encountered
                #add the leaf node value to tempList
                tempList.append(str(root.val))
                #join the list and append as int  to result
                res.append(int(("").join(tempList)))
                tempList.pop()
                return
            else:
                tempList.append(str(root.val))
                if root.left:
                    helper(root.left,tempList)
                if root.right:
                    helper(root.right,tempList)
                tempList.pop()#to pop the parent element

        helper(root,[])
        return sum(res)