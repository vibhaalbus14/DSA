from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        overlappingIntervals=[]
        for start,end in ranges:
            if not((left<start and right<start)or (left>end and right>end)):
                #they overlap
                for i in range(max(start,left),(min(end,right))+1):
                    if i not in overlappingIntervals:   
                        overlappingIntervals.append(i)

        
       
        if len(overlappingIntervals)==(right-left+1):
            return True
        else:
            return False
        
        