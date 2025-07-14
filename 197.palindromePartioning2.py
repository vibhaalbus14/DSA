'''whats the diff palindrome partition 1 & 2?
in 1, we were asked to list all possible partitions, hence bactracking was used
in 2, we were asked to identify min cuts, keeping track of partitions wasnt necessary,so , dp
in both the approaches, the way partition is generated is same move the indices, identify first valid 
palindrome partition and then recursion, but the difference lies in "do we need to store the partitions
or not"
'''
class Solution:
    def minCut(self, s: str) -> int:
        
        #approach
        #1.identify first valid palindromic partition, and then rec call
        #2. first construct a dp table of the given string and identify the palindrmic substrings
        #using length-wise strategy
        #3.keep track of minimum cuts in memo
        n=len(s)
        #dp length-wise strategy
        dp=[[0 for i in range(n)]for _ in range (n)]
        
        #loop through diagonally
        for L in range(1,n+1):
            for i in range(n-L+1):
                j=i+L-1
                if i==j:#length 1 substring
                    dp[i][j]=True
                elif s[i]==s[j] and (i+1==j or dp[i+1][j-1]):#outer letters match,no middle part
                    dp[i][j]=True
                else:
                    dp[i][j]=False
        #--------------------------dp-------------------------------
        # def checkPalindrome(i,j):
        #     nonlocal s
        #     l,r=i,j
        #     while l<=r:
        #         if s[l]!=s[r]:
        #             return False
        #         l+=1
        #         r-=1
        #     return True
        
        minVal=float("inf")
        memo={}
        def partition(index):
            nonlocal memo,minVal
            if index in memo:
                return memo[index]
            #make cuts such that the resultant strung on lhs is a plaindrome
            if index>=n:
                return 0
            for j in range(index,n):
                if dp[index][j]: #is a valid cut
                    minVal= min(minVal,partition(j+1)+1)#+1 because valid palindrome is already added
            memo[index]=minVal
            return memo[index]


        return partition(0)-1
          

obj=Solution()
print(obj.minCut("aab"))