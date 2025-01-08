from typing import List
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        #memo={}
        res=False

        @lru_cache
        def helper(index):
            nonlocal n,res
            #base case
            if index>=n:
                return True

            currFlag=False
            for j in range(index,n):
                if s[index:j+1] in wordDict:
                    currFlag=True
                    res=res or (helper(j+1) and currFlag)
            if not currFlag:
                res=False

            # memo[index]=res
            # return memo[index]
            return res
#catsandog
        return helper(0)
                