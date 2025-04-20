from typing import List
from math import sqrt
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        #approach
        #1.binary search  alongside time range
        #2. since all mechanics can mend in one shot, sum of cars that each mechanic can mend given the time from binary search using the math formula given

        def findCarSum(time):
            sum=0
            for rank in ranks:
                sum+=int(sqrt(time//rank))#sum of cars each mechanic can do
            return sum>=cars

        l=1
        r=max(ranks)*cars*cars

        while l<=r:
            mid=(l+r)//2
            if findCarSum(mid):
                #if its valid
                #reduce time nd check
                r=mid-1
            else:
                #inc time
                l=mid+1
        return l

        