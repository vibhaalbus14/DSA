#-----------------------TC : O(m*n*n) fr evry row, col => loop over entire col----------
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        m=len(points)
        n=len(points[0])

        
        def dfs(r,prevCol):
            if r==m:
                return 0

            marks=float("-inf")
            #choose a cell from curr row
            for j in range(n):
                marks=max(marks,dfs(r+1,j)+points[r][j]-abs(prevCol-j))
            return marks
        
        total=float("-inf")
        for j in range(n):
            total=max(total,dfs(1,j)+points[0][j])
        
        return total

#-----------------------TC : O(m*n) --------------------------------
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        #approach
        #1.here both the values and the col diff matters
        #2.so lets build the max that every col can make by considering the prev val and col diff
        #3. we use left and right array that notes the curr col max and prev col max-1

        m=len(points)
        n=len(points[0])
        maxVal=max(points[0])

        r=0

        while r+1<m:
            prevRow=points[r]
            currRow=points[r+1]

            left=[]
            right=[-1]*n

            #we try to identify the max points every cell in currRow can get from prevRow
            for val in prevRow:
                if not left:
                    left.append(val)
                else:
                    left.append(max(left[-1]-1,val))#prev pos max -1 for col diff, our current val
            for j in range(n-1,-1,-1):
                val=prevRow[j]
                if right[-1]==-1:
                    right[-1]=val
                else:
                    right[j]=max(right[j+1]-1,val)

            #make in place changes to the currRow
            for i in range(n):
                currRow[i]=currRow[i]+max(left[i],right[i])
                maxVal=max(maxVal,currRow[i])
            r+=1
    
        return maxVal