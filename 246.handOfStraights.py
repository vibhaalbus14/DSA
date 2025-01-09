from typing import List
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            #groups of given size cannot be formed
            return False
        
        hand.sort()
        counterHand=Counter(hand)

        while counterHand:
            k=0
            for key,val in counterHand.items():
                val=key
                break
            
            while True:
                #present one
                if counterHand[val]==1:
                    del counterHand[val]
                else:
                    counterHand[val]-=1
                #check for next one only if group size is less
                if k<groupSize-1:
                    if val+1 in counterHand:
                        val=val+1
                        k=k+1
                    else:
                        return False
                else:
                    break
                       
        return True
        

obj=Solution()
print(obj.isNStraightHand([1,2,3,6,2,3,4,7,8],3))
print(obj.isNStraightHand([1,2,3,4,5],4))