from typing import List
from functools import lru_cache
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        #recursion, memoization
        operators={"+","-","*"}


        n=len(expression)

        @lru_cache(None)
        def helper(start,end):
            
            temp=expression[start:end+1]
            if temp.isdigit():
                return [int(temp)]
            
            res=[]
            for j in range(start,end+1):
                if expression[j] in operators:
                    left=helper(start,j-1)
                    right=helper(j+1,end)
                    #print(left,right)
                    for l in left:
                        for r in right:
                            res.append(eval(str(l) + expression[j] +str(r))) 
            return res
            
        return helper(0,n-1)



            
