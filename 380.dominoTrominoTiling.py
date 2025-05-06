class Solution:
    def numTilings(self, n: int) -> int:
        #pattern question
        
        if n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 5

        pattern=[0]*(n+1)
        pattern[1]=1
        pattern[2]=2
        pattern[3]=5

        MOD= 10**9+7
        
        for i in range(4,n+1):
            pattern[i]=(pattern[i-1]*2 +pattern[i-3])%MOD
        
        return pattern[n]