from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        #approach
        #1.sort the array
        #2.does i<j not matter?
        #no, because we need to find a pair, its obvious that when we pick 2 diff indices, one will be smaller than the other => this i<j simply implies the indices chosen to form the pair must be unique
        #3.do binary search for every num and identify the possible indices where
        #x>=lower-curr and x<=higher-curr and subtract these indices
        #4.for lower=> identify left most possibility
        #for higher=> identigy right most possibility

        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n):
            left = bisect_left(nums,lower-nums[i],lo=i+1)
            right = bisect_right(nums,upper-nums[i],lo=i+1)
            count += right-left
        
        return count
        
        
