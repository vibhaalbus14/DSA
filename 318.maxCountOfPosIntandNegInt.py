from typing import List
from bisect import bisect_left,bisect_right
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        neg_end=bisect_left(nums,0) #first insertion of 0 pos
        pos_start=len(nums)-bisect_right(nums,0) #last insertion of 0 pos
        #if no 0 => len(nums)
        return max(neg_end,pos_start)