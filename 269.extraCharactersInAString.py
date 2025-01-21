from typing import List
from functools import lru_cache

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        #approach
        #dp
        #1. assume that substring starts from curr index cahr
        #2.identify a valid substring now, once it is doone, send the other half to check
        #3.assume that curr index does not involve in forming substring, make it unsused

        dictionary=set(dictionary)
        n=len(s)

        @lru_cache
        def helper(i):
            if i>=n:
                #ened of string, no chars present
                return 0

            skipCurrChar=helper(i+1)+1
            #consider the curr char as unused

            #consider the curr char
            #identify a substring that is valid

            noSkipCurrChar=float("inf")
            for j in range(i,n):
                if s[i:j+1] in dictionary:
                    #it is valid
                    #if this valid string is considered, then what about the rest of unprocessed string
                    noSkipCurrChar=min(noSkipCurrChar,helper(j+1))
            return min(skipCurrChar,noSkipCurrChar)

        return helper(0)

        