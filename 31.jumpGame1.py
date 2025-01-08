# def canJump(nums):
#     #write code here
#     n=len(nums)
#     curr_index=0
#     while(curr_index<n):
#         step_count=nums[curr_index]
#         prev_index=curr_index
#         curr_index+=step_count
#         if(curr_index>n-1):
#             return True
#         if(prev_index==curr_index):
#             return False

# print(canJump([1,3,4,1,1,2,1]))


#time complexity:O(n)
#space complexity:O(1)
#logic : identify the max possible reachable index  from every reachable index
def canJump(nums):
    n=len(nums)
    max_reach=0
    for index in range(n):
        #if given index is not reachable
        if index>max_reach:
            return False
        max_reach=max(max_reach,index+nums[index])

        if(max_reach>n-1):
            return True
print(canJump([2,3,1,0,0,0,0,0,2,1]))
    
