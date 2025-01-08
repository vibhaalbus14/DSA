from typing import List
from functools import lru_cache
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache #memo[(indexList,i)]=minSum
        def helper(indexList,i):
            if indexList==len(triangle) or i==len(triangle[indexList]):
                return 0
            #for first list,no choice,index is 0
            includeNum=helper(indexList+1,i)+triangle[indexList][i]
            includeNumPlus=helper(indexList+1,i+1)+triangle[indexList][i]
            return  min(includeNum,includeNumPlus)
        return helper(0,0)
obj=Solution()
print(obj.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
            
            