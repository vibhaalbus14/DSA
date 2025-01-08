#----------------------approach 2: TLE exceeds because of index() and max() calculations--------
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        #2 pointers approach
        l=0
        r=l+1
        count=0
        maxValue=float('-inf')
        while r<len(height) and l<=r:
            if height[l]==0: #min=0=>cannot store=>no use
                l+=1
                r=l+1
                continue
            if height[r]<height[l]:
                while r<len(height) and height[r]<height[l]:
                    r+=1
                if r==len(height):
                    #nothing greater than or equal to current l found,
                    #find next greater maxValue from ht[l+1:] and its index
                    maxValue=max(height[l+1:])
                    maxIndex=height.index(maxValue,l+1)#firstOccurence
                    #update count
                    for i in range(l+1,maxIndex):
                        count+=maxValue-height[i]
                    l=maxIndex
                    r=l+1
                    
            else: #height[r]>=height[l]:
                minVal=height[l]
                l+=1
                while l<r:
                    count+=minVal-height[l]
                    l+=1
                r=l+1
        return count
            
#---------------------------------approach 2---------------------------------------------
class Solution:
    def trap(self, height: List[int]) -> int:
        #2 ptr approach
        #position l and r pointers to the extremes
        #the one that is larger =>helpers to hold water
        #the one that is smaller=> decides the quantity of water to hold
        l,r=0,len(height)-1
        leftMax=0
        rightMax=0
        count=0
        while l<r:
            #compare which supports
            if height[l]<height[r]:#=> l decides quantity and right supports
                if height[l]>=leftMax:
                    leftMax=height[l]
                else:
                    count+=leftMax-height[l]
                l+=1
            else:
                if height[r]>=rightMax:
                    rightMax=height[r]
                else:
                    count+=rightMax-height[r]
                r-=1
        return count


        