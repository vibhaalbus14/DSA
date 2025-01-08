class Solution(object):
    def findDuplicate(self, nums):
        #Floyd's Hare-Tortoise approach
        #implement the array as linked list
        #here, the elements in array are treated as indices
        #eg:       [1,3,4,2,2]
        #indices    0 1 2 3 4
        #ll formed:0->1->3->2->4 (4 pointing to prev 2)
        #                   |--|
        fast,slow=0,0
        #cycle detection
        while True:
            fast=nums[nums[fast]]
            slow=nums[slow]
        #cycle head detection
            if slow==fast:
                ptr=0
                while ptr!=slow:
                    ptr=nums[ptr]
                    slow=nums[slow]
                return ptr
    
obj = Solution()
print(obj.findDuplicate([18,13,14,17,9,19,7,17,4,6,17,5,11,10,2,15,8,12,16,17]))
# nums_updated = set(nums)

# return (sum(nums) - sum(nums_updated)) / (len(nums) - len(nums_updated))