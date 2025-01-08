#time comp=O(n)=>iterate over the nums array, heappush and heappop is logn
#space comp=O(n)=> dict stores all n unique elements
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #approach
        #1.loop through nums and create a hash map (key,val)=(key,freq)
        #2.create a max priority queue and append the (val,key) pairs 
        #here, since tuple is beig appended, heapq will consider first to be priority and then value
        #in case the priorities are same, it will consider the val
        #3.pop k elments from hashmap and print its val
        maxHeap=[]
        hashMap={}
        array=[]
        for num in nums:
            if num in hashMap:
                hashMap[num]+=1
            else:
                hashMap[num]=1
        
        
        pairs=[pair for pair in hashMap.items()]
        
        for tup in pairs: #(key,val)
            heapq.heappush(maxHeap,(-tup[1],-tup[0]))#(val,key) and negative since its a max heap

        count=0
        while count<k:
            tup=heapq.heappop(maxHeap)
            array.append(-tup[1])
            count+=1
        return array