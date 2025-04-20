from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #approach
        #sliding window
        #exactly(k)= greater/equal(k) - greater/equal(k+1)

        def trace(threshold):
            hashMap=defaultdict(int)
            l=0
            count=0
            for r in range(len(nums)):
                hashMap[nums[r]]+=1

                while len(hashMap.keys())>=threshold:
                    count+=(len(nums)-r)
                    if hashMap[nums[l]]==1:
                        del hashMap[nums[l]]
                    else:
                        hashMap[nums[l]]-=1
                    l+=1
                   
            return count
        
        return trace(k)-trace(k+1)
        