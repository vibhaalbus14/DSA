from collections import lru_cache
class Solution:
    def punishmentNumber(self, n: int) -> int:

        def dp(s,num):
            m=len(s)
            @lru_cache
            def helper(index,currSum):
                if index==m and currSum==num:
                    return True
                if currSum>num or index>=m:
                    return False
                
                for j in range(index+1,m+1):
                    if int(s[index:j])+currSum<=num:
                        if  helper(j,currSum+int(s[index:j])):
                            return True
                    else:
                        break #because the value only increases further
                return False
            return helper(0,0)
        
        punishmentNum=0
        for i in range(1,n+1):
            square=i*i
            if dp(str(square),i):
                punishmentNum+=square
        return punishmentNum


        