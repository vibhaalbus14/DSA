from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #approach
        #1.maintain a dec monotonic stack to store i,jth values
        #2.if the currVal is greater than top of stack => pop
        #3.if the curr val is lesser than top (k<j) and greater than its min Val (k>i) => ret true
        #4.if the curr Val is lesser than top and lesser rthan minVal => append to stack
        #5.min val is kept track such that ,in (num,minVal) present in stack, num=>j and minVal=>i
        #encountered number=k

        stack=[] #(num,its minVal)
        minNum=float("inf")
        
        for currNum in nums:
            while stack and currNum>=stack[-1][0]:
                stack.pop()#violates the cond where j>k
            
            if stack and  currNum<stack[-1][0]  and currNum>stack[-1][1]:
                return True
            #continue to add into stack
            stack.append((currNum,minNum))
            minNum=min(currNum,minNum)
        return False