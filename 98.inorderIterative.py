#time comp =O(n) as each node is visited exactly once
#space comp= O(ht) ht can be logn gor ht balanced tree or n for skewed tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    #write code here
    if not root:
        return []
    curr=root
    stack=[]
    array=[]
    while curr or stack:#no of nodes
        #go as left as possible
        while curr:#max no of times this occurs=max ht of left nodes
            stack.append(curr)
            curr=curr.left
            
        #pop the middle node
        node=stack.pop()
        array.append(node.val) 
        
        #go to the right of popped node
        curr=node.right
    return array
        
        