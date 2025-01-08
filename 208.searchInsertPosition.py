import bisect
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #return bisect.bisect_left(nums,target)
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=target:
                #search for the left side
                r=mid-1
            else:
                l=mid+1
        return l
