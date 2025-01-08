# Definition for a binary tree node.
from itertools import permutations
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        #approach:
        #1.identify all possible permutations of the array
        #2.build a bst for all possibilities
        #3.bfs the trees and get the arrays
        #4.store the bfs arrays into finalList
        #5.everytime a unique bfs array is added,it means a unique tree=>add the start to finalRoots
        #6.return the finalRoots
        
        array=[i for i in range(1,n+1)]
        listOfPerms=list(permutations(array))

        finalList=[]
        finalRoots=[]

        def createTree(numList):
            root=None
            for num in numList:
                newNode=TreeNode(num)
                if root==None:
                    root=newNode
                else:
                    curr=root
                    while True:
                        if num<curr.val:
                            if not curr.left:
                                curr.left=newNode
                                break
                            curr=curr.left
                        else:
                            if not curr.right:
                                curr.right=newNode
                                break
                            curr=curr.right
            return root   

        def bfsArray(root):
            start=root
            dq=deque()
            res=[]
            dq.append(root)
            while dq:
                node=dq.popleft()
                if node!=None:
                    res.append(node.val)
                    
                    dq.append(node.left)
                    
                    dq.append(node.right)
                else:
                    res.append(None)
            return (res,start)

        for numList in listOfPerms:
            
            listOfNodes,root=bfsArray(createTree(numList))
            if listOfNodes not in finalList:
                finalList.append(listOfNodes)
                finalRoots.append(root)                

        return finalRoots
        