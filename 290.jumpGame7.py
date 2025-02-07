from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        #greedy tech
        #bfs
        #but stop visiting same indices
        #if till index 5 uve already added , another index in buffer calls 4, redundant addition
        #thus we keep track of maxProcessedIndex, to ensure in case we skip all processed indices
        #now why not make use of visited set?
        #maxProcessedIndex helps in preventing unnecessary loops of i
        #in visited, we have to reach i and then make a decision to add into dq or not
        #thus visited causes tle while maxProcessedIndex skips this nner loop and thus is more efficient
        n=len(s)
        buffer=deque()
        buffer.append(0)
        flag=True
        maxProcessedIndex=0
        while flag and buffer:
            startIndex=buffer.popleft()
            start=max(startIndex+minJump,maxProcessedIndex+1)
            end=min(startIndex+maxJump,n-1)
            for i in range (start ,end+1):
                if s[i]=="0" :
                    if i ==n-1:
                        return True 
                    buffer.append(i)
            maxProcessedIndex=end
        return False
