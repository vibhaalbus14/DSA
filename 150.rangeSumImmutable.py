class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        sum=0
        while left<=right and left>-1 and right<len(self.nums):
            sum+=self.nums[left]
            left+=1
        return sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)