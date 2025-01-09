class Solution:
    def checkValidString(self, s: str) -> bool:
        #star=> (,),nothin
        #(()))( => not valid
        #this implies that at any point in string if closing brac> opening brackets=> string is invalid

        minLeft=0
        maxLeft=0

        for char in s:
            if char=="*":
                minLeft,maxLeft=minLeft-1,maxLeft+1 #min as * =>) and max as *=>(
            elif char=="(":
                minLeft,maxLeft=minLeft+1,maxLeft+1
            else:
                minLeft,maxLeft=minLeft-1,maxLeft-1

            if maxLeft<0:
                #=> despite using all * as (, if we cannot balance=>invalid
                return False
            
            if minLeft<0:
                #=> when we use * as ")", it doesnt contribute,so now use * as empty strings/nothing=> revocable
                minLeft=0
        
        if minLeft==0:
            return True
        else:
            return False

#------------------------------------------------------------------------------------------
from functools import lru_cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s)==1 and s!="*":
            return False
        #star=> (,),nothin
        #(()))( => not valid
        #this implies that at any point in string if closing brac> opening brackets=> string is invalid
        @lru_cache
        def helper(i,left,right):
            if right>left:
                return False
            if i>=len(s) and left==right:
                return True
            if i>=len(s):
                return False
            

            rightB=False
            leftB=False
            star=False

            if s[i]==")":
                rightB=helper(i+1,left,right+1)
            elif s[i]=="(":
                leftB=helper(i+1,left+1,right)
            else:
                star=((helper(i+1,left,right+1))or (helper(i+1,left,right)) or (helper(i+1,left+1,right)))
            
            return leftB or rightB or star

        return helper(0,0,0)

            


