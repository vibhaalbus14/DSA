from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #to get max sum in bw the array=> kadanes algo 
        # to get max sum from circular subarray => total-min subarray sum from kadanes
        #return max(gobalMax from kadanes, total-min Sum)
        #note: if nums=[-1,-2,-3,-4]
        #then globalMax=-1 ; total=-10 and globalMin=-10
        #then max(-1,-10-(-10))=> max(-1,0)=>0
        #its immposible to form a sum "0" from negative numbers
        #hence ig globalMax<0: return globalMax else max(globalMax,total-globalMin)

        currSumMax=0
        globalMax=nums[0]
        total=0
        currSumMin=0
        globalMin=nums[0]

        for num in nums:
            #in same iteration , we compute globalMax,globalMin,total
            currSumMax+=num
            currSumMax=max(currSumMax,num)
            globalMax=max(currSumMax,globalMax)

            currSumMin+=num
            currSumMin=min(currSumMin,num)
            globalMin=min(currSumMin,globalMin)

            total+=num
        
        #check for all negative number edge case
        return globalMax if globalMax<0   else max(globalMax,total-globalMin) 
