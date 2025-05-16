from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        hashMap=defaultdict(set)
        n=len(words)

        for i in range(n):
            for j in range(i+1,n):
                if groups[i]!=groups[j] and len(words[i])==len(words[j]):
                    diff=0
                    for k in range(len(words[i])):
                        if words[i][k]!=words[j][k]:
                            diff+=1
                        if diff>1:
                            break
                    if diff==1:
                        hashMap[i].add(j)
                        hashMap[j].add(i)
        
        #dp cache
        @lru_cache(None)
        def helper(index,prev): #index is the currIndex and prev=prev chosen index
            if index>=n:
                return []
            include=[]
            exclude=[]
            if prev==None:
                include.append(words[index])
                include.extend(helper(index+1,index))
            elif groups[index]!=groups[prev] and index in hashMap[prev]:
                #Add the current word and call next
                include.append(words[index])
                include.extend(helper(index+1,index))
            exclude.extend(helper(index+1,prev))

            return max(include,exclude,key=len)
        return helper(0,None)
        
