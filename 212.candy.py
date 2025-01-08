from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        #greedy approach
        #1. 1st pass from left to right, comapare elements with that on lhs
        #2.2nd pass from right to left, compare elements with taht on rhs
        #3.use a list called candies with default val 1
        #4.only if elements are greater, on both the passes, we update
        #5.if its lesser or equal, keep the val at default

        n=len(ratings)
        candies=[1 for _ in range(n)]

        #left pass
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
        #right pass
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                #check if the val is already more
                if candies[i]>candies[i+1]:
                    #dont do anything, cond already satisfied
                    pass
                else:
                    candies[i]=candies[i+1]+1
                    
        return sum(candies)