class Solution(object):
    def twoSum(self, nums, target):
        l,r=0,len(nums)-1
        while(l<r):
            sum_obt=nums[l]+nums[r]
            if sum_obt==target:
                return [l+1,r+1]
            elif sum_obt<target:
                l+=1
            else:
                r-=1

object=Solution()
print(object.twoSum([2,7,11,15],9))