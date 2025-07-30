from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        #backtracking
        #maximum bitwise OR is Or-ing all the numbers and getting as many one's as possible
        count=0
        maxVal=0
        n=len(nums)
        for num in nums:
            maxVal=maxVal | num


        def backtrack(index,currVal):
            nonlocal count,maxVal,n
            if index==n :
                if currVal==maxVal:
                    count+=1
                return
            backtrack(index+1,currVal)#exclude
            #include
            currVal|=nums[index]
            backtrack(index+1,currVal)
            currVal^=nums[index]
        
        backtrack(0,0)

        return count



        