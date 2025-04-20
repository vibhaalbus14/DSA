from typing import List
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        #approach
        #dp=> TC: O(N^2) and SC :O(N^2)
        #OPTIMAL=> GREEDY + BINARY SEARCH => TC :O(N) AND SC:O(1)

        #1.identify diff capabilities from 1 to max(nums) since capability ranges in this range
        #2.for evry capability, do a linear search in nums , checking whether
        #k nums can be chosen , that are non adjacent , and that can give this capability val
        #3.if yes, then reduce capability , if not increase capability


        def searchForCapability(cap):
            count=0
            i=0

            while i <len(nums):
                #count the curr num only if it is  than cap else , cap will change
                if nums[i]<=cap:
                    count+=1
                    #skip the adjacent house
                    i+=2
                else:
                    #if cap is more, ignore the current one
                    #since its not considered as counted, count remains the same
                    i+=1
            return  count>=k

        l=1
        r=max(nums)

        while l<=r:
            mid=(l+r)//2
            if searchForCapability(mid):
                #try to find min capability
                r=mid-1
            else:
                #inc capability
                l=mid+1
        
        return l

        
        
        