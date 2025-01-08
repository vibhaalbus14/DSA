# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #construct dic holding {key: value} as {node.val:its col} using bfs
        #as the elements are not unique, use list instead of dict
        if not root:
            return []
        dq=deque()
        tupList=[]
        dq.append((root,0,0))#append tuple as(node,its col,its row)
        while dq:
            tup=dq.popleft()
            node=tup[0]
            col=tup[1]
            row=tup[2]
            tupList.append((node.val,col,row))#adding to dict

            #left child
            if node.left:
                dq.append((node.left,col-1,row+1))
            if node.right:
                dq.append((node.right,col+1,row+1))
        #first sort, acc to node values
        itemList=sorted(tupList,key= lambda item: item[0])
        #second sort, acc to row values
        itemList=sorted(itemList,key = lambda item: item[2])
        #third sort,acc to column values
        itemList=sorted(itemList,key = lambda item: item[1])
        tempList=[]
        res=[]
        tempList.append(itemList[0][0])#appending node value
        start=0
        for i in range(1,len(itemList)):
            if itemList[i-1][1]!=itemList[i][1]:
                res.append(tempList[start:])
                start=len(tempList)
            tempList.append(itemList[i][0])
        #append the last set of items from tempList to res
        res.append(tempList[start:])
        return res


        



        