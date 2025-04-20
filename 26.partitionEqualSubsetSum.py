# class Solution(object):
#     def canPartition(self, nums):
#         if(sum(nums)%2!=0):
#             return False
#         else:
#             target=sum(nums)//2
        
#         def helper(target,index):
#             if index>=len(nums) or target <0:
#                 return False
#             elif target==0:
#                 return True
#             else:
#                 include=helper(target-nums[index],index+1)
#                 exclude=helper(target,index+1)
#                 return include or exclude
#         return helper(target,0)
# object=Solution()
# print(object.canPartition([1,2,3,4,5]))

class Solution(object):
    def canPartition(self, nums):
        if(sum(nums)%2!=0):
            return False
        else:
            target=sum(nums)//2
        ht={}
        
        def helper(target,index,ht):
            if target==0:
                return True
            elif index>=len(nums) or target <0:
                return False
            else:
                if (index,target) in ht:
                    return ht[(index,target)]
                else:
                    include=helper(target-nums[index],index+1,ht)
                    exclude=helper(target,index+1,ht)
                    ht[(index,target)]=include or exclude
                    return ht[(index,target)]
        return helper(target,0,ht)
object=Solution()
print(object.canPartition([1,2,3,4,5]))
        
#-------------------------optimal------------------------
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False

        l = len(nums)
        target = total//2
        nums.sort(reverse=True)
        memo={}

        
        def dfs(i, curr):
            if i>=l or curr>target:
                return False
            if (i,curr) in memo:
                return memo[(i,curr)]
            if curr+nums[i]==target: #include step
                return True
            include=dfs(i+1,nums[i]+curr)
            if not include:
                exclude=dfs(i+1,curr)
            memo[(i,curr)]=include or exclude
            return include or exclude

        return dfs(0, 0)