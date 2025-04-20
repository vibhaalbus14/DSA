from typing import List
class Solution:
    #approach
    #median will always give the min operations
    #if length is even, bth median vales give the same min operations
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        #directions=[(0,1),(0,-1),(1,0),(-1,0)]
        m=len(grid)
        n=len(grid[0])
        
        nums=[]
        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j])
        nums.sort()
        median=nums[len(nums)//2]
        changes=0

        for num in nums:
            diff=abs(median-num)
            if diff%x!=0:
                return -1
            else:

                changes+=(diff//x)
        return changes
                

        # def search(num):
        #     #make all the cells equal to num
        #     dq=deque()
        #     visited=set()
        #     dq.append((0,0))
        #     visited.add((0,0))
        #     changes=0

        #     while dq:
        #         r,c=dq.popleft()

        #         if grid[r][c]!=num:
        #             diff=abs(num-grid[r][c])
        #             if diff%x==0: #if we can reach the diff by adding or subtracting x =>attainable
        #                 changes+=(diff//x)
        #             else:
        #                 return -1
        #         #add the neighbouring cells
        #         for tr,tc in directions:
        #             nr=tr+r
        #             nc=tc+c

        #             if nr>=0 and nr<m and nc>=0 and nc<n and (nr,nc) not in visited:
        #                 visited.add((nr,nc))
        #                 dq.append((nr,nc))
            
        #     return changes
        
        # return search(median)

        



        