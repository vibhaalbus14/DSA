# #time complexity:O(2^n)
# #space complexity:O(n)
# def outer(cost):
#     def climbFrom(index):
#         if(index>len(cost)-1):
#             return 0
#         onestep=cost[index]+climbFrom(index+1)
#         twostep=cost[index]+climbFrom(index+2)

#         return min(onestep,twostep)
#     return min(climbFrom(0),climbFrom(1))
# print(outer([1,2,3]))
    

# #------------memoization----------------------------
# #time complexity:O(n)
# #space complexity:O(n)
# def outer(cost):
#     ht={}
#     n=len(cost)-1
#     def climbFrom(index):
#         if(index>n):
#             return 0
#         else:
#             if index in ht:
#                 return ht[index]
#             else:
#                 oneStep=cost[index]+climbFrom(index+1)
#                 twoStep=cost[index]+climbFrom(index+2)
#                 ht[index]=min(oneStep,twoStep)
#                 return ht[index]
#     return min(climbFrom(0),climbFrom(1))
# print(outer([1,2,3]))
#-------------tabulation------------
def outer(cost):
    n=len(cost)
    dp=[0]*(n+1)
    for i in range(2,n+1):
        dp[i]=min((cost[i-1]+dp[i-1]),(cost[i-2]+dp[i-2]))
    return dp[n]
print(outer([1,2,1,3,4,2,1,1]))


