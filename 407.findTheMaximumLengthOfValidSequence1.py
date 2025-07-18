from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        #x%2 give 0 or 1
        #=> sum of 2 nums positive or neg
        #=> choose positive sum or choose neg sums, do both

        #=> if odd=> a num must be div and not div=> vice vers
        #=> if even => all the nums must be either div or not div

        #run 3 greedy runs
        #1.to capture vice versa
        #2.to capture all are div by 2
        #3.to capture all are not div by 
        

        maxLength=0

        def viceVersa(flagVal):
            isDiv=flagVal
            currLength=0
            for num in nums:
                if num%2==0 and isDiv==False:
                    #works
                    isDiv=True
                    currLength+=1
                elif num%2!=0 and isDiv==True:
                    isDiv=False
                    currLength+=1
            return currLength

        def allSimilar(flagVal):
            isDiv=flagVal
            currLength=0
            for num in nums:
                if num%2==isDiv:
                    currLength+=1
            return currLength
        
        maxLength=max(viceVersa(True),viceVersa(False),allSimilar(1),allSimilar(0),maxLength)

        return maxLength










        