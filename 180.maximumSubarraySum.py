from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSumMax=0
        globalMax=nums[0]

        for num in nums:
            currSumMax+=num
            currSumMax=max(currSumMax,num)
            globalMax=max(currSumMax,globalMax)
        return globalMax