# spaces=0
# for i in range(5,0,-2):
#     op=" "*(spaces//2)+"*"*i+" "*(spaces//2)
#     spaces+=2
#     print(op)

# arr1=[]
# arr1.extend([])
# print(arr1)

#lowest priority=> processed first
import heapq
minHeap=[]
minHeap.append((1,10))#(priority,ele)
minHeap.append((2,20))
minHeap.append((3,30))
heapq.heapify(minHeap)
while minHeap:
    print("MINHEAP")
    prior,ele=heapq.heappop(minHeap)
    print(f" prior {prior} , ele val {ele} ")

maxHeap=[]
maxHeap.append((-1,10))#(priority,ele)
maxHeap.append((-2,20))
maxHeap.append((-3,30))
heapq.heapify(maxHeap)
while maxHeap:
    print("MAXHEAP")
    prior,ele=heapq.heappop(maxHeap)
    print(f" prior {prior} , ele val {ele} ")

    
    