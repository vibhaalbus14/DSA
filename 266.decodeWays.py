from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        #partioning and bactracking
        #but no need to return the list divisions
        #=>dp partitioning
        hashMap={}
        alphabets="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alphabets)):
            hashMap[str(i+1)]=alphabets[i]

        
        @lru_cache(None)
        def helper(i):
            total=0
            if i>=len(s):
                return 1
            for j in range(i,len(s)):
                #check if its a valid partition
                if s[i:j+1] in hashMap:
                    total+=helper(j+1)
            return total
                    
               
        return helper(0)
        
        