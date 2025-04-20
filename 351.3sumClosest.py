#tc: O(n^2)

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n=len(nums)
        diff=float("inf")
        closestSum=None

        for i in range(n):
            l=i+1
            r=n-1
            while l<r:
                currSum=nums[i]+nums[l]+nums[r]
                if abs(currSum-target)<diff:
                        diff=abs(currSum-target)
                        closestSum=currSum
                if currSum<=target:
                    l+=1
                else:
                    r-=1
                
        return closestSum
    
#-----------------------------------------------------------------------
#TC :O(n**2 log n)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        diff=float("inf")
        closestSum=None

        for i in range(n-2):
            for j in range(i+1,n-1):
                #binary search here
                l=j+1
                r=n-1

                while l<=r:
                    mid=(l+r)//2

                    if abs((nums[mid]+nums[i]+nums[j])-target)<diff:
                            diff=abs((nums[mid]+nums[i]+nums[j])-target)
                            closestSum=nums[mid]+nums[i]+nums[j]
                    if nums[mid]+nums[i]+nums[j]<=target:
                        
                        l=mid+1
                    else:
                        r=mid-1
                
        return closestSum

        

        