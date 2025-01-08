#-----------------------------------approach1 : swapping-------------------------------
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        zeroPtr=0
        nonZeroPtr=0

        #approach:
        #1.make zeroPtr point to 0 value and nonZeroPtr to non-zero value
        #2.if zeroPtr<nonZeroPtr index=>swap adn make both the values equal to nonZero ptr val
        #3.zeroPtr>nonZeroPtr then only increment the nonZeroPtr index as it is positioned properly
        #4.do this on loop till nonZeroPtr < len(nums)

        while nonZeroPtr<len(nums):
            while nonZeroPtr<len(nums) and nums[nonZeroPtr]==0 :
                nonZeroPtr+=1

            while zeroPtr<len(nums) and nums[zeroPtr]!=0  :
                zeroPtr+=1#always maintain at first occurence of 0

            if zeroPtr<len(nums) and nonZeroPtr<len(nums) :
                if zeroPtr<nonZeroPtr :
                    nums[zeroPtr], nums[nonZeroPtr]=nums[nonZeroPtr],nums[zeroPtr]#swap
                    zeroPtr+=1#make it point to same next index
                else:
                    nonZeroPtr+=1
        
#----------------------------------approach 2-----------------------------

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #use stack
        count=0
        stack=[]
        for num in nums:
            if num==0:
                count+=1
            else:
                stack.append(num)
        for i in range(0,count):

            stack.append(0)
        nums[:]=stack[:]