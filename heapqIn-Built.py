import heapq
#a python module used to implement min priority queue
#heap=[]
#it offers the foll. funtions
#1.heapq.heappush(heap,value)
#  =>it pushes a value and automatically performs bubble up to ensure the min val is  always at the root
#2.heapq.heappop(heap)
#  =>it ensures that root element is popped and replaces the last element at root , performs bubble down
#3.heap[0]=> peeks the root element

heap=[]
heapq.heappush(heap,8)
print(heap)
heapq.heappush(heap,3)
print(heap)
heapq.heappush(heap,1)
print(heap)
heapq.heappush(heap,-2)
print(heap)

heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
print(heap[0])

#round func
#syntax= round(number,decimal places) . if no decimal places, then its considered by default as zero
a=15.67890
print(round(a,3))
print(round(a))