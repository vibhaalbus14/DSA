from typing import List
from functools import reduce
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return (reduce(lambda x, y: x | y, nums)) << (len(nums) - 1)
obj=Solution()
print(obj.subsetXORSum([1,2,3]))