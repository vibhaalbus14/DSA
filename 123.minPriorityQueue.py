#more importance to lower priority
#lower priority nodes are at the top
#in min binary heap, the elements are singular values  and are sorted acc to the values
#in min priority queue, the elements are nodes that are made up of values and priority. comparision
#is done on priority than values, this is the difference
#the same goes for max heap(acc. to values,max value at top/root) and max priority queue (acc. to priority
#max priority node at top/root)
class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
 
class PriorityQueue:
    def __init__(self):
        self.data = []#priority queue array here #the collection of nodes as list/array

    #to add nodes to 
    def enqueue(self,value,priority):
        newNode=Node(value,priority)
        self.data.append(newNode)#new child
        #identify the coorect position of the node based on its priority
        #call bubbleUp
        self.bubbleUp(len(self.data)-1)
        return self
    
    def bubbleUp(self,index):
        if len(self.data)==1:
            return
        if index<=0:
            return
        childIndex=index
        parentIndex=(index-1)//2

        childNode=self.data[childIndex]
        parentNode=self.data[parentIndex]
        #compare the priorities
        if childNode.priority<parentNode.priority:
            #swap node positions
            self.data[childIndex],self.data[parentIndex]=parentNode,childNode
            #propogate the child upwards
            self.bubbleUp(parentIndex)        

    
    def dequeue(self):
        if self.data==[]:
            return None
        elif len(self.data)==1:#only one element,pop it out,list becomes empty
            rootNode=self.data.pop()
            return rootNode
        rootNode=self.data[0]
        #there exists another element
        #swap the root value with last element
        lastVal=self.data.pop()
        self.data[0]=lastVal
        #check if the priority criteria is followed
        #compare parent with children
        #call bubbleDown
        self.bubbleDown(0)
        return rootNode

    def bubbleDown(self,index):
        if index in range(len(self.data)//2,len(self.data)): #if the index is in leaf nodes's index range, all set
            return
        parentIndex=index
        leftChildIndex =(2*index)+1
        rightChildIndex=(2*index)+2
        parentNode=self.data[parentIndex]
        

        if leftChildIndex<len(self.data) and rightChildIndex<len(self.data):#both the child exists
            leftChildNode=self.data[leftChildIndex]
            rightChildNode=self.data[rightChildIndex]

            if parentNode.priority>min(leftChildNode.priority,rightChildNode.priority):
                #swap with the minimum
                if leftChildNode.priority<rightChildNode.priority:
                    self.data[parentIndex],self.data[leftChildIndex]=leftChildNode,parentNode
                    self.bubbleDown(leftChildIndex)
                else:
                    self.data[parentIndex],self.data[rightChildIndex]=rightChildNode,parentNode
                    self.bubbleDown(rightChildIndex)
        else:
            if leftChildIndex<len(self.data):#only left child
                leftChildNode=self.data[leftChildIndex]
                
                if parentNode.priority>leftChildNode.priority:
                    self.data[parentIndex],self.data[leftChildIndex]=leftChildNode,parentNode
                    self.bubbleDown(leftChildIndex)

    def peek(self):
        return self.data[0]