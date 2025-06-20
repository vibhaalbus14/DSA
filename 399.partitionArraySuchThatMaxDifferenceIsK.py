from typing import List
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        #greedy approach, sort and use
        #why not dp?
        #beacuse dp tends to exclude certain elements,can cause duplication.This will vioate the fact that every element must be present exactly once.Plus, even if dp was possible, for every subseq, min and max needs t be stored and too many args in function and its possible to count the elements in subseq but not no of subseq that increases time comp
        #why order of sub doesnt matter?
        #1.beacuse thers no other stack greedy way to do
        #2.beacuse evn if we choose a larger index and then a smaller index, we are not interested in the order we choose elemenst but interested in no of subseq that can be formed=> not in construction of subseq but identifying num of subseq
        
        n=len(nums)
        count=1
        
        nums.sort()
        min_,max_=nums[0],nums[0]

        for i in range(n):
            
            if nums[i]>max_ :
                if nums[i]-min_<=k:
                    max_=nums[i]
                else:
                    min_ ,max_=nums[i],nums[i]
                    count+=1
            
        return count


