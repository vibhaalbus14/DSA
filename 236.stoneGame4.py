from functools import lru_cache
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache
        def helper(i):
            if i==0:
                return float("-inf")

            maxVal=float("-inf")
            #for x in range(i,0,-1):
            for x in range(1,i+1):
                #checkNum1=math.sqrt(x)
                #if x==(int(checkNum1)*int(checkNum1)):
                if x*x>i: #very imp step, to break unnecesssary looping
                    break
                stonesTaken=x*x
                # print(x)
                # print(int(checkNum1)*int(checkNum1))
                # print(int(checkNum1))
                maxVal=max(maxVal,stonesTaken-helper(i-stonesTaken))
                

            return maxVal
                
        scoreDifference=helper(n)
        #print(scoreDifference)
        if scoreDifference>0:
            return True
        else:
            return False
