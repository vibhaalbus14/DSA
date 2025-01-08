#time and space complexity same as 0/1 knapsack
from typing import List
def outer(n:int,W:int,values:List[int],weights:List[int])->int:
    def helper(index,rem_wt):
        #base_case
        if(index>=n or rem_wt==0):
            return 0
        else:
           
            exclude=helper(index+1,rem_wt)
            include=0
            if(weights[index]<=rem_wt):
                include=values[index]+helper(index,rem_wt-weights[index])
            return max(include,exclude)
    return helper(0,W)
print(outer(3,8,[2,3,9],[8,2,5]))