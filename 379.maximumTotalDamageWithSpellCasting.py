from collections import Counter
from typing import List
from functools import lru_cache
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        unique = sorted(count)
        damage = [val * count[val] for val in unique]#contribution of every unique val
        n = len(unique)

        @lru_cache(None)
        def helper(i):
            if i >= n:
                return 0

            # Skip current
            skip = helper(i + 1)

            # Take current and jump to first index j where unique[j] > unique[i] + 2
            
            j=i+1
            while j<n and unique[j]<=unique[i]+2:
                j+=1
            take=helper(j)+damage[i]
            return max(skip, take)

        return helper(0)
