from typing import List
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        stack=colors+colors
        count=0
        
        l=0
        r=k-1
        diff=0
        for i in range(l+1,r+1):
            if stack[i]==stack[i-1]:
                diff+=1

        if diff==0:
            count+=1
        
        for l in range(1,n):
            if stack[l-1]==stack[l]:#extend l pointer
                diff-=1
            r+=1#make it size=k
            if stack[r]==stack[r-1]:
                diff+=1

            if diff==0:
                count+=1
                
        return count
        
        

        