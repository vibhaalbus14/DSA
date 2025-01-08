class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    
        

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.root=None  

        for num in nums:#creating tree
            newNode=TreeNode(num)
            if self.root is None:
                self.root=newNode
                
            else:
                curr=self.root
                while True:
                    if num<curr.val:
                        if curr.left is None:
                            curr.left=newNode
                            break
                        else:
                            curr=curr.left
                    else:
                        if curr.right is None:
                            curr.right=newNode
                            break
                        else:
                            curr=curr.right
        self.array=[]

        def helper(root):#inorder traversal
            if root.left:
                helper(root.left)
            self.array.append(root.val)
            if root.right:
                helper(root.right)
                
        helper(self.root)
        
        return self.array[-k]
#---------------------------------approach2-------------------------------------------------
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #kth largest element == smallest element of k large integers
        #this implies store smallest element in the beginning
        #perfect ds is minheap
        #heap=[]
        heap=nums
        heapq.heapify(heap)
        #ensure size of heap is k
        while len(heap)>k:
           heapq.heappop(heap)

        # for num in nums:
        #     if len(heap)<k:
        #         heapq.heappush(heap,num)
        #     else:
        #         heapq.heappushpop(heap,num)
        #once it has k top elements, return the first
        return heap[0]

