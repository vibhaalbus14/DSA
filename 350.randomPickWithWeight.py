from typing import List
from math import  random
import bisect

class Solution:
    #approach
    #1.create a prefix sum array
    #2.make a random module choose something bw (1,sum(all nums))
    #3.map that random no to prefix sum array and find its insert pos
    #4.this index position is the index position to be returned

    #rather than creating say [1,2,3] as [0,1,1,2,2,2]=> rpeting indices w no of times
    #entire thing is simulated in prefix sums
    #1[1,3,6]=> 1 to 1="1" nos ; 1 to 3 => "2" nos and 3 to 6 => "3" nos 

    def __init__(self, w: List[int]):
        self.prefixSum=[w[0]]

        for i in range(1,len(w)):
            self.prefixSum.append(self.prefixSum[-1] + w[i])

    def pickIndex(self) -> int:
        num=random.randint(1,self.prefixSum[-1])
        return bisect.bisect_left(self.prefixSum,num)        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()