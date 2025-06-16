from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        maxVal=-1
        currMax=nums[-1]

        #why from right to left?
        #beacuse nums[j]>nums[i] and i<j
        #this will help us to get max value and eliminate
        #as well consider thos i values that are less than max
        for i in range(n-2,-1,-1):
            if nums[i]<currMax:
                maxVal=max(maxVal,currMax-nums[i])
            else:
                #set the new max cause we need max to be high to have max diff
                currMax=nums[i]
        return maxVal
        