# from functools import lru_cache
# class Solution:
#     def canBeValid(self, s: str, locked: str) -> bool:
#         n=len(s)

#         @lru_cache(None)
#         def helper(index,left):
#             if index>=n :
#                 if left==0: #balanced
#                     return True
#                 return False
            
#             if left<0:
#                 return False
            
#             normal=False
#             withLocks=False
#             #changes can be made only if locked[i]=0
#             if s[index]=="(":
#                 normal=helper(index+1,left+1)
#                 if locked[index]=="0":
#                     withLocks=helper(index+1,left-1)
#             elif s[index]==")":
#                 normal=helper(index+1,left-1)
#                 if locked[index]=="0":
#                     withLocks=helper(index+1,left+1)
#             #check if it can be changed

#             return normal or withLocks

#         return helper(0,0)
            
#----------------------------------approach---------------------------------------------
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n=len(s)
        #treat "0" lock as wildcard
        if n==1:
            return False
        minLeft,maxLeft=0,0

        for i,paren in enumerate(s):
            if locked[i]=="0":
                #options
                minLeft,maxLeft=minLeft-1,maxLeft+1
            elif locked[i]=="1":
                if paren=="(":
                    minLeft,maxLeft=minLeft+1,maxLeft+1
                else:
                    minLeft,maxLeft=minLeft-1,maxLeft-1
            
            if maxLeft<0: #no way to generate valid parenthesis
                return False
            
            if minLeft<0: #we can maybe not change "0" locks to ")"
            #its revocable
                minLeft=0
                minLeft+=1 #because u can only change *->"(" or ")", if minleft<0 it means
                #changing to ")" didnt work, so change it to "("
            
        if minLeft==0:#minLeft should be zero to ensure the brackets are balanced
            return True
        else:
            return False

        