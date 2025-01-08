from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #approach
        #1.traverse the tree recursively 
        #2.create a node of ll everytime the node is not null
        start=None
        tail=None
        
        def createLinkedList(node):
            nonlocal start,tail
            #create an ll node
            newNode=TreeNode(node.val)
            if start==None:
                start=newNode
                tail=newNode
            else:
                tail.right=newNode
                tail=newNode

        def preOrderTraversal(root):
            createLinkedList(root) #creation of node
            if root.left:
                preOrderTraversal(root.left)
            if root.right:
                preOrderTraversal(root.right)

        if  root:
            preOrderTraversal(root)
            root.val=start.val
            root.left=None
            root.right=start.right
        '''
        why root =start did not give right op?

        ans: initially root =>ori tree node
        after root=start, root points to wherever start was pointing
        but this is seen locally only within the function .Thus , root=start only updates the local 
        ref, but when root is accessed from outside by an object, root still continues to point to 
        ori tree node. Thus , changes did not persist

        why root.right=start.right worked?

        ans: by doing this line, we modify the internal structure of tree node, i.e the original root of the 
        tree is modified and is made to point to new Tree's node. Since,the original structure is modified,
        changes persisted.

        '''
        
#----------------------approach 2---------------------------------
#time comp : O(n)
#space comp: O(h)=> h= ht of bin tree , rec call stack
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #approach
        #1.find the atomic subtree
        #2.make the left most point to rightmost node
        #3.make the parent's rightpointer point to leftmost node
        #4.do this recursively to make in place changes
        if not root:
            return
        
        def preorderTraversal(root):
            if not root: 
                return None
            
            leftSide=preorderTraversal(root.left)
            rightSide=preorderTraversal(root.right)

            if leftSide:
                leftSide.right=root.right
                root.right=root.left
                root.left=None
            return rightSide or leftSide or root
        
        preorderTraversal(root)
            
            

