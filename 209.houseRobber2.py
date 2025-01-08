# #---------------------------------------------------------------------------------------------
# from typing import List
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         #only thing, keep a flag to see if first house at index 0
#         #is robbed or not, if yes and u reach last house at index n-1,
#         #then dont rob
#         n=len(nums)
#         memo={}

#         def helper(index,flag):
#             if (index,flag) in memo:
#                 return memo[index,flag]
#             if index==n-1:
#                 if not flag:
#                     return nums[index]
#                 else:
#                     return 0
#             if index>=n:
#                 return 0
#             #exclude step
#             exclude=helper(index+1,flag)
#             #include step
#             if index==0:#which means including 0th index house
#                 include=helper(index+2,1)+nums[index]
#             else:
#                 include=helper(index+2,flag)+nums[index]#why +2? skipping adjacent house
#             memo[(index,flag)] =max(include,exclude)
#             return memo[(index,flag)]
#         return helper(0,0)

#------------------------------------------------------------------------------------------------------
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        #rather than using a flag that occupies more space,
        #pass 2 nums  1.from first house till last but one
        #2.from 2nd house till last house
        n=len(nums)
        if n==1:
            return nums[0]
        def changeNumsRange(start,end):
            memo={}
            def helper(index):
                nonlocal memo
                if index in memo:
                    return memo[index]
                
                if index>=end:
                    return 0
                #exclude step
                exclude=helper(index+1)
                #include step
                
                include=helper(index+2)+nums[index]#why +2? skipping adjacent house
                memo[index] =max(include,exclude)
                return memo[index]
            return helper(start)
        
        fromFirstHouse=changeNumsRange(0,n-1)
        fromSecondHouse=changeNumsRange(1,n)
        return max(fromFirstHouse,fromSecondHouse)

            