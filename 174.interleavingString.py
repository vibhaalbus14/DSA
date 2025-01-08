class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        p,q,r=len(s1),len(s2),len(s3)
        if p==q==r==0:
            return True
        if p==0:
            if s2==s3:
                return True
        if q==0:
            if s1==s3:
                return True
        if r<p+q:
            return False
        memo={}
        def helper(i,j,k):
            nonlocal memo
            if (i,j) in memo:
                return memo
            if i==p and j==q and k==r:
                return 1 #all matches
            matchesWithS1=0
            matchesWithS2=0
            
            if i<p and k<r:
                if s1[i]==s3[k]:#both matches
                    matchesWithS1=helper(i+1,j,k+1)
            if j<q and k<r:
                if  s2[j]==s3[k]:
                    matchesWithS2=helper(i,j+1,k+1)
            memo[(i,j,k)]=matchesWithS1 or matchesWithS2
            return memo[(i,j,k)]
        helper(0,0,0)
                
        