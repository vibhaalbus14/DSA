from typing import List
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #lis approach
        #1.sort it according to width
        #2.apply lis on height
        #3.why not sort both? this doesnt lead to efficient sorting in terms of width or in terms of height
        envelopes.sort(key=lambda item:(item[0],-item[1]))#sort height in descending so that say [4,5],[4,6] and 4,6 doesnt fit into 4,5

        memo={}
        def helper(index,targetHeight):
            if index>=len(envelopes):
                return 0

            if (index,targetHeight) in memo:
                return memo[(index,targetHeight)]
            
            include=0
            if envelopes[index][1]>targetHeight:
                include=helper(index+1,envelopes[index][1])+1
            
            exclude=helper(index+1,targetHeight)
            memo[(index,targetHeight)]=max(include,exclude)
            return memo[(index,targetHeight)]
        
        maxCount=0
        for i in range(len(envelopes)):
            maxCount=max(maxCount,helper(i,float("-inf")))
        return maxCount

#--------------------approach:monotonic stack +binary search-------------------
from bisect import bisect_left
from typing import List
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #lis approach
        #1.sort it according to width
        #2.apply lis on height
        #3.why not sort both? this doesnt lead to efficient sorting in terms of width or in terms of height
        envelopes.sort(key=lambda item:(item[0],-item[1]))#sort height in descending so that say [4,5],[4,6] and 4,6 doesnt fit into 4,5

        height=[item[1] for item in envelopes]

        stack=[]
        for ht in height:
            #if ht>stack[-1],insert happily
            #if ht<=stack[-1],identify the insert position,i.e the smallest number such that
            #ht>=smallest number

            #1.all height has to be inserted
            #2.check the insert position, if its at the end,append to stack
            #3.else , rather than appending,replace ht to that insert position
            index=bisect_left(stack,ht)
            if index==len(stack):
                stack.append(ht)
            else:
                stack[index]=ht
        return len(stack)
        

        