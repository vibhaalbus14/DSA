# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        #similar to level order
        #flag is used to check if it is to be printed from l -> r or r -> l for every new level
        #flag=0 =>l->r and 1 => r->l
        res=[]
        array=[]
        dq=deque()
        dq.append((root,0))#appending values as tuple of the form (node,its level)
        prevLevel=0
        start=0
        flag=0#initially left to right
        while dq:
            tup=dq.popleft()
            node=tup[0]
            level=tup[1]
            if level>prevLevel:
                if flag==0:
                    res.append(array[start:]) #append the array holding current level elements to res #l->r
                    flag=1
                else:
                    if(flag==1):
                        res.append(array[:start-1:-1])#r->l
                        flag=0
                start=len(array) #clear the array  
                prevLevel=level #update prevLevel
            array.append(node.val)
            #add nodes's children to dq
            if node.left:
                dq.append((node.left,level+1))
            if node.right:
                dq.append((node.right,level+1))
        #once the dq is empty, append last set of array elements
        if flag==0:
            res.append(array[start:])
        else:
             res.append(array[:start-1:-1])
        return res