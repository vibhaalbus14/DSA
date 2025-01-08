class Node:
    def __init__(self,sum,leftRange,rightRange):
        self.sum=sum
        self.leftRange=leftRange
        self.rightRange=rightRange
        self.left=None
        self.right=None

class SegmentTree:
    def buildTree(self,nums,leftRange,rightRange):
        if leftRange==rightRange:#leaf node=>no children
        # just creation of node and assigning value to sum from array
            return Node(nums[leftRange],leftRange,rightRange)
        
        #not a leaf node
        #create a node and pass the sum initially to be zero, since it has to be calculated from its children
        root=Node(0,leftRange,rightRange)
        m=(leftRange+rightRange)//2
        #build left and right subtrees recursively
        root.left=self.buildTree(nums,leftRange,m)
        root.right=self.buildTree(nums,m+1,rightRange)
        #update the sum of parent
        root.sum=root.right.sum+root.left.sum
        return root
    
    #start checking from root
    def update(self,root,index,val):
        #reach the root node and change the vaue of the index
        #once done,reflect the change to its parent and propogate

        #check if leaf node
        if root.leftRange==index and root.leftRange==root.rightRange:
            #found
            root.sum=val
            return 
        m=(root.leftRange+root.rightRange)//2
        if index<=m:
            #check left side
            self.update(root.left,index,val)
        else:
            self.update(root.right,index,val)
        #update parent
        root.sum=root.left.sum+root.right.sum

    #start checking from root
    def checkRange(self,node,l,r):
        if node.leftRange==l and node.rightRange==r:
            return node.sum
        #three ways the given range can be found
        #1.onto the greater side ie l>m
        #2.onto the lesser side i.r r<=m
        #3.else distributed across both sides

        m=(node.leftRange+node.rightRange)//2
        if l>m:
            return self.checkRange(node.right,l,r)
        elif r<=m:
            return self.checkRange(node.left,l,r)
        else:
            return self.checkRange(node.left,l,m)+self.checkRange(node.right,m+1,r)
        
nums=[]
index=2
val=9
l=3
r=5
# if not nums:
#     return []
treeObj=SegmentTree()
start=treeObj.buildTree(nums,0,len(nums)-1)
treeObj.update(start,index,val)
treeObj.checkRange(start,l,r)