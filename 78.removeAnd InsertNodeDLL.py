class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

def linkNodes(node1,node2):
    node1.next = node2
    node2.prev = node1

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node):
        if head:
            return "list empty"
        curr=head
        while(curr):
            if curr==node:
                if curr.prev==None and curr.next:#first node
                    head=curr.next
                    head.prev=None
                elif curr.prev and curr.next: #intermediate node
                    curr.prev.next=curr.next
                    curr.next.prev=curr.prev
                    
                elif curr.prev and curr.next==None:#last node
                    tail=curr.prev
                    tail.next=None
                else:#only one node where both prev and next are none
                    head=None
                curr.next=None
                curr.prev=None
            else:
                curr=curr.next

    def insertB(self, nodePosition, nodeInsert):
        #to remove the node if it already exists
        curr=head
        while(curr):
            if curr==nodeInsert:
                self.remove(nodeInsert)
                break
        count=0
        if head:#DLL already exists
            curr=head
            #at first nodePosition
            while curr:
                count+=1
                if nodePosition==count:
                    if curr.prev==None:#first place=>head
                        nodeInsert.next=head
                        head.prev=nodeInsert
                        head=nodeInsert
                        break
                    else:
                        if curr.next and curr.prev:#in bw
                            curr.prev.next=nodeInsert
                            nodeInsert.prev=curr.prev
                            curr.prev=nodeInsert
                            nodeInsert.next=curr
                            break
                curr=curr.next
            if nodePosition==count+1:#last position
                tail.next=nodeInsert
                nodeInsert.prev=tail
                tail=nodeInsert     
        else:
            head=nodeInsert


                


