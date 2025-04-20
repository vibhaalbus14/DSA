from collections import Counter
from typing import List
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        #approach
        #1.brute force
        #2.use hashMap for O(1) lookup
        hashMap=Counter(nums)
        nums.sort()
        totalSum=sum(nums)
        #maxOutlier=float("-inf")
    
        for i in range(len(nums)-1,-1,-1):
            outlier=nums[i]
            hashMap[outlier]-=1
            remSum=totalSum-outlier

            #check existence of sumNum of special Nums
            if remSum%2==0 and hashMap[remSum//2]!=0:
                #maxOutlier=max(maxOutlier,nums[i]) 
                return outlier
            hashMap[outlier]+=1

        #return maxOutlier