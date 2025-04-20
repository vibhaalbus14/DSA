#time complexity:O(logn)
#space complexity:O(n)

class Solution(object):
    def search(self, nums, target):
        #to check if target element exists
        res=0
        pivotIndex=-1
        #since the list is sorted, the point where this mishaps is the pivot index
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                pivotIndex=i-1
                break
       
        if pivotIndex==-1:
            pivotIndex=0
            numsOriginal=nums
        else:
            numsOriginal=nums[pivotIndex+1:]+nums[:pivotIndex+1]
        
         #creating a hast table key: value where key=num and value=index of num in nums
        ht={}
        for i,num in enumerate(nums):
            if num not in ht:
                ht[num]=i
        #binary search
        def binarySearch(start,end,numsOriginal):
            if (start>end):
                return -1
            else:
                mid=(start+end)//2
                if numsOriginal[mid]==target:
                    return ht[numsOriginal[mid]]
                elif target<numsOriginal[mid]:
                    return binarySearch(start,mid-1,numsOriginal)
                else:
                    return binarySearch(mid+1,end,numsOriginal)
        return binarySearch(0,len(numsOriginal)-1,numsOriginal)

obj=Solution()
print(obj.search([1,3],3))


        # for i,num in enumerate(nums):
        #     if num==target:
        #         count=1
        #         altIndex=i
        #         break
        # if count==1:
        #     return altIndex
        # else:
        #     return -1
        #-------------to find the position of target in original nums------------------
        # if count==1:
        #     if altIndex>pivotIndex:
        #         return altIndex-pivotIndex-1
        #     else:
        #         return altIndex+pivotIndex
        # else:
        #     return -1 #target doesnt exist

#----------------------------------approach-------------------------------------------------
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #first identify the miniumum elements's index
        #then mark boundaries
        #then do binary search
        n=len(nums)

        def binarySearch():
            l=0
            r=n-1
            while l<=r:
                mid=(l+r)//2
                if (mid==0 or nums[mid]<nums[mid-1]) and (mid==n-1 or nums[mid]<nums[mid+1]):
                    return mid
                elif nums[mid]<nums[r]:#search on left side
                    r=mid-1
                elif nums[mid]>nums[r]:#search on right side
                    l=mid+1      

        def binarySearchRegular(l,r):
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return -1

        if n!=1:
            start=binarySearch()
            end=start-1 
            if end<0:
                end=0
        else:
            start,end=0,0

        if start==end:#sorted array
            return binarySearchRegular(0,n-1)
        if target>=nums[0] and target<=nums[end]:
            #search right half
            return binarySearchRegular(0,end)
        if target<=nums[n-1] and target>=nums[start]:
            #search left half
            return binarySearchRegular(start,n-1)
        else:
            return -1


#-------------------------------optimal code TC:O(n)-----------------------------------------------
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #approach
        #1.identify the rotated index=> index of the samllest number
        #2.loop over regualr array but map the indices to rotated array

        n=len(nums)
        if n==1:
            return 0 if target in nums else -1
        l=0
        r=n-1
        rotIndex=None

        while l<=r:
            mid=(l+r)//2
            
            if nums[mid]<nums[mid-1]:
                rotIndex=mid
                break
            if nums[mid]<nums[-1]:
                #go towards left
                r=mid-1
            else:
                #towards right
                l=mid+1
        
        #loop over regular array, but map the indices to rotated array
        l=0
        r=n-1

        while l<=r:
            mid=(l+r)//2
            rotated_mid=(mid+rotIndex)%n

            #check in rotated array
            if nums[rotated_mid]==target:
                return rotated_mid
            if nums[rotated_mid]<target:
                l=mid+1 #make changes wrt to the regualr sorted array
            else:
                r=mid-1
        return -1

        

        