from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[]
        total=0

        for i,num in enumerate(arr):
            
            while stack and num<stack[-1][1]:
                prevIndex,prevVal=stack.pop()
                #back ward extension
                #since the stack is in inc order, the stopping index to pooped num is the next prev index itself
                #this is stopped by previous smaller element
                left=prevIndex-(stack[-1][0] if stack else -1)
                #forward extension
                #how far an element can command ahead
                #this is stopped by next smaller element
                right=i-prevIndex
                total+=prevVal*left*right
            stack.append((i,num))
        
        while stack :
            prevIndex,prevVal=stack.pop()
            left=prevIndex-(stack[-1][0] if stack else -1)
            right=len(arr)-prevIndex
            total+=prevVal*left*right
        
        return total%(10**9+7)
        
