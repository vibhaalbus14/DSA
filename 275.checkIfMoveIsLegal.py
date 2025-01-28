from collections import deque
from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        #endpoints must be valid
        #b,b,w,b is a good line
        #in line "w,b,b,w,w,w,x" where x=b, this part "b,b,w,w,w,x" is also a good line => subparts of a line can also be good

        rows=len(board)
        cols=len(board[0])
        if color=="B":
            req="W"
        else:
            req="B"

        hashMap={  
        1:[(-1,0)],#top
        2:[(0,-1)],#left
        3:[(1,0)],#bottom
        4:[(0,1)],#right
        5:[(-1,-1)],#topLeft
        6:[(-1,1)],#topRight
        7:[(1,-1)],#bottomLeft
        8:[(1,1)]#bottomRight
         }
        
        def bfs(directions):
            flag=-1
            dq=deque()
            dq.append((rMove,cMove))

            while dq:
                r,c=dq.popleft()
                #check its neighbours in directions
                for tr, tc in hashMap[directions]:
                    nr=r+tr
                    nc=c+tc

                    if nr>=0 and nr<rows and nc>=0 and nc<cols and board[nr][nc]!="." :
                        if board[nr][nc]==req:
                            
                            if flag==-1:
                                flag=False
                            dq.append((nr,nc))
                        elif board[nr][nc]==color:
                            if flag==-1:
                                return False
                            else:
                                return True
                                #once u say same color endpoint, no need to check further, return
                                
                            

            #print("inside",flag)
            if flag==-1:
                return False
            else:
                return flag

        answer=False
        for i in range(1,9):
            answer= answer or bfs(i)
        

        return answer

    
