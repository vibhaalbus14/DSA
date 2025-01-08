from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    #approach
    #1.inorder traversal of tree and create a list of nodes
    #2.make the first value to be -inf
    #3.use pointers to move through the list

    def __init__(self, root: Optional[TreeNode]):
        self.listOfValues=[float('-inf')]
        self.ptr=0
        if not root:
            pass
        else:
            #traverse through the list
            def inorderTraversal(node):
                if node.left:
                    inorderTraversal(node.left)
                self.listOfValues.append(node.val)
                if node.right:
                    inorderTraversal(node.right)
            inorderTraversal(root)
              
    def next(self) -> int:
        #move the pointer to next index and return index val
        self.ptr+=1
        return self.listOfValues[self.ptr]

    def hasNext(self) -> bool:
        next=self.ptr+1
        if next<len(self.listOfValues):
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()