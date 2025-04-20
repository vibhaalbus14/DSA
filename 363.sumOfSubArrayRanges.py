from typing import List
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        #approach
        #1.range of each subarray = max1-min1 + max2-min2+.....+maxn-minn
        #2.this can be formed as max(subArrays)-min(subArrays)
        #3.identify the sum of subarray maximums and identify the sum of subarray minimums
        #4.total= sum(maxs)-sum(min)
        #to find maxs=> monotonic dec stack
        #to find mins=> monotonic dec stack

        decStack=[]
        incStack=[]
        totalSum=0
        for i,num in enumerate(nums):
            
            #to find no of subarrays a current num can be a max
            #dec monotonic stack
            while decStack and num>decStack[-1][1]:
                prevIndex,prevVal=decStack.pop()
                backwardExt=prevIndex-(-1 if not decStack else decStack[-1][0])
                forwardExt=i-prevIndex
                #since its max, add to totalSum
                totalSum+=(backwardExt * forwardExt * prevVal)
            decStack.append((i,num))

            #to find no of subarrays a current num can be a min
            #inc monotonic stack
            while incStack and num<incStack[-1][1]:
                prevIndex,prevVal=incStack.pop()
                backwardExt=prevIndex-(-1 if not incStack else incStack[-1][0])
                forwardExt=i-prevIndex
                #since its min, sub from totalSum
                totalSum-=(backwardExt * forwardExt * prevVal)
            incStack.append((i,num))

        #include the left over nums in both inc and dec stack
        while decStack:
            prevIndex,prevVal=decStack.pop()
            backwardExt=prevIndex-(-1 if not decStack else decStack[-1][0])
            forwardExt=len(nums)-prevIndex
            totalSum+=(backwardExt * forwardExt * prevVal)
        
        while incStack:
            prevIndex,prevVal=incStack.pop()
            backwardExt=prevIndex-(-1 if not incStack else incStack[-1][0])
            forwardExt=len(nums)-prevIndex
            totalSum-=(backwardExt * forwardExt * prevVal)
        
        return totalSum


        