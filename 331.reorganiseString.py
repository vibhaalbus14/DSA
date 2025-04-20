import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        #approach
        #1.maintain a maxheap

        hashMap=Counter(s)
        res=""
        maxHeap=[]
        for key,freq in hashMap.items():
            maxHeap.append((-freq,key))

        heapq.heapify(maxHeap)
        
        while maxHeap:
            freq1,char1=heapq.heappop(maxHeap)
            freq1=-freq1

            if not res or char1!=res[-1]:
                res+=char1
                freq1-=1
                if freq1!=0:
                    heapq.heappush(maxHeap,(-freq1,char1))
            else:
                if not maxHeap:
                    return ""
                freq2,char2=heapq.heappop(maxHeap)
                freq2=-freq2
                res+=char2
                freq2-=1
                if freq2!=0:
                    heapq.heappush(maxHeap,(-freq2,char2))
                heapq.heappush(maxHeap,(-freq1,char1))
            
        return res
                


        