#--------------------------approach:memoization---------------
#time comp=O(n**2)
#space comp=O(n**2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp ={}

        def helper(i,j):
            nonlocal dp
            if i>j:
                return 0

            if (i,j) in dp:
                return dp[(i,j)]  

            if i==j:#its a palindrome, so mark in hashmap
                dp[(i,j)]=1
                return dp[(i,j)]
 
            helper(i+1,j) #calling right substring
            helper(i,j-1)  #calling left substring

            #checking if current substring from i to j i.e s[i:j+1] is a palindrome
            if s[i]==s[j] and (j==i+1 or helper(i+1,j-1)):#if two corners match 
                #and if theres no middle part or if the middle part is palindrome make it 1
                #eg: "aa" has no middle part so i=0,j=1 and i+1=j says theres no middle part
                #eg: "abea" middle part is "be" which is obtained from i+1,j-1
                dp[(i,j)] = 1
            else:
                #if the last doesnt match or middle part isnt a palindrome,make it 0
                dp[(i,j)] = 0   
                #return to whoever called
            return dp[(i,j)]     
        helper(0,n-1)
        return sum(dp.values())

#--------------------------approach:tabulation---------------
#time comp=O(n**2)
#space comp=O(n**2)
#less rec func call overhead=> better performance depite time and space comp being the same
class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[-1]*n for i in range(n)]
        count=0
        #length
        for length in range(1,n+1):
            for i in range(n-length+1):
                j=i+length-1

                if dp[i][j]!=-1:
                    if dp[i][j]==1:
                        count+=1

                elif i==j:
                    dp[i][j]=1
                    count+=1

                elif s[i]==s[j] and (i+1==j or dp[i+1][j-1]):#if middle part exists or if middle part is a palindrome
                    dp[i][j]=1
                    count+=1
                else:
                    dp[i][j]=0
        return count

