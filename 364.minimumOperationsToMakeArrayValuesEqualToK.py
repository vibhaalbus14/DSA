from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        #invalid case
        #since elements that are greater can only be bought down and not the other way
        if min(nums)<k:
            return -1
        
        #choose second greatest element as curr
        #make all elements greater than this to be curr
        #continue to do so till target is reached
        setNums=set(nums)#remove duplicates
        setNums.add(k)
        #can sort also but doesnt matter
        #all nums become curr except the largets element
        #so the ans is length-1
       
        return len(setNums)-1 #because we start equalizing from last but oneth num
        

        