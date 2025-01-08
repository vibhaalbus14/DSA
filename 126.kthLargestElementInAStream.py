import heapq
class KthLargest(object):
    #the kth largest element in an array = smallest element in an array of size k having k large numbers
    #since heap automatically stores the smallest element at root, it can be accessed at O(1)
    #addition and removal is O(logn) complexity
    #hence min heap of size k is used,

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.heap=[]
        #this ensures only the top k largest elments out of nums are present in heap
        #by default, the first element is the smallest of all large numbers or is kth largest of all large 
        #nums heap
        for num in nums:
            if len(self.heap)<self.k:
                heapq.heappush(self.heap,num)
            else:
                #everytime a new element is added,if the new element is larger than the prev  smallest
                # it stays, else becomes the smallest and is popped out
                heapq.heappushpop(self.heap,num)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        #elif val>self.heap[0]:
            #heapq.heapreplace(self.heap,val)
        else:
            heapq.heappushpop(self.heap,val)
            
            #only if the value is greater than the smallest,it can contribute to change in largest numbers,
            #else, makes no sense in adding
            #also, heapq.pushpop(heap,val) can be done
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)