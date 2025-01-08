from functools import reduce
from typing import List
class Solution(object):
    def subsetXORSum(self, nums:List[int])->int:
        res=0
        def calc_subset(subset,index):
            nonlocal res
            n=len(nums)
            if(index==n):
                if(len(subset)==0):
                    pass
                else:
                    res+=reduce(lambda a,b: a^b,subset)
                return
            else:
                calc_subset(subset,index+1)
                subset.append(nums[index])
                calc_subset(subset,index+1)
                subset.pop()
        calc_subset([],0)
        return res
obj=Solution()
print(obj.subsetXORSum([1,2,3]))




