#time comp:O(mxn*mxn)
#space comp:O(mxn)
from typing import List
from functools import lru_cache
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        if m==1 and n==1 and matrix[m-1][n-1]=='1':
            return 1
        
        def checkMatrix(baseR,baseC,r,c):
            for i in range(baseR,r+1):
                for j in range(baseC,c+1):
                    if matrix[i][j]=='0':
                        return False
            return True

        @lru_cache
        def helper(baseR,baseC,r,c):

            if matrix[r][c]=='0':
                return 0

            if not checkMatrix(baseR,baseC,r,c):
                return 0

            if r>=m and c>=n:
                return 0

            currArea=0
            if r-baseR==c-baseC :
                rows=r-baseR+1
                cols=c-baseC+1
                currArea=cols*rows
                
            
            right=0
            bottom=0
            #consider right and bottom neighbour
            if r in range(m) and c+1 in range(n) :
                right=helper(baseR,baseC,r,c+1)
            if r+1 in range(m) and c in range(n):
                bottom=helper(baseR,baseC,r+1,c)
            
            return max(right,bottom,currArea)

        maxArea=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]!='0':
                    maxArea=max(maxArea,helper(i,j,i,j))
        return maxArea
        
#------------------------approach 2-----------------------------------------------------------
#time comp:O(mxn)
#space comp:O(mxn)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #approach
        #1.evry cell is a part of a square
        #2.this square keeps increasing in diensions
        #3.what constructs a square is if its left, bottom and bottom-left are 1's
        #4.we find that the problems are overallping=>dp

        m=len(matrix)
        n=len(matrix[0])
        memo={}

        def helper(r,c):
            nonlocal memo
            if r>=m or c>=n or matrix[r][c]=='0':#out of range or cell value being 
                #xero does not contribute in forming square
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            currSide=1
            left=helper(r,c+1)
            bottom=helper(r+1,c)
            bottomLeft=helper(r+1,c+1)

            memo[(r,c)]=currSide+min(left,bottom,bottomLeft)#why min?
            #the expansion of square is limited by the smallest satisfying ones i.e say
            #(3,1,2) this means the rows and cols uptill 1, contribute to square, but after 1, say 2,
            # not all rows and cols are 1, similarly after 2 say 3, again not all rows and cols are
            # 1/ contribute to square
            #this primarily eliminates all the squares that has a zero embedded
            return memo[(r,c)]

        #loop through every cell in matrix and call helper
        maxSide=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    maxSide=max(maxSide,helper(i,j))

        return maxSide*maxSide #to form area