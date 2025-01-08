#max passes for left=len(nums)
#passes for right=len(nums)
#time comp=O(n) due to sorting
#space comp=O(1) in program but canbe O(1) or O(n) or O(logn) acc to sorting algo used
class Solution(object):
    def maxFrequency(self, nums, k):
        left=right=0
        maxFreq=1
        maxSumAfterKOperations=k
        nums.sort()
        #2 pointers approach 
        #sort the array as the lower elements can be incremented to match the higher elmeents
        #only inc operations are allowed
        while left<=right and right <len(nums):
            maxSumAfterKOperations+=nums[right]
            #print(maxSumAfterKOperations)
            sumOfWindow=(right-left+1)*nums[right]#length of window * right most elemnet of the window
            #print(sumOfWindow)
            if sumOfWindow<=maxSumAfterKOperations:
                #window valid , increase the size of the window
                maxFreq=max((right-left+1),maxFreq)
                #print(maxFreq)
                right+=1
            else:
                #window invalid as the no of operations used on elements are more than specified
                #reduce the no of elements on which operation is to be performed
                maxSumAfterKOperations-=nums[left]
                maxSumAfterKOperations-=nums[right]#since right most gets added acc to progrm logic again
                left+=1
        return maxFreq
obj=Solution()
print(obj.maxFrequency([3,9,6],2))
            

