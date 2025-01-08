#time complexity:O(2^n)
#space complexity:O(n)
# from typing import List
# def outer(n:int,W:int,values:List[int],weights:List[int])->int:
#     def helper(index,rem_wt):
#         #base_case
#         if(index>=n or rem_wt==0):
#             return 0
#         else:
#             exclude=helper(index+1,rem_wt)
#             include=0
#             if(weights[index]<=rem_wt):
#                 include=values[index]+helper(index+1,rem_wt-weights[index])
#             return max(include,exclude)
#     return helper(0,W)
# print(outer(3,8,[2,3,9],[8,2,5]))

# #--------------------memoization-------------------------
# from typing import List
# def outer(n:int,W:int,values:List[int],weights:List[int])->int:
#     ht={}
#     def helper(index,rem_wt):
#         #base_case
#         if(index>=n or rem_wt==0):
#             return 0
#         else:
#             if index in ht:
#                 return ht[index]
#             else:
#                 exclude=helper(index+1,rem_wt)
#                 include=0
#                 if(weights[index]<=rem_wt):
#                     include=values[index]+helper(index+1,rem_wt-weights[index])
#                 ht[index]=max(include,exclude)
#                 return ht[index]
#     return helper(0,W)
# print(outer(3,8,[2,3,9],[8,2,5]))
'''note:this approach wouldnot work since 2 value depends on 2 parameters,rem_et and index.Hence just seraching 
for particular index wont solve , but the search should be ht[index][rem_wt] rather than ht[index].\
hence memoization will include a 2d array rather than a list or hashmap
'''
#time complexity:O(nxw)
#space complexity:O(nxw)
# from typing import List
# def outer(n:int,W:int,values:List[int],weights:List[int])->int:
#     dp_table=[[-1]*(W+1) for _ in range(n)]#w+1 because in the table it is 0 to W and not from 1 to W
#     def helper(index,rem_wt):
#         #base_case
#         if(index>=n or rem_wt==0):
#             return 0
#         else:
#             if dp_table[index][rem_wt]!=-1:
#                 return dp_table[index][rem_wt]
#             else:
#                 exclude=helper(index+1,rem_wt)
#                 include=0
#                 if(weights[index]<=rem_wt):
#                     include=values[index]+helper(index+1,rem_wt-weights[index])
#                 dp_table[index][rem_wt]=max(include,exclude)
#                 return dp_table[index][rem_wt]
#     return helper(0,W)
# print(outer(3,8,[2,3,9],[8,2,5]))

#-------------------------------------tabulation----------------
#time complexity:O(nxw)
#space complexity:O(nxw)
# def knapSack(W,n,wt,val):
#     dp=[[0]*(W+1) for _ in range(n+1)]
#     for i in range(1,n+1):#items lists
#         for j in range(1,W+1):#the remaining weight in knapsack
#             include=0
#             if(wt[i-1]<=j):
#                 include=val[i-1]+dp[i-1][j-wt[i-1]]
#             exclude=dp[i-1][j]
#             dp[i][j]=max(include,exclude)
#     return dp[n][W]
# print(knapSack(8,3,[8,2,5],[2,3,9]))
#--------------------Space Optimised Tabulation---------------
#time complexity:O(nxw)
#space complexity:O(w)
def knapSack(W,n,wt,val):
    prev=[0]*(W+1)
    curr=[0]*(W+1)
    for i in range(1,n+1):#items lists
        for j in range(1,W+1):#the remaining weight in knapsack
            include=0
            if(wt[i-1]<=j):
                include=val[i-1]+prev[j-wt[i-1]]
            exclude=prev[j]
            curr[j]=max(include,exclude)
            prev=curr[:]
    return curr[W]
print(knapSack(8,3,[8,2,5],[2,3,9]))

