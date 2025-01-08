# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        """
        if not root :
            return []
        
        # def treeConst(root):
        #    #create the root node
        #     array=root
        #     rootNode=TreeNode(array[0])
        #     deque=deque([rootNode])
        #     i=1

        #     while i<len(array):
        #         currNode=deque.popleft()

        #         #to create left node
        #         if i<len(array) and array[i] is not None:
        #             currNode.left=TreeNode(array[i])
        #             deque.append(currNode.left)
        #         i+=1
        #         #to create right node
        #         if i<len(array) and array[i] is not None:
        #             currNode.right=TreeNode(array[i])
        #             deque.append(currNode.right)
        #         i+=1

        #     return rootNode
        # ancestor=treeConst(root)

        #---------------------------------------------------------------------
    
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
        return res