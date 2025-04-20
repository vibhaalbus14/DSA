from typing import List
#TC:-------------------------------------------------------------O(n**2)-----------------------------------------------------------------------------
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res=0
        ithVal=nums[0]
        for j in range(1,len(nums)-1):
            #calculate the kth val
            # for k in range(j+1,len(nums)):
            #     res=max(res,(ithVal-nums[j])*nums[k])
            
            #take max k from leftover
            res=max(res,(ithVal-nums[j])*max(nums[j+1:]))
            
            #check if current ith val can be a jth val
            ithVal=max(ithVal,nums[j])
        return res
        

#-----------------------------------------------------------------TC:O(n)-----------------------------------------------------------------------------
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res=0
        ithVal=nums[0]
        max_diff=0
        for k in range(len(nums)):
            #first given the ith,jth and kth value, compute the max res

            res=max(res,max_diff*nums[k])
            #reset the ithVAL
            ithVal=max(ithVal,nums[k])
            #update the maxdiff,ith-jth=> check if j can take curr kth pos
            #this ensures i<j and upcoming k>j
            max_diff=max(max_diff,ithVal-nums[k])
        
        return res
        