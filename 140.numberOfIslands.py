#time comp=O(m*n)
#space comp:O(m*n)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #approach
        #the number adjacent 1's be it horz or vertical all grouped together forms an island
        #here the matrix,grid is rectangular
        #hence, the nodes are (row,col) unlike the usual adjacency matrix where same nodes act as start and end
        #1.loop through the grid
        #3.if u find 1 => land=>possibility of island only if the coordinated are not visited before
        #4.pass this node to bfs/dfs to identify the corresponding adjacent nodes
        #5.the no of times dfs/bfs is called from main func==no of islands
        #similar to connected components but rather than passing one node
        #here node is passed as row,col

        if not grid:
            return 0
        
        def dfsTrav(visited,i,j):
            visited.add((i,j))
            #identify its neighbours
            #left,right,top and bottom
            positions=[(0,-1),(0,1),(-1,0),(1,0)]
            for r,c in positions:#check validity for range, one value and visited
                if i+r in range(rows) and j+c in range(cols) and grid[i+r][j+c]=='1' and (i+r,j+c) not in visited:
                    dfsTrav(visited,i+r,j+c)


        visited=set()
        noIslands=0
        rows=len(grid)
        cols=len(grid[0])
        #loop through
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfsTrav(visited,i,j)
                    noIslands+=1
        return noIslands