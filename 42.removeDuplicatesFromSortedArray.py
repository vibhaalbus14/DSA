# class Solution(object):
#     def removeDuplicates(self, nums):
#         count=0
#         for ptr1 in range (len(nums)):
#             for ptr2 in range(ptr1+1,len(nums)):
#                 if nums[ptr1]==nums[ptr2]:
#                     count+=1
#                     nums[ptr2]=101
#         nums=sorted(nums)
#         return len(nums)-count
# object=Solution()
# print(object.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

#fast and slow pointers    
#i is a fast pointer and unique_value or unique_index is a slow pointer
class Solution(object):
    def removeDuplicates(self, nums):
        unique_value=1 #consider the element at first position ,0th position to be unique

        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]):
                nums[unique_value]=nums[i]
                unique_value+=1
        print(nums)
        return unique_value
object=Solution()
print(object.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
#the reason this approach i.e unique_index=0 and comparing i and i+1 wont work because ur comparing in the end,but thers no element to coare with in the last
#hence take i and i-1
#if it differs at the first occurence ,add





