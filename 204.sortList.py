from typing import List,Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def findMiddle(head):
            slow=head
            fast=head

            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next

            return slow
        
        def merge(leftList,rightList):#compare using 2 pointers
            l,r=leftList,rightList
            while l and r:
                if leftList.val<rightList.val:
                    pass

        
        def divide(head):
            if not head or head.next:
                return head
            mid=findMiddle(head)
            rightPart=mid.next
            mid.next=None
            leftAtomicPart=divide(head)
            rightAtomicPart=divide(rightPart)

            return merge(leftAtomicPart,rightAtomicPart)