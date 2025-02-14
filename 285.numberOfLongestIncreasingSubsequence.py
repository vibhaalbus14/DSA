from typing import List
from collections import lru_cache

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        @lru_cache(None)
        def helper(index,cmpVal):#1,3,5,4,7
            if index>=n:
                return (0,1) #length,occurence
            exclude_length,exclude_occ=helper(index+1,cmpVal)

            include_length,include_occ=0,1
            
            if nums[index]>cmpVal:
                next_length,next_occ=helper(index+1,nums[index])
                include_length,include_occ=next_length+1,next_occ

                include=max(include,helper(index+1,nums[index])+1)
                
            
            #pass on longest length and its occurence
            if exclude_length>include_length:
                maxLength,occ= exclude_length,exclude_occ
            elif exclude_length<include_length:
                maxLength,occ= include_length,include_occ
            else:
                maxLength,occ=exclude_length,include_occ+exclude_occ
            
            return maxLength,occ
            
          
        

        maxLength,count=helper(0,float("-inf"))
        
        return count
    

        

            