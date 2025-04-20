from typing import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        #approach
        #1.everytime a char is included, increment count
        #2.no need to pass hashMap, because we are looking at one branch at a time, unlike include, exclude
        
        hashMap=Counter(tiles)

        def backtrack():
            count=0
            for key,val in hashMap.items():
                if val>0:
                    hashMap[key]-=1
                    count+=1
                    count+=backtrack()
                    hashMap[key]+=1
            return count
        return backtrack()


