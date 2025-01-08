from functools import lru_cache
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
      #approach
      #1.lcs of str1 and str2
      #2.since the op string must contain both str1 and str2,we'll loop through the lcs and fit the missing charc of str1 and str2 preserving the order
        memo={}
        def helper(i,j):
            nonlocal memo
            if (i,j) in memo:
                return memo[(i,j)]
            if i>=len(str1) or j>=len(str2):
                return ""
            if str1[i]==str2[j]  :
                memo[(i,j)]=str1[i]+helper(i+1,j+1)
            else:
                temp1=helper(i+1,j)
                temp2=helper(i,j+1)
                memo[(i,j)]=temp1 if len(temp1)>len(temp2) else temp2
            return memo[(i,j)]
        

        #-----------------------------------------------
        commonLCS=helper(0,0)

        if not commonLCS:
            return str1+str2
        
        # @lru_cache #memo[(i,j)]=scs string
        # def loopThroughAndAdd(strA,strB,i,j):
        #     if (i==len(strA) and j==len(strB)) or (i==len(strA)) :
        #         return  strB
        #     elif j==len(strB):
        #         strB=strB+strA[i:]
        #         return strB
        #     if strA[i]==strB[j]:
        #         return loopThroughAndAdd(strA,strB,i+1,j+1)
        #     else:
        #         #1.it is either, commonLCS does not have the letter
        #         #2.or ,common LCS has extra letter, so skip letter of strB here
        #         strBcase1=strB[:j]+strA[i]+strB[j:]
        #         temp1=loopThroughAndAdd(strA,strBcase1,i+1,j+1)
        #         temp2=loopThroughAndAdd(strA,strB,i,j+1)
        #         return temp1 if len(temp1)<len(temp2) else temp2
                 
        # print(commonLCS)
        # commonLCS=loopThroughAndAdd(str1,commonLCS,0,0)
        # print(commonLCS)
        # commonLCS=loopThroughAndAdd(str2,commonLCS,0,0)
        # return commonLCS


        #-------------------------------------------------------------------------------------
        res=[]
        i,j=0,0 #i => str1 , j=> str2 , k=>commonLcs
        for char in commonLCS:
            while i<len(str1) and str1[i]!=char:
                res.append(str1[i])
                i+=1
            i+=1 #cause now its same, we add it as char and inc i ptr

            while j<len(str2) and str2[j]!=char:
                res.append(str2[j])
                j+=1
            j+=1

            #if same
            res.append(char)

        #add remaining chars
        if i<len(str1):
            while i<len(str1):
                res.append(str1[i])
                i+=1
        if j<len(str2):
            while j<len(str2):
                res.append(str2[j])
                j+=1
        return "".join(res)
obj=Solution()
print(obj.shortestCommonSupersequence("abac","cab"))
print(obj.shortestCommonSupersequence("aaaaaa","aaaaaa"))
print(obj.shortestCommonSupersequence("bbbaaaba","bbababbb"))