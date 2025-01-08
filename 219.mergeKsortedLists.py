from typing import List,Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        listOfNodes=[]

        def addNodes(head):
            if not head:
                return
            curr=head
            while curr:
                listOfNodes.append((curr,curr.val)) #node add, node val
                curr=curr.next

        for ll in lists:
            if ll: #since lists can be [None]
                addNodes(ll)

        if not listOfNodes:
            return

        #sort the nodes in list acc to node values
        listOfNodes.sort(key=lambda x:x[1])
        dummy=ListNode()
        dummy.next=listOfNodes[0][0]
        #make all the nodes point to each other
        for i in range(len(listOfNodes)-1):#except the last one
            currNode=listOfNodes[i][0]
            nextNode=listOfNodes[i+1][0]
            currNode.next=nextNode
        listOfNodes[-1][0].next=None

        return dummy.next

