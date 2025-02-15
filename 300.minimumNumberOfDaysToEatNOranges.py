from collections import deque
class Solution:
    def minDays(self, n: int) -> int:
        #minHeap dijkstra's approach
        #bfs approach
        dq=deque()
        visited=set()
        visited.add(n)
        #3 options in the beginning
        dq.append((0,n))
        while dq:
            days,org=dq.popleft()
            if org==0:
                return days
            if org-1>=0 and org-1 not in visited:
                dq.append((days+1,org-1))
                visited.add(org-1)
            if org%2==0 and org-(org//2) not in visited:
                rem=org-(org//2)
                dq.append((days+1,rem))
                visited.add(rem)
            if org%3==0 and org-(2*(org//3)) not in visited :
                rem=org-(2*(org//3))
                
                dq.append((days+1,rem))
                visited.add(rem)
            
            