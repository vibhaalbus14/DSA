from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        #approach
        #line sweep algorithm
        #1.birth year->mark +1
        #2.death years-> mark -1
        #3.now sort the years
        #4.use a maxval to keep check of no of people alive,and update 
        #earliest year

        years=[]
        for birth,death in logs:
            years.append((birth,1))
            years.append((death,-1))
        
        earliestYear=None
        maxCount=float("-inf")

        years.sort(key = lambda x:(x[0],x[1]))

        totalPop=0
        for year,curr in years:
            totalPop+=curr
            if totalPop>maxCount:
                maxCount=totalPop
                earliestYear=year
        
        return earliestYear
            
