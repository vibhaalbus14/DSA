from typing import List
from collections import defaultdict
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        length=len(nums)
        hashMap1=defaultdict(int)
        for i,num in enumerate(nums):
            hashMap1[num]=i
        newNums=[]

        for a in nums:
            newNum1=str(a)
            sum1=0
            for n in newNum1:
                sum1+=int(n)
            
            newNums.append((a,sum1))
            
        newNums.sort(key=lambda x: (x[1],x[0]))
        
            
        
        hashMap2=defaultdict(int)
        for i,num in enumerate(newNums):
            n,currSum=num
            hashMap2[n]=i
        swaps=0
        for i in range(length):
            num1=newNums[i][0]
            num2=nums[i]
            
            if hashMap1[num1]!=hashMap2[num1]:
                
                
                oldPos1=hashMap1[num1]
                oldPos2=hashMap1[num2]

                if oldPos1!=hashMap2[num1] or oldPos2!=hashMap2[num2]:
                    hashMap1[num1],hashMap1[num2]=oldPos2,oldPos1
                    nums[oldPos2]=num1
                    nums[oldPos1]=num2
                    swaps+=1
            
                
        return swaps

        
        
        