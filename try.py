# # # from typing import List
# # # class Solution:
# # #     def subsets(self, nums: List[int]) -> List[List[int]]:
# # #         ans = []
# # #         def recursiveCall(l :List, i:int):
            
# # #             if i == len(nums)-1:
# # #                 yes = l.copy()
# # #                 yes.append(nums[i])
# # #                 no = l.copy()
# # #                 ans.append(yes)
# # #                 ans.append(no)
            
# # #             elif i > len(nums):
# # #                 pass
            
# # #             else:
# # #                 yes = l.copy()
# # #                 yes.append(nums[i])
# # #                 recursiveCall(yes, i+1)
# # #                 recursiveCall(l.copy(), i+1)
        
         
# # #         return ans
# # # start=0
# # # end=1
# # # print(f"{start}->{end}")
# # grid=[[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
# # n=8
# # prefixSum=[[-1 for _ in  range(n)]for _ in  range(n)]
# # for i in range(n):
# #     for j in range(n):
# #         if j==0:
# #             sum=grid[i][j]
# #         else:
        
# #             sum+=grid[i][j]
# #         prefixSum[i][j]=sum
# # #print(prefixSum)
# # # res=0
# # # for i in range(0,7+1):
# # #     res+=prefixSum[i][7]
# # # print(res)
# # # if (res==0) or (res==((7-0+1)*(7-0+1))):
# # #     print(True) #full of zeroes or ones
# # # else:
# # #     print(False)
# # # prefixSumParent=[[-1 for _ in  range(n)]for _ in  range(n)]
# # # for col in range(n):
# # #     for row in range(n):
# # #         if row==0:
# # #             sum=prefixSum[row][col]
# # #         else:
# # #             sum+=prefixSum[row][col]
# # #         prefixSumParent[row][col]=sum
# # # for list in grid:
# # #     print(list)
# # # print("---------------------------------------------")
# # # for list in prefixSum:
# # #     print(list)
# # # print("---------------------------------------------")
# # # for list in prefixSumParent:
# # #     print(list)
# # # #print(prefixSumParent)
# # # res=prefixSumParent[3][7]
# # # print(res)
# # # subList=[1,3,2]
# # # res=sorted(subList)

# # print(len(s))
# # print(len(words))
# words=["This", "is", "an", "example", "of", "text", "justification."]
# for word in words:
#     print(word,len(word))


# def helper(n):
#     fact=[1 for i in range(n+1)]
#     for i in range(2,n+1):
#         fact[i]=i*fact[i-1]
#     for i,num in enumerate(fact):
#         print(i,num)
#     return fact[n]
# print(helper(50))
# 
shifts=[3,5,9]
perfixSum=[0 for i in range(len(shifts)+1)]
print(128%26)
print((128%26)+97)