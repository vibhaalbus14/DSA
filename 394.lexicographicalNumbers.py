from functools import cmp_to_key
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def cmp_order(a,b):
            if str(a)<str(b):
                return -1
            elif str(a)<str(b):
                return 1
            else:
                return 0

        stack=[]
        for i in range(1,n+1):
            stack.append(i)
        stack.sort(key=cmp_to_key(cmp_order))
        return stack
