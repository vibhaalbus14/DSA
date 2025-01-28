from typng import List
from collections import lru_cache

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        #"""""occurences dont matter"""""""""""
        #sorting helps to delete next and prev num


        hashMap=Counter(nums) #num, occurence
        numsNew=list(hashMap.keys())
        numsNew.sort()
        
        @lru_cache
        def helper(index):
            if index>=len(numsNew):
                return 0
            #not choosing this
            exclude=helper(index+1)
            #choose this
            include=numsNew[index]*hashMap[numsNew[index]]
            if index+1<len(numsNew):
                if numsNew[index+1]==numsNew[index]+1:
                
                    include=numsNew[index]*hashMap[numsNew[index]]+helper(index+2)
                else:
                    include=numsNew[index]*hashMap[numsNew[index]]+helper(index+1)

            #index +2 so that we delete the immediate next one
            #no need to worry about num-1 since its never considered
            return max(include,exclude)
        return helper(0)
        