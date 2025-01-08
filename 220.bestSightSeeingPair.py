from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # #similar to buy and sell stocks

        # @cache
        # def helper(index,seen):
        #     if index>=len(values) :
        #         return float("-inf")
        #     skip=helper(index+1,seen)
        #     pickFirst=float("-inf")
        #     pickSecond=float("-inf")
        #     if seen: #already chosen one spot
        #         #choose this spot
        #         pickSecond= values[index]-index #+helper(index+1,seen+1)
        #     else:
        #         #choose the spot
        #         pickFirst=helper(index+1,1)+values[index]+index
            
        #     # print(f"index:{index},seen:{seen},skip :{skip},pickFirst:{pickFirst},pickSecond:{pickSecond},max:{max(skip,pickFirst,pickSecond)}")

        #     return   max(skip,pickFirst,pickSecond)

        # return helper(0,0)  
#-------------------------------------------------------------------------------------------------- 
        #greedy approach
        #1.assume the first element is the second pair
        #2.initialize this current max to  value-distance
        #3.rather than taking the values and then subtracting their distance
        #4.we choose a value by subtracting the distance to next value,as we progress, we keep subtracting the values to match the distances

        res=0
        secondPair=values[0]-1 #since first comparision is with index 1,
        #0-1=-1, hence we intitially subtracted the val and kept it ready
        for i in range(1,len(values)):
            #choose the res
            res=max(res,values[i]+secondPair)
            #update secondPair, it can either be some previous value/current value
            secondPair=max(secondPair-1,values[i]-1)
        return res
