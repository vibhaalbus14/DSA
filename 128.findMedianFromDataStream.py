#----------------------approach 1-------------------------------
import heapq
class MedianFinder(object):

    def __init__(self):
        self.nums=[]
        self.length=0
        self.numCount="None"

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.maxHeap=[]
        self.minHeap=[]
        self.nums.append(num)
        self.length+=1
        
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        if self.length%2==0:
            elementsToBePopped=(self.length-2)//2
            self.numCount="even"
        else:
            self.numCount="odd"
            elementsToBePopped=self.length//2

        for num in self.nums:
            self.minHeap.append(num)
            self.maxHeap.append(-num)
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

        for count in range(1,elementsToBePopped+1):
            heapq.heappop(self.minHeap)
            heapq.heappop(self.maxHeap)

        if self.numCount=="even": 
            firstVal=heapq.heappop(self.minHeap)
            secondVal=-heapq.heappop(self.maxHeap)
            return float(firstVal+secondVal)/2
        else:
            return float(heapq.heappop(self.minHeap))
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#--------------------------------approach 2------------------------------------
#time comp:O(logn) as only heap push and pop are done
#space comp:O(n) => heap storage
import heapq
class MedianFinder(object):

    def __init__(self):
        self.minHeap=[]
        self.maxHeap=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #to the lower elements including first mid, max heap is used to get the middle most element
        #to the other half, min heap is used to get the next middle element

        #if even numbers,both min and max heaps have same length
        #in case of odd,since max heap or first half will include the first mid,its length is more by 1

        heapq.heappush(self.minHeap,-heapq.heappushpop(self.maxHeap,-num))

        if len(self.maxHeap)<len(self.minHeap): #this implies the first middle element is present on wrong side
        #push it from 2nd half to first half
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap)>len(self.minHeap): #odd
            return float(-self.maxHeap[0])
        else:
            return (-(self.maxHeap[0])+self.minHeap[0])/float(2)#even, take avg
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()