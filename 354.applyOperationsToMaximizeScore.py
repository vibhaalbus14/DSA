from math import sqrt,pow
import heapq
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        #1.create a prime score array for every num in n
        #2. to maximise the score , we always choose max number using maxHeap
        #3.but to identify no of  distinct subarrays in which max Num can be obt, we construct monotonic stack
        #4.monotonic dec stack , where all the indices are arranged with respect to primes scores
        #5.forming left and right sub arrrays from the given index and multiplying them will give us no of subarrays the chosen nocan be part of
        #6.do this till all k operations are used up


        #create primescore array
        primeScoreList=[]
        n=len(nums)
        MOD=10**9+7
        for num in nums:
            score=0
            #calc the factors of num
            for factor in range(2,int(sqrt(num)+1)):
                #if the factor is actual a factor of the chosen num
                if num%factor==0:
                    score+=1
                    #remove all same factors
                    while num%factor==0:
                        num//=factor
            
            if num>=2: #left over num apart fromo one is considereda factor
                score+=1

            primeScoreList.append(score)

        #create a monotonic stack
        leftSubarray=[-1]*n
        rightSubarray=[n]*n
        stack=[]

        for i in range(n):
            while stack and primeScoreList[i]>primeScoreList[stack[-1]]:
                index=stack.pop()
                rightSubarray[index]=i#this curr element forms the end of popped index element

            #if the currScore is less than the toop score, then it can expand on left side till the top index
            if  stack:
                leftSubarray[i]=stack[-1]
            stack.append(i)

        #construct maxHeap to maxmise the ops
        res=1
        maxHeap=[]
        for i in range(n):
            maxHeap.append((-nums[i],i))
        heapq.heapify(maxHeap)

        while k>0:
            num,index=heapq.heappop(maxHeap)
            num=-num
            
            #calculate the no of subarrays it can be part of
            subArrays=(index-leftSubarray[index])*(rightSubarray[index]-index)
            if k<subArrays:
                power=k
            else:
                power=subArrays
            res*=pow(num,power,MOD)#if pow is too big,3rd param will handle
            res%=MOD
            k-=subArrays
          
            
        return res

                
                





        