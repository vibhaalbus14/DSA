#time complexity=O(1) for enqueue and O(n) for dequeue as elements have to be shifted by index-1
#space comp for enqueue and dequeue operation=O(1)
queue=[]
#enqueue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
#dequeue
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)


#-----------------------------LL-------------------------
#time complexity=O(1)
#space comp for enqueue and dequeue operation=O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):#add to the end i.e last
        #addition from from front
        newNode=Node(value)
        self.size+=1
        if self.first==None:
            self.first=newNode
            self.last=newNode
        else:
            self.last.next=newNode
            self.last=newNode

    def dequeue(self):
        #removal from back/last
        if self.size==0:
            return None
        temp=self.first
        self.first=self.first.next
        self.size-=1
        if self.size==0:
            self.last=None
        return temp.value
            
