#time complexity:O(n)
#space complexity:O(n)
class Solution(object):
    def jump(self, nums):
        n=len(nums)
        memo={}
        def helper(index):
            if(index>=n-1):
                return 0 # no jumps necessary
            
            elif index in memo:
                return memo[index]

            else:
                max_jump=nums[index]
                min_steps=float('inf')
                for i in range(1,max_jump+1):#options availabe
                   next_index=index+i
                   step=helper(next_index)

                   if next_index<n:
                        min_steps=min(min_steps,step+1)

            memo[index]=min_steps
                
            return memo[index]
        return helper(0)
object=Solution()
print(object.jump([2,3,1,1,4]))
