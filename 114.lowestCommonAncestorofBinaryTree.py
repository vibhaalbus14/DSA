# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #-----------------------------------approach 1---------------------------

        #1.first bfs and identify the level of p and q
        #since the ancestor level can be 0 to min only
        #2.create an array of all nodes uptill min level
        #3.pass the nodes from above array in reverse order to check if p and q are reachable
        #if yes,append that node is the result since that's the lowest ancestor possible

        self.pqList=[[0,False],[0,False]] #sublist=[level,if changed]
        self.listOfNodes=[]
        self.ancestor=None
        def bfsTraversalPQ(root,p,q):
            dq=deque()
            dq.append((root,0)) #tup= (node,level)
            while dq:
                tup=dq.popleft()
                if tup[0]==p:
                    self.pqList[0][0]=tup[1]
                    self.pqList[0][1]=True
                else :
                    if tup[0]==q:
                        self.pqList[1][0]=tup[1]
                        self.pqList[1][1]=True
                if self.pqList[0][1] and self.pqList[1][1]:
                    break
                else:
                    if tup[0].left:
                        dq.append((tup[0].left,tup[1]+1))
                    if tup[0].right:
                        dq.append((tup[0].right,tup[1]+1))

        bfsTraversalPQ(root,p,q)
        self.minLevel=min(self.pqList[0][0] , self.pqList[1][0])

        def bfsForNodes(root):
            dq=deque()
            dq.append((root,0))
            while dq:
                tup=dq.popleft()
                node=tup[0]
                level=tup[1]
                if level>self.minLevel:
                    break
                else:
                    self.listOfNodes.append(node)
                    if node.left:
                        dq.append((node.left,level+1))
                    if node.right:
                        dq.append((node.right,level+1))
        bfsForNodes(root)

        def reachability(node,tempList):
            if not node:
                return False
            if node==p:
                tempList[0]=1
            else:
                if node==q:
                    tempList[1]=1
            if sum(tempList)==2: #both p and q reachable from given node
                return True
            else:
                    left= reachability(node.left,tempList)
                    right= reachability(node.right,tempList)
                    return left or right
            
        for num in self.listOfNodes[::-1]:
            if reachability(num,[0,0]):
                self.ancestor=num
                break
        return self.ancestor
    
    #---------------------approach2--------------------------------------
    
        minVal=min(p.val,q.val)
        maxVal=max(p.val,q.val)
        
        while True:
            if root.val<minVal: #is less than both=> not the  lowest common ancestor as not in bw node
                root=root.right
            elif root.val>maxVal: #greater than both, not lcs
                root=root.left
            else:
                return root #if greater than one and less than the other,lcs found
        