from functools import cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # minimax dp
        # optimal play at each turn
        # check all possibilities
        # but return the max stones you can get from all the turns

        @cache
        def helper(l, m):
            if l >= len(piles):
                return 0
            currPiles = 0
            maxStones = float("-inf")
            for i in range(1, min(2 * m, len(piles) - l) + 1):
                currPiles += piles[l + i - 1]
                maxStones = max(maxStones, currPiles - helper(l + i, max(m, i)))
            return maxStones

        # The answer is half of the total sum of the piles,
        # since the optimal play ensures we maximize our score.
        total = sum(piles)
        ans = helper(0, 1)
        return (total+ ans)//2
