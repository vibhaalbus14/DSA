from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        #approach
        # iterative dp
        #1.start from top-left
        #2.check if this cell can be part of any square and act as 
        #bottom right of the square its part of
        #3.for this the curr cell must be 1, and then top,left,and diagonal must be checked
        
        rows=len(matrix)
        cols=len(matrix[0])
        dp=[[0]*cols for _ in range(rows)]
        res=0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    dp[i][j]=0
                else:
                    #check if i/j is in first row/col
                    #if yes, then it is not part of any square
                    #since its the beginning line
                    if i==0 or j==0:
                        dp[i][j]=1
                        
                    else:
                        dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                        #diagonal,top,left
                    res+=dp[i][j]
        
        return res
            

