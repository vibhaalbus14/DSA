from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def bread_first(self):
        if self.root==None:#tree empty
            return []
        array=[]
        queue=deque()

        #add the root node into queue
        queue.push(self.root)
        while len(queue)!=0:
            #pop the leftmost element from queue
            node=queue.popleft()
            #add the popped value into array
            array.append(node.value)
            #add the left and right children of the node into queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
        return array
        
        



