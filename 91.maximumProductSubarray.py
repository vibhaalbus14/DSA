# #time complexity:O(n^2)=> helper is called n times and for each call, for loop till the end of array
# #space complexity:O(n)=>max size of subarray being stored at a given time is n
# from functools import reduce
# class Solution(object):
#     def maxProduct(self, nums):
        
#         #form subarrays
#         def helper(start,nums,maxProd):
#             if start==len(nums):
#                 #array ended
#                 return maxProd
#             for i in range(start,len(nums)):
#                 subArray=nums[start:i+1]
#                 print(subArray)
#                 if len(subArray)!=len(nums):#everything is a valid subarray except the entire array
#                     currentProduct=reduce(lambda a,b: a*b,subArray)
#                     maxProd=max(currentProduct,maxProd)#identify max product
#             print()
#             return helper(start+1,nums,maxProd)
#         return helper(0,nums,float('-inf'))
        
# obj=Solution()

# print(obj.maxProduct([-4,-3]))

#----------------approach 2--------------------------------
#time comp:O(n)
#space comp:O(1)
class Solution(object):
    def maxProduct(self, nums):
        if len(nums)==0:
            return 0
        res=currMax=currMin=nums[0]
        for num in nums[1:]:
            #swap if negative
            #max does not consider -ve value
            #min considers -ve value
            #if even -ves are encountered, this increases the max, but even or odd is not known
            #hence we are keeping track of minimum that considers the -ve value into mul
            #and max that considers the max at current index
            if num<0:
                currMax,currMin=currMin,currMax
            currMax=max(num,currMax*num)
            currMin=min(num,currMin*num)
            #at every index , update the result
            res=max(res,currMax)
            print(currMax,currMin,res)
        return res
obj=Solution()
print(obj.maxProduct([-4,-3]))