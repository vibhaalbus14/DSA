class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1:
            return s

        dp=[[-1]*n for _ in range(n)]

        #strings with length=1 are a palindrome and are found along diagonal
        for i in range(n):
            dp[i][i]=1

        maxLength=1
        start=0
        #length ranges from 1 to n
        for length in range(2,n+1):#since level 1 already calculated
            #i value ranges from 0 to n-length+1
            for i in range(n-length+1):
                #get the value of j
                j=i+length-1
                if s[i]==s[j] and (i+1==j or dp[i+1][j-1]):
                    dp[i][j]=1
                    length=j-i+1
                    if length>maxLength:
                        maxLength=length
                        start=i
                else:
                    dp[i][j]=0
        return s[start:maxLength+start]
'''
By filling the DP table for all smaller substrings before larger ones, 
we ensure that dp[i+1][j-1] is computed before dp[i][j]. So by the time we check 
value of dp[i+1][j-1] for a larger substring, it will have been correctly filled.'''