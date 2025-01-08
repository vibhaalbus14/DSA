from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #why xor?
        #basics: bitwise operators perform calculations at binary level but 
        #accept ip and op in decimal,hexadecimal , binary etc
        #1.if the numbers are same lets say 0 ^ 0=0 and 1^1=1
        #2.now how does this apply to our problem?
        #3.every number that repeats have the same binary rep
        #4.so xor of 4 i.e 4^4=0 => 0100 ^ 0100 =0
        #5.so lets take 4,1,2,1,2 , both 1's cancel each other,2's cancel eachother so finally
        #6.4^0=>0100 ^ 0000 =0100 == 4
        #7.hence this approach works

        res=0
        for n in nums:
            res=res^n
        return res
        