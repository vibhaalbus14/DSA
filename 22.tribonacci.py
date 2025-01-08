class Solution(object):
    def tribonacci(self, n):
        dp=[0,1,1]+[0]*35
        if(n==0 or n==1 or n==2):
            return dp[n]
        else:
            for i in range(2,len(dp)):
                dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]
obj=Solution()
print(obj.tribonacci(25))

dp=[0,1,1]+[0]*35
print(dp)