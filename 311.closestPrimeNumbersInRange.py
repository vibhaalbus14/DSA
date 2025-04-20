from math import sqrt
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        #if i is prime then
        #from i*i till n+1 in steps of i, all the numbers are not prime=> multiples of prime are non prime
        #=> sieve of eratosthenes algo to find primes in range(1,n)
        #time comp = O(n*(log(logn))) faster compared to O(n*sqrt(n))

        primeList=[True]*(right+1)
        primeList[0]=primeList[1]=False

        def eratosthenes(n):
            nonlocal primeList

            for i in range(2,int(sqrt(n))+1):
                #if the current number is prime
                if primeList[i]:
                    #acc. to algo, all the numbers that are multiples of i are non prime
                    for j in range(i*i,n+1,i):#starting from i*i ensures the smallest prime divisor mark it false
                        primeList[j]=False
        
        eratosthenes(right)
        #make a list of all primes within the range [left,right]
        primeNos=[]
        for i in range(left,right+1):
            if primeList[i]:
                primeNos.append(i)
        
        if len(primeNos)<2:
            return [-1,-1]
        
        minDiff=float("inf")
        for i in range(len(primeNos)-1):
            if primeNos[i+1]-primeNos[i]< minDiff:
                num1=primeNos[i]
                num2=primeNos[i+1]
                minDiff=num2-num1
        return [num1,num2]

        