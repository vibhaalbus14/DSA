# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#time comp: visiting only right nodes, max if it is right skewed= O(n)
#space comp: O(n) where n= nodes of the binary tree
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #if we stand on right side, the right most branch is seen
        #=>dfs along right most branch
        #=>choose right pointer from every node
        #=>right node superimposes the left node and hence left node is not seen
        #=>but if no right node available,then left node has to be seen
        #eg:[1,2] op=>[1,2] eg:[1,2,3,4] op=>[1,2,4]
        #bestway, travel level by level and append the right most node in every level

        if not root:
            return []
        prevLevel=0
        res=[]
        array=[]
        dq=deque()
        dq.append((root,0))

        #level order traversal,
        #at the beginning of every new level, add the last element of the previous level into the res
        while dq:
            tup=dq.popleft()
            node=tup[0]
            level=tup[1]
            if level>prevLevel:
                #new level reached
                res.append(array[-1])
                prevLevel=level
            #add new node values
            array.append(node.val)
            if node.left:
                dq.append((node.left,level+1))
            if node.right:
                dq.append((node.right,level+1))
        #add the final element of array since theres no level change
        res.append(array[-1])
        return res