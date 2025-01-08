from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #approach
        #1.comare the values and form a stack
        #2.compare the stack using 2 ptrs
        #3.return maxLength+1

        stack=[]
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                stack.append(">")
            elif arr[i-1]<arr[i]:
                stack.append("<")
            else:
                stack.append("=")
        
        maxLength=0
        length=1
        l=0
        r=l+1
        while l<=r and r<len(stack):
            #sliding window here
            if stack[l]!=stack[r] and stack[l]!="=" and stack[r]!="=":
                length+=1
                maxLength=max(length,maxLength)
            else:
                length=1
            l=r
            r=r+1
        return maxLength+1


