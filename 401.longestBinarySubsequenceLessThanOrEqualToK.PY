class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        #dp will give mle for strLength or when 3 params are passed
        #greedy approach
        #minimumLength = just by counting all zeroes

        n=len(s)
        currStr=''
        currBits=0

        #go from right to left , start by filling out lsb
        for i in range(n-1,-1,-1):
            if int(s[i]+currStr,2)<=k:#choose the curr bit only if value is less than k
                currStr=s[i]+currStr
                currBits+=1
        
        return currBits
            

        