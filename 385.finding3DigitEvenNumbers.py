from typing import List
from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res=[]
        hashMap=Counter(digits)
        sortedUniqueNum=list(hashMap.keys())
        sortedUniqueNum.sort()

        
        def backtrack(currSum, pos):
            nonlocal res,hashMap,sortedUniqueNum
            if pos==3 : #selective numbers
                for key in sortedUniqueNum:
                    if key%2==0 and hashMap[key]>=1:
                        #(currSum)
                        res.append(currSum*10+key)
                        #("res",res)
                        #(currSum*10+key)
                        #()
                return        

            #no restrictions
            for key in sortedUniqueNum:
                if pos==1 and key==0:
                    continue
                if hashMap[key]>=1:
                    hashMap[key]-=1
                    backtrack(currSum*10+key,pos+1)
                    hashMap[key]+=1
        backtrack(0,1)
        return res
                
            

            