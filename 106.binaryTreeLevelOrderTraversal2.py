# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root :
            return []
        res=[]
        array=[]
        dq=deque()
        dq.append((root,0))#appending values as tuple of the form (node,its level)
        prevLevel=0
        start=0
        while dq:
            tup=dq.popleft()
            node=tup[0]
            level=tup[1]
            if level>prevLevel:
                res.append(array[start:]) #append the array holding current level elements to res
                start=len(array) #clear the array  
                prevLevel=level #update prevLevel
            array.append(node.val)
            #add nodes's children to dq
            if node.left:
                dq.append((node.left,level+1))
            if node.right:
                dq.append((node.right,level+1))
        #once the dq is empty, append last set of array elements
        res.append(array[start:])
        res.reverse()
        return res
        