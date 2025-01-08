class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        prefixSum=[0 for i in range(n+1)]
        for i in range(1,len(prefixSum)):
            prefixSum[i]=prefixSum[i-1]+nums[i-1]
        for pivotIndex in range(len(nums)):
            left=prefixSum[pivotIndex]
            right=prefixSum[n]-prefixSum[pivotIndex+1]
            if left==right:
                return pivotIndex
        return -1