from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #fix one,two, three , choose 4th one by doing 
        #4th=target-1st-2nd-3rd
        #return all nums

        res=[]
        n=len(nums)
        nums.sort()
        for i in range(n-3):
            for j in range(i+1,n-2):
                # for k in range(j+1,n):
                #     req=target-nums[i]-nums[j]-nums[k]
                #     if req in nums[k+1:]:
                #         if [nums[i],nums[j],nums[k],req] not in res:
                #             res.append([nums[i],nums[j],nums[k],req])


                #implement 2 sums here
                twoSum=nums[i]+nums[j]
                l=j+1
                r=len(nums)-1
                while l<r:
                    currSum=twoSum+nums[l]+nums[r]
                    if currSum>target:
                        r-=1
                    elif currSum<target:
                        l+=1
                    else:
                        #equal
                        if [nums[i],nums[j],nums[l],nums[r]] not in res:
                            res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1


        return res