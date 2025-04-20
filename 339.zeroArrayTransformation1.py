from typing import List
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        #line sweep algo
        #binary search
        #but once we find it can be made zero at any nth query,return True
        #else, increasethe no of queries needed
        #or
        #just process all the queries and return True /False

        diff=[0]*(len(nums)+1)

        for l,r in queries:
            diff[l]+=1
            diff[r+1]-=1
        
        runningSum=0
        for i in range(len(nums)):
            #print("runningSum",runningSum)
            runningSum+=diff[i]
            if runningSum<nums[i]:
                return False
        return True

        
        