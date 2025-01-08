# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        def helper(inorder,postorder,ptr):
            #base case
            if ptr<0 or len(inorder)<=0:
                return None
            else:
                #root node is identified from the end of postorder
                #excact location is identified from inorder
                rootValue=postorder[ptr]
                root=TreeNode(rootValue)

                #identify the index of rootValue in inorder
                for i,num in enumerate(inorder):
                    if num==rootValue:
                        leftSubTree=inorder[:i]
                        rightSubTree=inorder[i+1:]
                        break
                #make the root point
                root.right=helper(rightSubTree,postorder,ptr-1)
                root.left=helper(leftSubTree,postorder,ptr-len(rightSubTree)-1)

                return root #this is returned, i.e the root of current rec call
            #is returned as left or right to make the prev rec calls's root point to this node
        return helper(inorder,postorder,len(postorder)-1)
