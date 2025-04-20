from functools import lru_cache
from typing import List

#------------------------TC :O(n*n^2*n) here currSum possiblities=n^2------------


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        #no col constraint
        #one element from every row must be chosen
        #dp question

        m=len(mat)
        n=len(mat[0])

        @lru_cache(None)
        def dp(row,currSum):
            nonlocal globalMin
            if row>=m:
                globalMin=min(globalMin,abs(currSum-target))
                return
            #every row has n choices to choose from
           
            for j in range(n):
                dp(row+1,currSum+mat[row][j])
            
        globalMin=float("inf")
        dp(0,0)
        
        return globalMin
            
#---------------optimization after removing  dup-----------------
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        #no col constraint
        #one element from every row must be chosen
        #dp question

        m=len(mat)

        @lru_cache(None)
        def dp(row,currSum):
            nonlocal globalMin
            if row>=m:
                globalMin=min(globalMin,abs(currSum-target))
                return
            #every row has n choices to choose from
           
            for j in range(len(mat[row])):
                
                dp(row+1,currSum+mat[row][j])
                   
        globalMin=float("inf")
        for i in range(m):
            #set=> to remove duplicates
            #sort? this wont always work but passes in this prob
            #we sort every row and when we find that 
            #currSum+num-target>globalMin=>break
            #what does this mean?
            #it means whenever we try to reach the min abs diff from a positive side, it wont work
            #even tho we havent epxlored all paths /rows, we break early
            #
            mat[i]=list(set(mat[i]))
            
        dp(0,0)
        
        return globalMin

#------------------------optimisation after removing dup and sorting-----------
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        #no col constraint
        #one element from every row must be chosen
        #dp question

        m=len(mat)

        @lru_cache(None)
        def dp(row,currSum):
            nonlocal globalMin
            if row>=m:
                globalMin=min(globalMin,abs(currSum-target))
                return
            #every row has n choices to choose from
           
            for j in range(len(mat[row])):
                if currSum+mat[row][j]-target>globalMin:
                    break
                dp(row+1,currSum+mat[row][j])
                   
        globalMin=float("inf")
        for i in range(m):
            #set=> to remove duplicates
            #sort? this wont always work but passes in this prob
            #we sort every row and when we find that 
            #currSum+num-target>globalMin=>break
            #what does this mean?
            #it means whenever we try to reach the min abs diff from a positive side, it wont work
            #even tho we havent epxlored all paths /rows, we break early
            #
            mat[i]=sorted(set(mat[i]))
            
        dp(0,0)
        
        return globalMin
            




        
            




        




        