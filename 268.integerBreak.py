from functools import lru_cache
class Solution:
    def integerBreak(self, n: int) -> int:
        
        @lru_cache    
        def helper(num,digits):

            maxProd=1
            if num==0 or num==1:
                return 1 #cause multiplication

            for i in range(1,num):
                #print(i,num)
                maxProd=max(maxProd,helper(num-i,digits+1)*i)
                if digits>=2:
                    maxProd=max(maxProd,num)
            return maxProd

        return helper(n,1)
#------------------------------approach2---------------------------------------------

class Solution:
    def integerBreak(self, n: int) -> int:

        if n==2 or n==3:
            return n-1 
        @lru_cache    
        def helper(num):

            maxProd=1
            if num==0 or num==1:
                return 1 #cause multiplication

            for i in range(1,num+1):
                #print(i,num)
                maxProd=max(maxProd,helper(num-i)*i)
            return maxProd

        return helper(n)
