class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        #approach
        #1.use minheap=> time,node,side
        #2.use visited to keep track of nodes that are marked
        #3.like bfs
        #4.adjList is not needed since its array implementation and
        #R=> node+1 and L=> node-1

        finalDominoes=[]
        for char in dominoes:
            finalDominoes.append(char)
        minHeap=[]
        visited=set()

        for i,char in enumerate(dominoes):
            if char!=".":
                minHeap.append((0,i,char)) #time,node,side
        
        while minHeap:
            currTime,currNode,currSide=heapq.heappop(minHeap)

            if currNode in visited:
                continue
            if minHeap and currTime==minHeap[0][0] and currNode==minHeap[0][1] and currSide!=minHeap[0][2]:
                #both sides nullify each other and curr node wont move
                finalDominoes[currNode]="."
                visited.add(currNode)
                continue
            
            finalDominoes[currNode]=currSide
            visited.add(currNode)

            #look for its neighbours
            if currSide=="R":
                neighbour =currNode+1
            else:
                neighbour =currNode-1
            #check neighbour's validity

            if neighbour>=0 and neighbour<len(dominoes) and neighbour not in visited:
                heapq.heappush(minHeap,(currTime+1,neighbour,currSide))
        
        return "".join(finalDominoes)
            
