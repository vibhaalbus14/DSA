class Solution(object):
    def search(self, nums, target):
        low,high=0,len(nums)-1
        def helper(nums,low,high):
            if(low<=high):
                mid=(low+high)//2
                if nums[mid]==target:
                    return mid
                elif target<nums[mid]:
                    #search in first half
                    return helper(nums,low,mid-1)
                else:
                    #search in next half
                    return helper(nums,mid+1,high)

            return -1
        return helper(nums,low,high)
obj=Solution()
print(obj.search([-1,0,3,5,9,12],9))

        