from typing import List
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        subsetHashmap={}
        for word in words2:
            currHashmap={}
            for char in word:
                    if char not in currHashmap:
                        currHashmap[char]=1
                    else:
                        currHashmap[char]+=1
            for key,val in currHashmap.items():
                if key not in subsetHashmap:
                    subsetHashmap[key]=val
                else:
                    subsetHashmap[key]=max(subsetHashmap[key],val)

        #print("subsetHash",subsetHashmap)
        res=[]
        
        for word in words1:
            copySubset=subsetHashmap.copy()
            #print("start",copySubset)
            for char in word:
                if char in copySubset:
                    if copySubset[char]>1:
                        copySubset[char]-=1
                    else:
                        del copySubset[char]
                    #print("inside",copySubset)

            if not copySubset:
                res.append(word)
        
        return res



# print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"],["l","e"]))

# print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"],["lo","eo"]))
print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"],["e","oo"]))