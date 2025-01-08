# Definition for singly-linked list.
#time complexity:O(n)+O(n^2)for recursion=>O(n^2)
#space complexity:O(n) due to rec call stack
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swap(self,curr,tail):
        temp=curr.val
        curr.val=tail.val
        tail.val=temp

    def reverseList(self, head):

        if head==None or head.next==None:
            return head
        curr=head
        tail=head
        while(tail.next!=None):#mark the last node as tail
            tail=tail.next
        #swap first and last elements
        self.swap(curr,tail)
        curr=curr.next

        def helper(curr,tail):
            #base case
            if(curr.next==tail or curr==tail):
                return head
            else:
                intermediate=curr
                while(intermediate.next!=tail):
                    intermediate=intermediate.next
                
                self.swap(curr,intermediate)
                return helper(curr.next,intermediate)
        return helper(curr,tail)
#-------------approach 2----------------------
#reversing the list by changing the direction of arrows
#eg:1->2->3->4-> has to be converted to
#   <-1<-2<-3<-4 
#time complexity:O(n)
#space complexity:O(1)
class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        curr=head
        prev=None
        while curr:
            ptr=curr
            ptr.next=prev
            prev=ptr
            curr=curr.next
        return prev

head=ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
object=Solution()
print(object.reverseList(head))
                


        


