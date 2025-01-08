#time comp: O(n*2^n)=O(n^2)(dp)+O(n*2^n)
#space comp: O(n + n^2 + 2^n)(rec call stack + dp +intermediate storage)
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #approach
        #1.identify all possible partitions=> backtracking
        #2.but partions can be included only if they are palindromic
        #3.so, first construct a dp table of the given string and identify the palindrmic substrings
        #using length-wise strategy
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
        #--------------------------backtracking-------------------------------
        res=[]
        def partition(index,subList):
            nonlocal n,res
            if index>n-1: #reached the end of string, add subList to res
                res.append(subList[:])
                return
            #loop from index to end of string
            for j in range (index,n):
                #check if this partition is  a palindrome from dp table
                if dp[index][j]==1:
                    subList.append(s[index:j+1])
                    partition(j+1,subList)
                    subList.pop()
        partition(0,[])
        return res    


