class Solution(object):
    def threecurrent_sum(self, nums):
        
        finalList=[]

        for i in range(len(nums)):
           for j in range(i+1,len(nums)):
               thirdNum=-(nums[i]+nums[j])
               #if thirdNum in nums and nums.index(thirdNum)!=i and nums.index(thirdNum!=j):
               if thirdNum in nums[j+1:]:
                   finalList.append([nums[i],nums[j], -(nums[i]+nums[j])])
        finalList=[list(v) for v in set(tuple(sorted(lst))for lst in finalList)]
        return finalList

object=Solution()
print(object.threecurrent_sum([-1,0,1,2,-1,-4]))
print(object.threecurrent_sum([0,0,1]))    
print("----------------------------------------------")

# class Solution(object):
#     def threecurrent_sum(self, nums):
#         finalList=[]
#         nums=sorted(nums)
#         for fixedPtr in range(0,len(nums)-2):#ensuring the positions to l and r pointers remain
#             if fixedPtr>0 and nums[fixedPtr]==nums[fixedPtr-1]:#to remove duplicates
#                 continue

#             l=fixedPtr+1
#             r=len(nums)-1
#             while(l<r):
#                 current_sum=nums[l]+nums[r]+nums[fixedPtr]
#                 if current_sum==0:
#                     finalList.append([nums[fixedPtr],nums[l],nums[r]])
#                     l+=1
#                     r-=1
#                     #first occurence of the number is considered and then duplicate is checked for
#                         #-2,-2,0,-1,2,2,3,3,4,4
#                         #remove duplicates from left pointer
#                     while l<r and nums[l]==nums[l-1]:
#                         l+=1
#                         # remove duplicates from right pointer
#                     while l<r and nums[r]==nums[r+1]:
#                         r-=1
#                 elif current_sum<0:
#                     l+=1
#                 else:
#                     r-=1
        
#         return finalList
# object=Solution()
# print(object.threecurrent_sum([-1,0,1,2,-1,-4]))
# print(object.threecurrent_sum([-2,-2,0,-1,2,2,3,3,4,4]))
# print(object.threecurrent_sum([0,0,1]))        

