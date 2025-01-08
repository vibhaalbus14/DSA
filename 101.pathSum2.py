# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return []
        res=[]
        def helper(sum,tempList,node):
            if not node:
                return
            #base case
            if not node.left and not node.right:
                sum+=node.val
                tempList.append(node.val)
                if sum==targetSum:
                    res.append(tempList[:])
                tempList.pop()#to remove leaf node
                return
            else:
                tempList.append(node.val)
                sum+=node.val

                if node.left:
                    helper(sum,tempList,node.left)
                if node.right:
                    helper(sum,tempList,node.right)

            tempList.pop()#to remove the parent node
        helper(0,[],root)
        return res
        