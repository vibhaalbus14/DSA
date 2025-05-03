class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        uniqueTop=set(tops)
        uniqueBottom=set(bottoms)

        minSwaps=float("inf")

        #loop over to make all the elements equal to uniquetop Element
        for match in uniqueTop:
            currCount=0
            isBreak=False
            for i,val in enumerate(tops):
                if val==match:
                    continue
                else:
                    if bottoms[i]!=match:
                        isBreak=True
                        break
                    else:
                        currCount+=1
                if currCount>minSwaps:
                    isBreak=True
                    break
            if not isBreak:
                minSwaps=min(minSwaps,currCount)
        

        #check for bottom dominoes
        for match in uniqueBottom:
            currCount=0
            isBreak=False
            for i,val in enumerate(bottoms):
                if val==match:
                    continue
                else:
                    if tops[i]!=match:
                        isBreak=True
                        break
                    else:
                        currCount+=1
                if currCount>minSwaps:
                    isBreak=True
                    break
            if not isBreak:
                minSwaps=min(minSwaps,currCount)
        
        return -1 if minSwaps==float("inf") else minSwaps
            
