from typing import List
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        head=None
        n=len(grid)
        prefixSum=[[-1 for _ in  range(n)]for _ in  range(n)]
        for i in range(n):
            for j in range(n):
                if j==0:
                    sum=grid[i][j]
                else:
                    sum+=grid[i][j]
                prefixSum[i][j]=sum


        def checkGrid(sr,er,sc,ec):
            # #iterating through each and every cell in the grid isnt optimal
            # #use dp
            # val=grid[sr][sc]
            # memo={}
            # def dfs(sr,sc):
            #     nonlocal val,er,ec,n,memo
            #     if sr>er or sc>ec or sr not in range(n) or sc not in range(n):
            #         return True
            #     if (sr,sc) in memo:
            #         return memo[(sr,sc)]
            #     #check if all values in the square are the same
            #     if grid[sr][sc]==val:
            #         #check its neighbours
            #         #right,bottom,diagonal
            #         memo[(sr,sc)]= dfs(sr,sc+1) and dfs(sr+1,sc) and dfs(sr+1,sc+1)
            #     else:
            #         memo[(sr,sc)]= False
                
            #     return memo[(sr,sc)]
            # return dfs(sr,sc)
                
            val=prefixSum[sr][ec]
            for i in range(sr,er+1):
                if prefixSum[i][ec]!=val:
                    return False

        def helper(sr,er,sc,ec):
            nonlocal head
            if checkGrid(sr,er,sc,ec):
                newNode=Node(grid[sr][sc],True,None,None,None,None)
            else:
                newNode=Node(grid[sr][sc],
                            False,
                            helper(sr,(er//2),sc,(ec//2)),
                            helper(sr,(er//2),(ec//2)+1,ec),
                            helper((er//2)+1,er,sc,(ec//2)),
                            helper((er//2)+1,er,(ec//2)+1,ec))
                
            if not head:
                head=newNode
                return head
            else:
                return newNode

                
        return helper(0,n-1,0,n-1)


        