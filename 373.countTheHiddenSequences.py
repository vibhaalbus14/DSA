from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        #approach
        #1.identify how low and how high a value in nums can go with given diff
        #2.start with 0 and build cumulative diff sum
        #why? because lets say nums[0]=x=> some start number
        #3.then nums[1]-nums[0]=diff[0]
        #=> nums[1]=nums[0]+diff[0]
        #=> nums[2]=nums[1]+diff[1]+diff[0] .. mathematical induction
        #4.=> x+minVal>=lower and x+maxVal>=upper
        #5.=> valid range [lower-minVal,upper-maxVal]
        #6.count= (upper-lower)-(maxVal-minVal)+1

        a,minVal,maxVal=0,0,0
        for diff in differences:
            a+=diff
            minVal=min(a,minVal)
            maxVal=max(a,maxVal)
        
        
        count= (upper-lower)-(maxVal-minVal)+1 
        return  0 if count< 0 else count
        