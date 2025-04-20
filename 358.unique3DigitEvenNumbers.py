from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        #only count, no need to create combs
        hashMap=Counter(digits)
        count=0
        def backtrack(place):
            nonlocal count
            if place==4:
                count+=1
                return
            
            for key,freq in hashMap.items():
                if (place==1 and key==0) or (place==3 and key%2!=0) or freq==0:#first place and zero=> not a 3 digit num
                    #last place but num is odd
                    #num not available as freq ==0
                    continue
                
                #fill out that place
                #reduce the freq

                hashMap[key]-=1
                backtrack(place+1)
                hashMap[key]+=1

        backtrack(1)
        return count
            

