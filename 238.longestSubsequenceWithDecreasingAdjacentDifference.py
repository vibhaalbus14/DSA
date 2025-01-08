from functools import lru_cache
from typing import List
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(index,prevIndex,diff):
            if index>=len(nums):
                return 0 #returning count
            exclude=helper(index+1,prevIndex,diff)
            include=0
            if prevIndex ==-1:
                if nums[index]<=diff:
                    include=helper(index+1,index,diff)+1
            elif abs(nums[index]-nums[prevIndex])<=diff:
                include=helper(index+1,index,abs(nums[index]-nums[prevIndex]))+1
            return max(exclude,include)
        
        return helper(0,-1,float("inf"))
        


        