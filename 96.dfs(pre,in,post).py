from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def dfs_in_order(self):# left middle right
        if not self.root:
            return []
        array=[]
        def trav(node):
            if node.left:#identify the left node and traverse it
                trav(node.left)

            array.append(node.value)#add the value of current node

            if node.right:#identify the right node and traverse it
                trav(node.right)
        trav(self.root)
        return array
        
        

    def dfs_pre_order(self):#middle left right
        if not self.root:
            return []
        array=[]
        def trav(node):
            array.append(node.value)
            
            if node.left:
                trav(node.left)
            
            if node.right:
                trav(node.right)
        trav(self.root)
        return array

    def dfs_post_order(self):#left right middle
        if not self.root:
            return []
        array=[]
        def trav(node):
            if node.left:
                trav(node.left)
            
            if node.right:
                trav(node.right)
                
            array.append(node.value)
        trav(self.root)
        return array
        



