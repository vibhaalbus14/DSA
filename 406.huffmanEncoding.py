
import heapq

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
    #used to compare in heap, else heap cannot recognise to comapre type TreeNode
    def __lt__(self, other):
        return self.val < other.val



class Solution:
    def huffmanCodes(self,S,f,N):
        # approach
        
        #use minheap to pop out 2 small nos everytime
        #use an adjList to tarck the parent and its children
        #build tree
        #tree values can be alpha or summated integers
       
        minHeap=[]
        
        for i in  range(N):
            heapq.heappush(minHeap,TreeNode(f[i]))
        
        
        while len(minHeap)>1:
            left=heapq.heappop(minHeap)
            right=heapq.heappop(minHeap)
            
            res=left.val+right.val
            newNode=TreeNode(res)
            newNode.left=left
            newNode.right=right
            
            
            heapq.heappush(minHeap,newNode)
            
        root=minHeap[0]
            
        #build tree
        
        res=[]
        
        def preOrder(node,code):
            
            nonlocal res
            
            if not node:
                return None
                
            if not node.left and not node.right:
                res.append(code[:])
                
            if node.left:
                preOrder(node.left,code+'0')
            if node.right:
                preOrder(node.right,code+'1')
                
                
        preOrder(root,'')
                
        return res
                
            
            
            
            
        
        