from typing import List
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        #approach
        #1.rather than sending every number from starting bound and identifying which will lead to res
        #2.see the digits that go through next round by comapring the end values
        #3.once all rounds aka pipes are passed,identify the digits in the pipe

        low=bounds[0][0]
        high=bounds[0][1]


        for i in range(1,len(original)):
            diff=original[i]-original[i-1]

            #check if the current pipe values can get these next values from next pipe

            #i=> curr pipe
            low=max(low+diff,bounds[i][0])
            high=min(high+diff,bounds[i][1])
            #try to get as many numbers that intersect/overlap or pass through the pipe
            #satisfying the difference

            if low>high:
                return 0
        return high-low+1