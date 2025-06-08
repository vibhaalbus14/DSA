import heapq
from collections import defaultdict
class Solution:
    def clearStars(self, s: str) -> str:
        #minHeap approach

        alpha="abcdefghijklmnopqrstuvwxyz"
        hashMap=defaultdict(int)
        for i,char in enumerate(alpha):
            hashMap[char]=i
        
        minHeap=[]
        for i,char in enumerate(s):
            if char=="*" and minHeap:
                heapq.heappop(minHeap)
            else:
                heapq.heappush(minHeap,(hashMap[char],-i,char)) #min ascii value, max index why? closest to * is max index

        res=[]
        minHeap.sort(key= lambda x: -x[1])
        
        for val,index,char in minHeap:
            res.append(char)

        return "".join(res)

        