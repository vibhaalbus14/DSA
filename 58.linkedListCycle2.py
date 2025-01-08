# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# Time complexity=O(n)
# Space complexity=O(n)
class Solution(object):
    def detectCycle(self, head):
        start=head#to note the position of loop head
        if head==None or head.next==None:
             return None
        curr=head
        end=None
        position=-1
        ptrList=[None]*(10**4)
        i=0
        while i<len(ptrList) and curr.next  not in ptrList:
                ptrList[i]=curr
                curr=curr.next
                if(curr==None):#no loop
                    return None
                i+=1
        end=curr #check if only the end node points to the start
        return end.next
    
        #------------to get the position---------------
        # while(start!=end):#since end can point to itself
        #      position+=1 #starting from first node
        #      if end.next==start:
        #         return position
        #         break
        #      start=start.next
        # position+=1
        # return position
        
        #------------to return node at position----------------------
        # count=0
        # curr=head
        # while(count!=position):
        #     curr=curr.next
        #     count+=1
        # return curr.val

        
# Time complexity=O(n)
# Space complexity=O(n)
class Solution(object):
    def detectCycle(self, head):
     if head is None or head.next is None:
          return None
     curr=head
     ht={} #node-position pair in ht
     i=0
     while curr:
          if curr not in ht:
               ht[curr]=i
               i+=1
               curr=curr.next
     return curr

# Time complexity=O(n)
# Space complexity=O(1)
class Solution(object):
    def detectCycle(self, head):
         #fast -slow pointer approach
         if head is None or head.next is None:
              return None
         fast=head #moves by two steps
         slow=head #moves by one step

         while fast and fast.next:
              fast=fast.next.next
              slow=slow.next
              if fast==slow: # both met=> cycle exists
                   break
         if fast!=slow: # cycle does not exist
              return None
         #to identify loop start

         ptr=head
         while(ptr!=slow):
              ptr=ptr.next
              slow=slow.next
         return ptr

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6)
 
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
# make a loop
six.next = three
 
head = one
 
object=Solution()
print(object.detectCycle(head))
        