from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        #approach
        #1.build a dp table using prev rows
        #2.this table adds evry top row values
        #3.consider every row to be a histogram prob, numbers indicate height and width is 1 for all
        #4.for every row in dp table, identify the largest rectangle possible using inc monotonic stack

        #note: space can be optimised by just using one list

        m=len(matrix)
        n=len(matrix[0])

        dp=[[0]*n for _ in range(m)]

        #1st row of dp == 1st row of matrix
        for j in range(n):
            dp[0][j]=int(matrix[0][j])
        #build subsequent dp rows based on prev dp rows and current matrix row
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j]=='0':
                    continue #because all cells are by def intiaised to 0
                dp[i][j]=int(matrix[i][j])+dp[i-1][j]
        #once the d-p table is built
        #pass every row of dp table to identify max rectangle
        #i.e for evry row, compute largest rectangle in a histogram
        finalMaxArea=0
        def histogramRectangle(i):
            maxArea=0
            #currenrtly we are working at this ith row of dp table
            stack=[] #jth, val
            for j in range(n):
                currVal=dp[i][j]
                if not stack or currVal>=stack[-1][1]:
                    stack.append((j,currVal))
                else:
                    while stack and currVal<stack[-1][1]:
                        prevIndex,prevVal=stack.pop()
                        maxArea=max(maxArea,(j-prevIndex)*prevVal)
                    stack.append((prevIndex,currVal)) #because current val is smaller than prev and can thus extend backwards
            #cal area for left over rectangles in stack

            while stack :
                prevIndex,prevVal=stack.pop()
                maxArea=max(maxArea,(n-prevIndex)*prevVal)
            return maxArea
        
        #send in all rows of dp table
        for i in range(m):
            finalMaxArea=max(finalMaxArea,histogramRectangle(i))
        return finalMaxArea
                    
#---------------------------------space optimised--------------------------------------
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        #approach
        #1.build a dp table using prev rows
        #2.this table adds evry top row values
        #3.consider every row to be a histogram prob, numbers indicate height and width is 1 for all
        #4.for every row in dp table, identify the largest rectangle possible using inc monotonic stack

        #note: space can be optimised by just using one list

        m=len(matrix)
        n=len(matrix[0])
        finalMaxArea=0
        dp=[0]*n 

        def histogramRectangle():
            maxArea=0
            #currenrtly we are working  on dp list
            stack=[] #jth, val
            for j in range(n):
                currVal=dp[j]
                if not stack or currVal>=stack[-1][1]:
                    stack.append((j,currVal))
                else:
                    while stack and currVal<stack[-1][1]:
                        prevIndex,prevVal=stack.pop()
                        maxArea=max(maxArea,(j-prevIndex)*prevVal)
                    stack.append((prevIndex,currVal)) #because current val is smaller than prev and can thus extend backwards
            #cal area for left over rectangles in stack

            while stack :
                prevIndex,prevVal=stack.pop()
                maxArea=max(maxArea,(n-prevIndex)*prevVal)
            return maxArea

        #build subsequent dp rows based on prev dp rows and current matrix row
        for i in range(m):
            for j in range(n):
                
                if matrix[i][j]=='0':
                    dp[j]=0
                else:
                    dp[j]=int(matrix[i][j])+dp[j]
            #make a call to histogram
            #i.e for evry row, compute largest rectangle in a histogram
            finalMaxArea=max(finalMaxArea,histogramRectangle())

        return finalMaxArea
                    

        

        