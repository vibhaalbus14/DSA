#time comp=O(n)
#space comp=O(ht of tree) [logn,n]
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def postorderTraversal(root):
    #visit every node's family
    if not root:
         return []
    stack=[root]
    visited=[False]
    array=[]
    
    while stack:
        curr=stack.pop()
        visit=visited.pop()
        #if the node's children are not added,
        #add the node to stack with True
        #add its right and left children with false as their childern are not visited
        if curr:#the leaf nodes have null children, hence to filter them
            if visit:
                array.append(curr.val)
            else:
                stack.append(curr)
                visited.append(True)
                stack.append(curr.right)
                visited.append(False)
                stack.append(curr.left)
                visited.append(False)
    return array
    
    