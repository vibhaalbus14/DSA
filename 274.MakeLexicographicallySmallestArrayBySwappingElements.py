from typing import List
from collections import deque
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        #1.sort the numbers
        #2.store them in groups such that the limit difference is obeyed and map num to grp
        #3.popleft from grp every time u encounter a number in nums

        groups=[]
        numToGroupMap={}

        sortedNums=sorted(nums)

        for num in sortedNums:
            if not groups or abs(groups[-1][-1]-num)>limit:
                groups.append(deque())
                #create a new group
            groups[-1].append(num)
            numToGroupMap[num]=len(groups)-1
            #map num to its group, easier lookup
        
        #do the swap
        for i in range(len(nums)):
            num=nums[i]

            #get the group
            currGrp=numToGroupMap[num]

            nums[i]=groups[currGrp].popleft()
        return nums
            