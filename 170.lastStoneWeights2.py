import math
from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #pairing always acc to last diff will not yield min result
        #approach
        #1.sum up the weights
        #2.half=total//2
        #3.divide the weights into two grps(and hence /2) such that the sum of each
        #is A<=half
        #the other is total-A=B
        #4.sub A-B to get optimal difference
        if len(stones)==1:
            return stones[-1]
        total=sum(stones)
        halfValue=total//2
        #find one subset close to halfValue
        #dp here
        memo={}
        def helper(index,sum):
            nonlocal halfValue,stones
            if (index,sum) in memo:
                return memo[(index,sum)]
            if sum>halfValue or index>len(stones):
                return  0
            if index==len(stones) and sum<=halfValue:
                return sum
            #to get all possible combinations of subset
            include=helper(index+1,sum+stones[index])
            exclude=helper(index+1,sum)

            memo[(index,sum)]=max(include,exclude)
            return memo[(index,sum)]
        #once the max sum of subset such that sum<=halfValue is found
        firstSubset=helper(0,0)
        secondSubset=total-firstSubset
        return int(math.fabs(firstSubset-secondSubset))
