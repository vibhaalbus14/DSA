class Solution(object):
    def removeDuplicates(self, nums):
        uniqueIndexPtr=1
        occ=1#since the element at 0th index is considered unique already
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1] and occ<2:
                occ+=1
                nums[uniqueIndexPtr]=nums[i]
                uniqueIndexPtr+=1
            #if the numbers repeat and occurence is greater than 2, no action required
            else:
                if(nums[i]!=nums[i-1]):
                    occ=1
                    nums[uniqueIndexPtr]=nums[i]
                    uniqueIndexPtr+=1
            
        return uniqueIndexPtr
object=Solution()
print(object.removeDuplicates([1,1,1,2,2,3]))