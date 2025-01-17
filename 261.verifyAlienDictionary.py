from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashMap={}
        for i,char in enumerate(order):
            hashMap[char]=i
        
        for i in range(len(words)-1):
            currW=words[i]
            nextW=words[i+1]

            currLength=len(currW)
            nextLength=len(nextW)
            flag=False
            for i in range(min(currLength,nextLength)):
                if currW[i]==nextW[i]:
                    pass
                elif hashMap[currW[i]]<hashMap[nextW[i]]:
                    #is a valid order
                    #since first diff is encountered, break
                    flag=True
                    break
                else:
                    return False
            if not flag:
                if currLength>nextLength:
                    return False
        return True