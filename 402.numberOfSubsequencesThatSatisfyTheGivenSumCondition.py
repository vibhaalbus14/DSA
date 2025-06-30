from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        #approach
        #we are counting the subsequences such that lth element must always be there, and max element cannot exceed the rth
        #=> 2**(r-l) will give all the subsequences starting from i , till j
        n=len(nums)
        nums.sort()
        MOD=10**9+7

        count=0

        l,r=0,n-1

        while l<=r:
            if nums[l]+nums[r]<=target:
                count+=pow(2,(r-l),MOD)
                count%=MOD
                l+=1
            else:
                r-=1
        return count
        