from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        #convert the ll to nums list
        #recursive equal splitting since the tree is to be heigh balanced

        if not head:
            return head
        
        curr=head
        nums=[]

        while curr:
            nums.append(curr.val)
            curr=curr.next

        def helper(low,high):
            if low==high:
                return TreeNode(nums[low])
            
            mid=(low+high)//2

            root=TreeNode(nums[mid])
            if mid-1>=low:
                root.left=helper(low,mid-1)
            if high>=mid+1:
                root.right=helper(mid+1,high)
        
            return root
        n=len(nums)
        return helper(0,n-1)