# #----------------------------recursion--------------------------------
# #space complexity=O(n+m) from max depth of rec tree
# #time complexity=0(2^(n+m))
# def longestCommonSubsequence(text1, text2):
#     #write code here
    
#     def helper(firstIndex,secondIndex):
#         nonlocal text1,text2
#         if(firstIndex==len(text1) or secondIndex==len(text2)):
#             return 0
#         else:
#             if(text1[firstIndex]==text2[secondIndex]):
#                 return 1+helper(firstIndex+1,secondIndex+1)
#             else:
#                 return max(helper(firstIndex+1,secondIndex),helper(firstIndex,secondIndex+1))
                
                
#     return helper(0,0)

# print(longestCommonSubsequence("pbcdq","pcq"))

#----------------------------memoization---------------------
#this dictionary will have values of lax common matches from that i,j
#space complexity=O(n+m) from max depth of rec tree + O(nxm) from has table==> O(nxm)
#time complexity=0(n*m)

def LongestCommonSubsequence(text1,text2):
    mem={}
    def helper(i,j):
        if(i==len(text1) or j==len(text2)):
            return 0
        else:
            if (i,j) in mem:
                return mem[(i,j)]
            else:
                if text1[i]==text1[j]:
                    mem[(i,j)]= 1+ helper(i+1,j+1)
                else:
                    mem[(i,j)]=max(helper(i+1,j),helper(i,j+1))
        return mem[(i,j)]
    return helper(0,0)
print(LongestCommonSubsequence("pbcdq","pcq"))

#----------------tabulation------------------------------
#space complexity:O(nxm)
#time complexity:O(nxm)
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len(text1)][len(text2)]
object=Solution()
print(object.longestCommonSubsequence("abcde","ace"))
