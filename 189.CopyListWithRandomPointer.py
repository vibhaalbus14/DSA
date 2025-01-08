from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #approach
        #1.in the original LL , traverse through the nodes, mark the hashmap [node_address:index]
        #2.make a new LL , and mark all the new nodes in hashmap as [index:node_address]
        #3.traverse the original list again , this time focus on random pointer
        #4.map both the hashmap using a new hashmap
        #5.curr.random=node_address 
        #6.hashmap1[node_address]=index
        #7. in new hashmap2[source index: dest index]
        #8.use third hashmap3, node.random=hashMap3[hashMap2[source index]]
        #9.return start
        if not head:
            return head

        hashMapAddressToIndex={}
        hashMapIndexToIndex={}
        hashMapIndexToAddress={}
        curr=head
        start =None
        i=0 #to keep tract of node indices
        while curr:
            #make a new copy of ll
            if start==None:
                new_node=Node(curr.val)
                start=new_node
            else:
                newCurr=start
                while newCurr.next:
                    newCurr=newCurr.next
                new_node=Node(curr.val)
                newCurr.next=new_node
            hashMapAddressToIndex[curr]=i
            hashMapIndexToAddress[i]=new_node
            curr=curr.next
            i+=1
        #null node
        hashMapAddressToIndex[None]=i
        hashMapIndexToAddress[i]=None
        
        #traversal completed
        #just identify random poinnters value now
        i=0
        curr=head
        while curr:
            hashMapIndexToIndex[i]=hashMapAddressToIndex[curr.random]
            i+=1
            curr=curr.next
        hashMapIndexToIndex[i]=hashMapAddressToIndex[None]

        curr=start
        i=0
        while curr:
            if hashMapIndexToAddress[hashMapIndexToIndex[i]]:
                curr.random=hashMapIndexToAddress[hashMapIndexToIndex[i]]
            curr=curr.next
            i+=1
        
        return start
                