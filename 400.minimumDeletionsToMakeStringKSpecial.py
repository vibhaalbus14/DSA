from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        #assuming one to be the base fre
        #max allowed values are [base,base+k]
        #anything less has to be deleted completely as we are allowed only to del but not add
        #anything greater than upper limit , extras have to be deleted

        counter=Counter(word)
        freqList=list(counter.values())
        n=len(freqList)

        def findDeletions(baseFreq):
            res=0
            for freq in freqList:
                if freq<baseFreq:
                    res+=freq
                elif freq>baseFreq+k:
                    res+=(freq-(baseFreq+k))
            return res
        
        ans=10**5+1

        for i in range(n):
            ans=min(ans,findDeletions(freqList[i]))
        return ans
        


        
        