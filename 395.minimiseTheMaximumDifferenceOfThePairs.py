from typing import List
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        #approach
        #dp with index and pairs formed so far will give TC of O(n*p) which is almost n**2
        #next approach
        #1.binary search over the values
        #2.use every mid value as the threshold saying this can be the max ans if we find p pairs
        #3.so by going over all the values in nums, we find if p pairs are psooible with diff<=threshold
        #4.if yes, try to minimise the threshold since we have to minimize the the overall op
        #5.if we cant find 'p' pairs within th egiven threshold, we increase the threshold val and repeat
        #6. final threshold is the answer

        n=len(nums)

        def checkPairsWithGivenThreshold(threshold):
            #if we need to minimise the diff=> only adj values will help
            i,count=0,0
            
            while i<n-1:
                if abs(nums[i]-nums[i+1])<=threshold:
                    count+=1
                    i+=2 #since i and i+1 are already paired we move to i+2
                    if count==p:
                        return True
                else:
                    i+=1
            return False

        nums.sort()
        l=0 #dont initialse it to min(nums) as here we are trying identify threshold that can also be 0 and not nums[0] val
        r=nums[-1]-nums[0] #why? since max threshold can never be greater than max-min given in nums
        res=0
        
        while l<=r:
            mid=(l+r)//2

            #now mid val acts as threshold
            #see if p pairs are possible with this threshold
            if checkPairsWithGivenThreshold(mid):
                #try to minimise
                res=mid#initialise to res since valid pairs are found
                r=mid-1
                
            else:
                #try to maximise
                l=mid+1
                
        return res
