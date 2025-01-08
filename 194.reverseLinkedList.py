# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #approach
        #1.traverse through the ll and identify prev,left
        #2.traverse through the ll and identify right,succ
        #3.prev.next=right and left.next=succ
        #4.now from left to right,make changes in "next" pointers

        if left==right or not head:
            return head
        
        #to identify prev,left
        curr=head
        prev=None
        count=1
        while count!=right:
            if count==left:
                leftNode=curr
                prevNode=prev
            prev=curr
            curr=curr.next
            count+=1
        rightNode=curr
        succNode=rightNode.next
       
        #rechange 
        if prevNode!=None:
            prevNode.next=rightNode

        curr=leftNode.next
        leftNode.next=succNode

        #reverse the list
        before=leftNode
        while curr and curr!=succNode:
            after=curr.next
            curr.next=before
            before=curr
            curr=after

        if left==1:
            head=rightNode
        return head

