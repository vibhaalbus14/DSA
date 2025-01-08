def LongestCommonSubsequence(text1,text2):
    mem={}
    def helper(i,j):
        if(i==len(text1) or j==len(text2)):
            return ""
        else:
            if (i,j) in mem:
                return mem[(i,j)]
            else:
                if text1[i]==text2[j]:
                    
                    mem[(i,j)]= text1[i]+ helper(i+1,j+1)
                else:
                    temp1=helper(i+1,j)
                    temp2=helper(i,j+1)
                    mem[(i,j)]=temp1 if len(temp1)>len(temp2) else temp2
        return mem[(i,j)]
    return helper(0,0)
    
print(LongestCommonSubsequence("abac","abac"))