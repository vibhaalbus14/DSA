# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        
        if not root:
            return ""  
        
        dq = deque([root])
        listOfNodeValues = []
        
        while dq:
            node = dq.popleft()
            if not node:
                listOfNodeValues.append('None')
            else:
                listOfNodeValues.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)

        return  "$".join(listOfNodeValues)   

    def deserialize(self, data):
        
        if data == "" :
            return None  
        
        listOfIntNodes = data.split("$") 
        dq = deque()
        start = TreeNode(int(listOfIntNodes[0]))  
        dq.append(start)
        ptr = 1 

        while dq:
            node = dq.popleft()

            if ptr < len(listOfIntNodes) and listOfIntNodes[ptr] != 'None':
                node.left = TreeNode(int(listOfIntNodes[ptr]))
                dq.append(node.left)
            ptr += 1

            if ptr < len(listOfIntNodes) and listOfIntNodes[ptr] != 'None':
                node.right = TreeNode(int(listOfIntNodes[ptr]))
                dq.append(node.right)
            ptr += 1
        
        return start
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))