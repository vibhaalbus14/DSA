from collections import deque
class Solution(object):
    def minSubArrayLen(self, target, nums):
        sum=left=right=length=0
        subArray=deque()
        minLength=float('inf')

        while right<len(nums):
            sum+=nums[right]
            subArray.append(nums[right])
            length+=1


            if sum>=target:
                while left<=right and sum>=target:
                    minLength=min(length,minLength)
                    print(subArray)
                    subArray.popleft()
                    sum-=nums[left]
                    length-=1
                    left+=1
            right+=1

        if minLength==float('inf'):
            return 0
        else:
            return minLength
obj=Solution()
print(obj.minSubArrayLen(7,[2,3,1,2,4,3]))