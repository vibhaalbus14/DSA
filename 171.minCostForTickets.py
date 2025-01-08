from typing import List
from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo={}
        def helper(day:int):
            if day in memo:
                return memo[day]
            if day>days[-1]:
                return 0 #do not include any more days as all days are covered
            if day>365:
                return float('inf')
            if day not in days: #to skip non travel days
                return helper(day+1)

            oneDayPass=helper(day+1)+costs[0]
            sevenDayPass=helper(day+7)+costs[1]
            thirtyDayPass=helper(day+30)+costs[2]
            memo[day]=min(oneDayPass,sevenDayPass,thirtyDayPass)
            return memo[day]
        return helper(1)