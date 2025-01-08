class Solution(object):
    def majorityElement(self, nums):
        
        # n=len(nums)
        # hashmap={}
        # for num in nums:
        #     if num in hashmap:
        #         hashmap[num]+=1
        #     else:
        #         hashmap[num]=1
        # max_val=max(hashmap.values())
        # for key,val in hashmap.items():
        #     if val==max_val:
        #         return key
        nums.sort()
        return nums[len(nums)//2]
obj=Solution()
print(obj.majorityElement([2,2,1,1,1,2,2]))
            