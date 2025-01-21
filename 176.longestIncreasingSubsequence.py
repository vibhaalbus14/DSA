#-----------------approach : memoization------------
#time comp:0(n**2)
#space comp:O(n*n)+O(n)[call stack]
from functools import cache
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def helper(index,cmpVal):
            if index>=len(nums):
                return 0
            foundGreaterVal=0
            foundLesserVal=0
            #foundGreaterValNotConsider=0
            if nums[index]>cmpVal:
                #which means we've found something greater
                foundGreaterVal=helper(index+1,nums[index])+1
                #foundGreaterValNotConsider=helper(index+1,cmpVal)
            
            foundLesserVal=helper(index+1,cmpVal)
            return max(foundGreaterVal,foundLesserVal)
             

        maxCount=float('-inf')
        for i in range(len(nums)):
            maxCount=max(maxCount,helper(i+1,nums[i]))
        return maxCount


obj=Solution()
print(obj.lengthOfLIS([10,9,2,5,3,7,101,18]))


#-----------------approach : tabulation------------
#time comp:0(n**2)
#space comp:O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp tabulation
        #since we need to find strictly increasing 
        #in tabulation we go from bottom , to top
        #we consider the prev indices whose value is lower than the current indices
        dp=[1]*len(nums)
        #why 1? because,at every step max we can consider is itself
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)#only that i th number
                    #or lesser number +1,since max length is needed
        return max(dp)
#-----------------------approach:monotonic stack and binary search--------------
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #monotonic stack approach
        #1.start iterating through the nums and add elements into stack
        #2.if the element encountered is smaller than the one already in stack,identify the element in stack such that,
        #element>=num and elment is smallest
        #3.to identify the smallest_element>=num, we do binary search,
        #plus the way elements are inserted into stack keeps it sorted
        #4.return the len of stack
        #5.note: the subsequence is not obtained, only the correct length is obtained
        def binarySearch(target,l,h,stack):
            while l<=h and h>-1:
                mid=(l+h)//2
                if stack[mid]>=target:#since the goal is to find the smallest
                    h=mid-1
                else:
                    l=mid+1
            return l
#10,9,2,5,3,7,101,18------------------------> stack:2,3,7,18 a correct insertion position for 9=>binary search
        stack=[]
        count=0
        for num in nums:
            if not stack or num>stack[-1]:
                stack.append(num)
            elif num<stack[-1]:
                index=binarySearch(num,0,len(stack)-1,stack)
                stack[index]=num
        return len(stack)

