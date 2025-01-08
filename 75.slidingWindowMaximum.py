# #--------------------------brute force approach in sliding window--------------------------
# #time complexity:O(k*(n-k+1))
# #space complexity:O(n-k+1)
# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         finalList=[]
#         for i in range(len(nums)-k+1):
#             window=nums[i:i+k]
#             finalList.append(max(window))
#         return finalList
# obj=Solution()
# print(obj.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))

#--------------------------deque approach------------------------
#time complexity:O(n)=>elements are accessed at max once to add and remov from deque O(2n)
#space complexity:O(k)=>size of deque

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq=deque()
        finalList=[]
        for i in range(k): #first window
            while dq and nums[i]>=nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            #output the max element
        finalList.append(nums[dq[0]])
        
        #for further windows
        for i in range(k,len(nums)):
            #to check if the max element is still part of the window
            if dq and dq[0]==i-k: #element is not part of present window as i-k is eliminated index
                dq.popleft()
            while dq and nums[i]>=nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            finalList.append(nums[dq[0]])
        return finalList
obj=Solution()
print(obj.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
        
        


