from typing import List
from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        @lru_cache
        def helper(i):
            if i>=len(stoneValue):
                return 0
            
            currVal=0
            maxVal=float("-inf")
            for x in range(i,i+3):
                if x<len(stoneValue):
                    currVal+=stoneValue[x]
                    maxVal=max(maxVal,currVal-helper(x+1))
            return maxVal
        
        scoreDifference=helper(0)
        total=sum(stoneValue)
        alice=(total+scoreDifference)//2
        bob=total-alice

        if alice>bob:
            return "Alice"
        if alice<bob:
            return "Bob"
        else:
            return "Tie"

