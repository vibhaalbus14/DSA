from typing import List
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        #map board to square numbers
        n=len(board)
        sq=1
        hashMap={}
        flag=0 #=>left to right
        for i in range(n-1,-1,-1):
            if flag==0:
                for j in range(n):
                    hashMap[sq]=board[i][j]
                    sq+=1
                flag=1#right to left
            elif flag==1:
                for j in range(n-1,-1,-1):
                    hashMap[sq]=board[i][j]
                    sq+=1
                flag=0
        #---------------------------------------------------------------------------------
        def bfsTraversal():
            nonlocal visited,minSteps
            while dq:
                currSquare,stepsTaken=dq.popleft()
                if currSquare==n*n:#if destination is reached,break unnecessary check on other squares
                    minSteps=stepsTaken
                    break
                for steps in range(1,7):# since a dice roll will lead to op from 1 to 6
                    nextStep=currSquare+steps
                    if nextStep>n*n:#only if the nextStep is within the bound of board
                        break

                    if hashMap[nextStep]!=-1:#before adding to deque, we check if theres a ladder or not
                        #we do this before adding and not after popping, as this will treat all squares after popping normally
                        #and this helps in avoiding chained ladders or snakes
                        nextStep=hashMap[nextStep]
                        
                    if nextStep not in visited:
                        visited.add(nextStep)
                        dq.append((nextStep,stepsTaken+1))
            return minSteps
        
        minSteps=-1
        visited=set()
        dq=deque()
        dq.append((1,0))#append (initial pos,steps taken so far)
        visited.add(1)
        return bfsTraversal()
obj=Solution()
print(obj.snakesAndLadders([[-1,-1,-1,-1,-1,-1],
                       [-1,-1,-1,-1,-1,-1],
                       [-1,-1,-1,-1,-1,-1],
                       [-1,35,-1,-1,13,-1],
                       [-1,-1,-1,-1,-1,-1],
                       [-1,15,-1,-1,-1,-1]]))

