from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        #notice that any robot can make only one switch downwards
        #robot 2 will collect from prefixSum right or postfix sum left
        #pattern problem
        #robot2 can choose anything from left or right 
        # robo1 tries to minimize that by choosing the switch that causes
        #minimum val for robot2

        cols=len(grid[0])
        prefixSum=[]
        postfixSum=[]

        for _ in range(cols):
            prefixSum.append(0)
            postfixSum.append(0)

        prefixSum[0]=grid[0][0]
        postfixSum[-1]=grid[1][cols-1]

        for i in range(1,cols):
            prefixSum[i]=prefixSum[i-1]+grid[0][i]

        for i in range(cols-2,-1,-1):
            postfixSum[i]=postfixSum[i+1]+grid[1][i]
        
        currPointsWithRobo2=postfixSum[0]+prefixSum[cols-1]
        #no of times switches can be made ==no of cols
        for i  in range(cols):
            #if robo 1 make switch / goes down at ith pos
        
            rightPartRemSum=prefixSum[cols-1]-prefixSum[i]
            leftPartRemSum=postfixSum[0]-postfixSum[i]

            maxRobo2=max(leftPartRemSum,rightPartRemSum)
            currPointsWithRobo2=min(currPointsWithRobo2,maxRobo2)
            #this minimization is done by robot1
        
        return currPointsWithRobo2