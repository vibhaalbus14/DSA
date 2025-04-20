from functools import lru_cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if finish < int(s):
            return 0

        for char in s:
            if int(char)>limit:
                return 0
        
        @lru_cache(None)
        def digitalDP(index,tight,identity):
            
            nonlocal currFinish
            if index>=len(currFinish)-len(s) :
                if not tight:
                    return 1
                diff=len(currFinish)-len(s)
                for i in range(len(s)):
                    if int(s[i])>currFinish[i+index]:
                        return 0
                    elif int(s[i])<currFinish[i+index]:
                        #ure free no need to check further
                        return 1
                return 1

            currTotal=0
            currLimit=min(currFinish[index],limit) if tight else limit

            for digit in range(currLimit+1):
                currTotal+=digitalDP(index+1,tight and (digit==currFinish[index]),identity)

            return currTotal

        currFinish=list(map(int,str(finish)))
        overall=digitalDP(0,True,1)
        if overall==0:
            return overall
        if start-1<int(s):
            left=0
        else:
            currFinish=list(map(int,str(start-1)))
            left=digitalDP(0,True,2)

        return overall-left