# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution(object):
    def deleteDuplicates(self, head):
        if head==None:
            return []
        elif head.next==None:
            return head
        else:
            #first node is accepted as original
            curr=head.next
            prev=head
            while(curr!=None):
                if(prev.val==curr.val):
                    prev.next=curr.next
                    intermediate=curr
                    curr=curr.next
                    intermediate.next=None
                prev=curr
                curr=curr.next
        return head

head=ListNode(1,ListNode(1,ListNode(2,ListNode(2,ListNode(3,ListNode(3,ListNode(4)))))))
object=Solution()
print(object.deleteDuplicates(head))