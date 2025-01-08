# class Solution(object):
#     def rotate(self, nums, k):
#         list_start=nums[0:7-k]
#         list_end=nums[7-k:len(nums)]
#         list_end.extend(list_start)
#         return list_end
# object=Solution()
# list_inp=[1,2,3,4,5,6,7]
# print(list_inp)
# print(object.rotate(list_inp,3))
#-------------------------------------------------------------------------------------------------------
# class Solution(object):
#     def rotate(self, nums, k):
#         for count in range(k):
#             for index in range(len(nums)):
#                 storage=nums[0]
#                 if(index==len(nums)-1):
#                     nums[index]=storage
#                 nums[index]=nums[(index+1)%len(nums)]

#         return nums
# object=Solution()
# print(object.rotate([1,2,3,4,5,6,7],3))

#-------------------------------------------------------------------------------------------------------

# class Solution(object):
#     def rotate(self, nums, k):
#         n=len(nums)
#         k=k%n
#         if(k==0):
#             return nums
        
#         ptr2=n-k

#         def swap(a,b):
#             nums[a],nums[b]=nums[b],nums[a]

#         for ptr1 in range(n):
#             if(ptr2>n-1):
#                 print("----------------",nums)
#                 break
#             swap(ptr1,ptr2)
#             ptr2+=1
            
#         if(k<=n-k):
#             count=0
#             index=k
#             while(count<n-2*k):
#                 val=nums[index]
#                 nums.pop(index)
#                 nums.append(val)
#                 count+=1
#         return nums
# object=Solution()
# print(object.rotate([1,2,3,4,5,6,7],3))

#-------------------------------------------------------------------------------------------------------

class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        if(k==0):
            return nums
        
        nums.reverse()
        #reverse first k elements
        nums[:k]=reversed(nums[:k])
        #reverse the next elements
        nums[k:]=reversed(nums[k:])
        #nums[:]=last kth position elements in the same order+first kth elements in the same order
        #for this approach,sorting the elements is not needed
        #nums[:]=nums[-k:]+nums[:-k]
        #k=k%n=> to identify effective rotation if n==5 and k==5,=>no rotation
        return nums
object=Solution()
print(object.rotate([1,2,3,4,5,6,7],3))
