class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #note down the cells that make up both the islands
        #start from one cell and bfs till a cell from another island is reached
        #                                   or
        #multi source bfs
        rows=len(grid)
        cols=rows

        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        visited=set()
       

        def bfs(r,c):
            nonlocal visited
            dq=deque()
            visited.add((r,c))
            dq.append((r,c))
            while dq:
                r,c=dq.popleft()
                for tr,tc in directions:
                    nr=tr+r
                    nc=tc+c

                    if nr>=0 and nr<rows and nc>=0 and nc<cols and grid[nr][nc]==1 and (nr,nc) not in visited:
                        dq.append((nr,nc))
                        visited.add((nr,nc))
        
        flag=True
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    #since there are only 2 islands=> 2 separate bfs calls
                    flag=False
                    bfs(i,j)
                    break
            if not flag:
                break
                        
        
        dq=deque()
        for i,j in visited:
            dq.append((0,i,j))
            
        
        while dq:
            changes,r,c=dq.popleft()
            # print(r,c,changes)
            # print("visited",visited)
            for tr,tc in directions:
                nr=tr+r
                nc=tc+c

                if nr>=0 and nr<rows and nc>=0 and nc<cols and (nr,nc) not in visited:
                    if  grid[nr][nc]==1 :
                        return changes
                    
                    else:
                        dq.append((changes+1,nr,nc))
                        visited.add((nr,nc))
                
                        
                        





           

        