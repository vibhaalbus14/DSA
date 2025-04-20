from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        if k>sum(candies):
            return 0 #insufficient piles
        
        def allotCandies(start):
            children=0
            for candy in candies:
                children+=candy//start
            
            if children>=k:
                return True
            else:
                return False
            
        #binary search from 1 to max(candies)

        l=1
        r=max(candies)

        while l<=r:
            mid=(l+r)//2
            if allotCandies(mid):
                l=mid+1
            else:
                r=mid-1
        return l-1
            