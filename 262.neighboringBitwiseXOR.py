from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        #der[i]=ori[i] xor ori[i+1]
        #=> ori[i+1]=ori[i]^der[i]
        #use this to identify the next element of original array
        #choose ori[0] to be 0/1,
        #if in the end i.e n-1, if we get the computed ==chosen=>its posiible to construct

        def validate(start):
            curr=start
            for num in derived:
                nextVal=curr^num
                curr=nextVal
            return curr==start
                
            
        
        return validate(0) or validate(1)