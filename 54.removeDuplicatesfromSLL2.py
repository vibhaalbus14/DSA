# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#head=ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4,ListNode(4,ListNode(5)))))))
head=ListNode(1,ListNode(1))

class Solution(object):
    def deleteDuplicates(self, head):
        if head==None or head.next==None:
            return head
        
        prev=head
        curr=head.next
        repeatedValue=None

        while curr!=None:
            if prev.val==curr.val:
                repeatedValue=prev.val#accept the first instance of unique nodes and store its value
                prev.next=curr.next
                
            else:
                if prev.val==repeatedValue:#remove the repeated node and set new head
                    #check if its beginning
                    if prev==head:
                        prev=prev.next
                        head=prev
                    else:
                            #to remove duplicates in the middle
                            #trav to node previous to prev from head
                            ptr=head
                            while ptr.next!=prev:
                                ptr=ptr.next
                            ptr.next=prev.next
                            prev=prev.next
                                    
                else:
                    prev=curr
            curr=curr.next 
         #to remove duplicates in the end node
        if prev.val==repeatedValue:
            #to remove duplicates in the end node
            #trav to node previous to prev from head
            if prev!=head:
                ptr=head
                while ptr.next!=prev:
                    ptr=ptr.next
                ptr.next=None
            else:
                head=None

        return head
    
    def traverse( self,head):
        if head==None:
            print("list empty")
        else:
            curr=head
            while curr!=None:
                print(f"{curr.val} ->",end=" ")
                curr=curr.next
            print()
object=Solution()
print(object.traverse(object.deleteDuplicates(head)))


#1 1 1 2 2 3
#1 2 2 3 3
#1 2 3 3 4 4 5