from collections import defaultdict,Counter
from typing import List
from math import sqrt

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        #approach
        #1.create an adjList for evry num containing all the numbers with wich it can sum up and form a perfecrt sq
        #2.loop over only the unique nos in nums=> to avoid duplicacy
        #3.for every num, loop over it sq pairs in adjList a, if that num is available, use it up
        
        adjList=defaultdict(set)
        uniqueNums=set(nums)
        n=len(nums)
        freqMap=Counter(nums)
        finalAns=0
        
        for i in range(n):
            for j in range(i+1,n):
                ans=nums[i]+nums[j]
                #if isqrt(nums[i] + nums[j]) ** 2 == nums[i] + nums[j]:  # Check perfect square
                if sqrt(ans).is_integer():#check if its a perfect sq
                    adjList[nums[i]].add(nums[j])
                    adjList[nums[j]].add(nums[i])
       
        def backtrack(currNum,rem):
            if rem==0:
                return 1
            #go over its pair
            total=0
            for neighbour in adjList[currNum]:
                if freqMap[neighbour]!=0:
                    freqMap[neighbour]-=1
                    total+= backtrack(neighbour,rem-1)
                    freqMap[neighbour]+=1

            return total
        
        for num in uniqueNums:
            freqMap[num]-=1
            finalAns+=backtrack(num,n-1)
            freqMap[num]+=1
        
        return finalAns

        

        