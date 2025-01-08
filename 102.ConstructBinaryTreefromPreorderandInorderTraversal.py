#102.ConstructBinaryTreefromPreorderandInorderTraversal.py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        def helper(preorder,inorder,ptr):
            #base case
            if ptr>=len(preorder) or len(inorder)<=0:
                return None
            
            rootVal=preorder[ptr]
            root=TreeNode(rootVal)

            for i,num in enumerate(inorder):
                if num==rootVal:
                    leftSubTree=inorder[:i]
                    rightSubTree=inorder[i+1:]
                    break

            root.left=helper(preorder,leftSubTree,ptr+1)
            root.right=helper(preorder,rightSubTree,ptr+len(leftSubTree)+1)
            
            return root
        return helper(preorder,inorder,0)
        

        