"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        finalList=[]
        tempList=[]
        dq=deque()
        dq.append((root,0))
        prevLevel=0
        start=0
        #print(root.children)#children are stored under a list
        while dq:
            node,level=dq.popleft()
            if level>prevLevel:
                finalList.append(tempList[start:])
                start=len(tempList)
                prevLevel=level
            tempList.append(node.val)
            for childNode in node.children:
                if childNode.val==None:
                    pass
                else:
                    dq.append((childNode,level+1))
        finalList.append(tempList[start:])
        return finalList


