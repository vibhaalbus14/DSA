from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #approach
        #1.maintain a monotonic stack
        #2.when curr bar height < top , pop till its >/=
        #3.index of adding curr val depends on how far its height is valid when traced towards left
        #4.append(index,val) into stack to calculate area

        maxArea=float("-inf")
        stack=[]

        for i,val in enumerate(heights):
            if not stack or val>=stack[-1][1]:
                stack.append((i,val))
            else:
                while  stack and val<stack[-1][1]:
                    prevIndex,prevVal=stack.pop()
                    #calc area
                    maxArea=max(maxArea,(i-prevIndex)*prevVal)
                stack.append((prevIndex,val))

        #left over bars in stack 
        #its width is calculated with len(heights)
        while stack:
            prevIndex,prevVal=stack.pop()
            maxArea=max(maxArea,(len(heights)-prevIndex)*prevVal)
        return maxArea