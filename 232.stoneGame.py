from typing import List
from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #minimax dp
        #optimal play at each turn
        #check all possibilities
        #but return the max stones u can get from all the turns

        @lur_cache(none)
        def helper(l,r):
            if l==r:
                return piles[r]
            if l>r:
                return 0
            
            pickFirstPile=piles[l]-helper(l+1,r)
            pickLastPile=piles[r]-helper(l,r-1)

            #im returning the max stones i can get
            return max(pickFirstPile,pickLastPile)

        ans=helper(0,len(piles)-1)
        total=sum(piles)
        aliceScore=(total+ans)//2
        return True if aliceScore>total//2 else False
        