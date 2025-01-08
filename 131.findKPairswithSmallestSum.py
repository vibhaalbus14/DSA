import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        #approach
        #1.find all combinations of list
        #2.create a minheap with priority as sum
        #3.pop elemnets with smallest sum, k times
        #4.return the finalList
        count=0
        minHeap=[]
        finalList=[]
        for i in nums1:
            for j in  nums2:
                heapq.heappush(minHeap,(i+j,[i,j]))#after one iteration,ure checking the heap to pop min sum
            sum,subList=heapq.heappop(minHeap)
            finalList.append(subList)
            count+=1
            if count==k:
                return finalList
#----------------------------approach2-------------------------------------------------------
#time comp:O(klogk)
#space comp:O(k)
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype:List[List[int]]
        
        """
        #approach:
        #1.add (sum,i,j) into minheap
        #2.add if the index com (i,j) is visited or not into visited set
        #3.why this approach?
        #4.since ,lowest sum is to be found out, chances are hight that the lower sumis found
        #at the beginning of both the arrays.So going through diff comb of nearby indices is imp
        #rather than starying away like 0,0 to 0,5 without checking 1,1
        #this also preserves unnecessary memory storage in heap and heao memory wont exceed
        #5.while k and heap, pop the lowest sum from heap
        #6.since it is the lowest, append the values from the indices popped
        #7.check for the nearby indices, add them to heap and visited

        visited=set()
        finalList=[]

        minHeap=[(nums1[0]+nums2[0],0,0)]# first value is taken as priority in heapq 0+0,since thats the
        #lowest sum possible from 2 sorted arrays
        visited.add((0,0))

        while k and minHeap:
            sum,i,j=heapq.heappop(minHeap)
            finalList.append([nums1[i],nums2[j]])

            #check its nearest neighbour pairs
            if i+1<len(nums1) and (i+1,j) not in visited:
                heapq.heappush(minHeap,(nums1[i+1]+nums2[j],i+1,j))
                visited.add((i+1,j))

            if j+1<len(nums2) and (i,j+1) not in visited:
                heapq.heappush(minHeap,(nums1[i]+nums2[j+1],i,j+1))
                visited.add((i,j+1))
            
            k-=1
        return finalList




