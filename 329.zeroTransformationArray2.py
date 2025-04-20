from typing import List 
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        #diff array
        #sweep line algo

        #1.pass the query till which u have to consider forming sweep line via binary serach, such that
        #min queries that satisfy the req are obt
        #2.form sweep line array for the queries
        #l,r,val => l +=val, for r+1. -=val
        #3.ensure all differenecs of all the queries are listed
        #4.now loop through diff array to find out if we have reached the number via diff or not
        #5.runningSum is imp to avoid neg effects on r+1 indices

        def sweepLineAlgo(index):
            diff=[0]*(len(nums)+1) #index +1 => total length +1 extra
            
            for i in range(index+1):
                l,r,val = queries[i]
                diff[l]+=val
                diff[r+1]-=val
            
            #now check if we can reach the number from 0
            runningSum=0
            for i in range(len(nums)):
                runningSum+=diff[i]
                if runningSum<nums[i]:
                    #cannot reach
                    return False
            return True
        
        #what if we cannot reach despite all queries
        if not sweepLineAlgo(len(queries)-1):
            return -1
        
        #what if we can reach without using any queries, i.e , all the nums are zero initially
        if all(num==0 for num in nums):
            return 0
        
        #implement binary Search to get min queries if possible
        l=0
        r=len(queries)-1

        while l<=r:
            mid=(l+r)//2
            if sweepLineAlgo(mid):
                #check if lower no of  queries can be usedto solve the same
                r=mid-1
            else:
                #check if on inc the queries, can solve it
                l=mid+1
        return l+1


