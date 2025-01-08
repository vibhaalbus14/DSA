from itertools import permutations
from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #approach:
        #1.identify all possible permutations of the array
        #2.build a bst for all possibilities
        #3.bfs the trees and get the arrays
        #4.store the bfs arrays into set
        #5.return len(set)
        
        array=[i for i in range(1,n+1)]
        listOfPerms=list(permutations(array))

        finalSet=set()

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
            return res

        for numList in listOfPerms:
            finalSet.add(tuple(bfsArray(createTree(numList))))

        return len(finalSet)
#-------------------------------approach 2--------------------------------
#since every node can take turn to become a root node
#the no of unique trees contributed by every unique node=
#  no(trees) given by nodes on left * no(trees) given by nodes on right
#say if 0 nodes=> 1 tree i.e an empty tree
#if one node=> 1 tree i.e tree with only root node

#say if 3 nodes i.e [1,2,3]
#if one is root=>nodes onto left of 1 =0=>trees possible =1
#              =>nodes onto right of 1=2=>trees possible =2
#total trees contributed if one is the root is=> 1*2=2

#if two is root=>nodes onto left of 2 =1=>trees possible =1
#              =>nodes onto right of 2=1=>trees possible =1
#total trees contributed if one is the root is=> 1*1=1

#if three is root=>nodes onto left of 3 =2=>trees possible =2
#              =>nodes onto right of 3=0=>trees possible =1
#total trees contributed if one is the root is=> 2*1=2

#total trees by all the nodes=2+1+2=5

#dynamic programming as the smaller sub problems help in solving the larger ones

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #dp[0 nodes]=1 tree
        #dp[1]=1 tree
        dp=[1]*(n+1) #the storage array,n+1 as tree when zero nodes is also taken
        
        for numNodes in range(2,n+1):
            total=0
            for nodeValue in range(1,numNodes+1):
                rightNodes=numNodes-nodeValue
                leftNodes=nodeValue-1
                total+=dp[leftNodes]*dp[rightNodes]
            dp[numNodes]=total
        return dp[-1]


