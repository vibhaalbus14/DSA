class MaxBinaryHeap:
    def __init__(self):
        self.heap = []
 
    def buildHeap(self, array):
        noOfNodes=len(array)
        #elements must follow heap property
        #start from lower internal nodes as to change a given index, its subtrees must follow heap property
        #leaf nodes always follow heap property since they have null children
        internalNodes=(noOfNodes//2)-1 #indices
        #pass all the nodes from last internal node to root to heapify
        for index in range(internalNodes,-1,-1):
            self.bubbleDown(array,index)
        self.heap=array
        return self
    
    def bubbleDown(self,array,index):#swap the parent node with max of its children
            #base case
            if  index in range(len(array)//2,len(array)):#if its a leafnode
                return
            leftChildIndex=(2*index)+1
            rightChildIndex=(2*index)+2
            if leftChildIndex<len(array) and rightChildIndex<len(array):#both left and right child exists
                if array[index]<max(array[leftChildIndex],array[rightChildIndex]):#have to swap
                    if array[leftChildIndex]>array[rightChildIndex]:
                        array[index],array[leftChildIndex]=array[leftChildIndex],array[index]
                        self.bubbleDown(array,leftChildIndex)
                    else:
                        array[index],array[rightChildIndex]=array[rightChildIndex],array[index]
                        self.bubbleDown(array,rightChildIndex)

            else:
                if leftChildIndex <len(array):#only left child exists as right child  cant exist without left
                #complete binary tree
                    if array[index]<array[leftChildIndex]:
                        array[index],array[leftChildIndex]=array[leftChildIndex],array[index]
                        self.bubbleDown(array,leftChildIndex)
            
        
    def remove(self):
        #remove the first element from array
        #make the last element the first element
        # pass this index to bubble down

        #check if the heap is empty before accessing top value
        if not self.heap:
            return None
        
        if len(self.heap)==1: #only one ele
            return self.heap.pop()
        
        maxValue=self.heap[0]
        lastVal=self.heap.pop()
        self.heap[0]=lastVal
        self.bubbleDown(self.heap,0) 
        return maxValue
            
        
    
    def insert(self,val):
        #insert the value at the end of heap
        #compare this child to its parent
        #the child propgates up to satisfy heap property
        #hence it calls bubbleUp function
        self.heap.append(val)
        self.bubbleUp(len(self.heap)-1)#pass the index of newly added element
        return self

    def bubbleUp(self,index):
        if index<=0:
            return
        childIndex=index
        parentIndex=(index-1)//2
        if self.heap[parentIndex]<self.heap[childIndex]:
            self.heap[parentIndex],self.heap[childIndex]=self.heap[childIndex],self.heap[parentIndex]
            self.bubbleUp(parentIndex)
        

    def peek(self):
        return self.heap[0]
        

        