class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class MyLinkedList(object):

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=-1 #since sll is 0 indexed

        

    def get(self, index):
        if index>self.size or index<0:
            return -1
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr.data 
    
        
        

    def addAtHead(self, val):
        new_node=Node(val)
        self.size+=1
        if self.head==None:#list empty
            self.head=new_node
            self.tail=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            
            
        
        

    def addAtTail(self, val):
        self.size+=1
        new_node=Node(val)
        if self.head==self.tail==None:#list empty
            self.head=new_node
            self.tail=self.head
            
        else:
            self.tail.next=new_node
            self.tail=new_node

    def addAtIndex(self, index, val):
        if index==0:
            self.addAtHead(val)
        elif index==self.size+1:#addition at tail
            self.addAtTail(val)
        elif index<=self.size:
            new_node=Node(val)
            curr=self.head
            count=0#starting from first node , hence count 0 i.e index based
            while(curr!=None and count<index-1):
                curr=curr.next
                count+=1
            new_node.next=curr.next
            curr.next=new_node
            self.size+=1
        else:
            return -1

        

    def deleteAtIndex(self, index):
        if index<=self.size:
            if index==0:#delete head
                curr=self.head
                self.head=curr.next
                curr.next=None
                self.size-=1
                if(self.size==-1):
                    self.head=self.Tail=None

            elif index==self.size:#delete tail
                curr=self.head
                prev=None
                while curr.next!=None:
                    prev=curr
                    curr=curr.next
                prev.next=None
                self.tail=prev
                self.size-=1
            else:
                curr=self.head
                count=0
                while(count<index):
                    prev=curr
                    curr=curr.next
                    count+=1
                prev.next=curr.next
                curr.next=None
                self.size-=1

        return -1



        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)

obj.addAtIndex(3,0)
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
print(obj.get(4))
obj.addAtHead(4)
obj.addAtIndex(5,0)
obj.addAtHead(6)

# print(obj.get(1))
# obj.addAtTail(3)
# obj.deleteAtIndex(1)
# print(obj.get(1))
