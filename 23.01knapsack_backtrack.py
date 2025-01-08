#time complexity:O(2^n)
#space complexity:O(n)
from typing import List
def outer(n:int,W:int,values:List[int],weights:List[int])->int:
    res=[]
    profit=0
    weights_added=[]
    def recFunc(i,profit):
        if i>=n:
            res.append(profit)
        else:
            recFunc(i+1,profit)
            weights_added.append(weights[i])
            if(sum(weights_added)<W):
                profit+=values[i]
                recFunc(i+1,profit)
                profit-=values[i]
            weights_added.pop()
    recFunc(0,profit)
    return max(res)
print(outer(3,8,[2,3,9],[8,2,5]))
            

            

            
        
