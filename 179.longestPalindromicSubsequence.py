#------------------approach: memoization-------------------------
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #memoization approach
        memo={}

        def helper(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==j:
                return 1 #one letter matches
            if i>j:
                return 0
            middlePart=0
            if s[i]==s[j] : #no middle part
                middlePart=helper(i+1,j-1)+2 #2 letters are included
            rightSubstring=helper(i+1,j)
            leftSubstring=helper(i,j-1)

            memo[(i,j)]=max(middlePart,rightSubstring,leftSubstring)
            return memo[(i,j)]
        
        return helper(0,len(s)-1)

#------------------approach:tabulation----------------------
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        if n==1:
            return n

        dp=[[-1]*n for _ in range(n)]

        #string of length 1 is a plaindromic subsequence
        for i in range(n):
            dp[i][i]=1
        
        maxLength=1
        subsequence=""

        for length in range(2,n+1):
            for i in range(n-length+1):
                j=i+length-1

                if s[i]==s[j]:
                    if i+1==j:
                        dp[i][j]=2
                    else:
                        dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        
        return dp[0][n-1]