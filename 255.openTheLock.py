from typing import List
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start="0000"
        visited=set() #used to maintain states that are  visited and not in deadends
        if start in deadends:
            return -1
        dq=deque()
        dq.append((start,0)) #start state, steps
        visited.add(start)

        while dq:
            currState,currSteps=dq.popleft()
            if currState==target:
                return currSteps
            #neighbours are all states obtained by dec / inc each position of the currState
            for i in range(4): #4 positions
                flag=0
                for _ in range(2): #2 moves, to inc or dec
                    neighbour=list(currState)
                    if flag==0: #increment
                        neighbour[i]=str((int(currState[i])+1)%9)
                        flag=1
                    else : #decrement
                        if int(currState[i])==0:
                            neighbour[i]=str(9)
                        else:
                            neighbour[i]=str((int(currState[i])-1)%9)
                    #add this changed state
                    neighbour="".join(neighbour)
                    if neighbour not in visited and neighbour not in deadends:
                        dq.append((neighbour,currSteps+1))
                        visited.add(neighbour)
        return -1