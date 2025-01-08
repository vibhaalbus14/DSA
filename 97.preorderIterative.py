#time comp:O(n)
#space comp:O(ht of tree)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    if not root:
        return []
    stack=[root]
    array=[]
    while stack:
        #pop the middle node  and append its value to array 
        node=stack.pop()
        array.append(node.val)
        #since left is needed before right, left is appended in the end as stack is LIFO
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return array