from typing import List
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        #sliding window tech
        l=0
        r=0
        curr=0
        maxCount=1
        
        while l<=r and r<len(nums):
            #reduce the window size till they are not equal
            while l<=r and (nums[r] & curr)!=0:
                curr ^=nums[l]#remove the overalappig pairs
                l+=1
            
            if  curr & nums[r]==0:
                maxCount=max(maxCount,r-l+1)
                curr= curr | nums[r] #take only overlapping pairs forward
                r+=1
                
        return maxCount
            
        