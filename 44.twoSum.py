# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(0,len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]
# object=Solution()
# print(object.twoSum([2,7,11,15],9))

def two_sum(array,target):
    #write code here
    
    ht={}
    for i,num in enumerate(array):#enumerate first return the index then the num
        complement=target-num
        
        if complement in ht:
            return [i,ht[complement]]
        
        ht[num]=i
    return []
        
    
print(two_sum([2, 7, 11, 15],9))