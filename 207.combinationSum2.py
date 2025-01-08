from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #backtracking
        #early pruning.how?
        #1.by checking if required sum is already greater than target
        #2.looping over and checking for dups
        res=[]
        n=len(candidates)
        candidates=sorted(candidates)

        def helper(index,subList,sum):
            #base case
            nonlocal res
            if sum==target:
                res.append(subList[:])#cant proceed since values>=1
                return
            
            if index>=n or sum>target:
                return
            #exclude step
            for i in range(index+1,n):
                if candidates[i]<=(target-sum):
                    if candidates[i-1]!=candidates[i]:                    
                        helper(i,subList,sum)
                        break
                else:
                    break
            
            #include
            subList.append(candidates[index])
            if candidates[index]<=target-sum:
                sum+=candidates[index]
                #subList+[candidates[index]]
                helper(index+1,subList,sum)
                #backtrack step
                sum-=candidates[index]
            subList.pop()
            
        helper(0,[],0)
        return res


            

