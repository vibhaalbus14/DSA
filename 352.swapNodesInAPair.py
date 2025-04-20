from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        if not head.next:
            return head

        l=head
        r=head.next
        prev=ListNode(-1)
        head=prev

        while r:
            l.next=r.next
            r.next=l
            prev.next=r #make the prev run start to point to swapped start
            prev=l
            if l.next!=None:
                l=l.next
                r=l.next
            else:
                return head.next
            
        
        return head.next

        