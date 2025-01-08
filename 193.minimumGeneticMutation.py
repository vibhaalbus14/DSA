from typing import List
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        #approach
        #1.the mutations in bank act as neighbouring nodes
        #2.from startGene , we can go to that node in bank such that there is only one char change
        #3.this one char change helps in identifying the neighbouring nodes aka adjacency
        #4.mark the genes in bank in visited
        #5.once the endGene is reached return min steps
        #6.if not return -1 when endGene is not reached and no genes are left in bank
        #7.since it says min, bfs> dfs +dp
        visited=set()
        dq=deque()

        def identifyChangeInChars(sourceGene,geneInBank):
            count=0
            for i in range(len(sourceGene)):
                if sourceGene[i]!=geneInBank[i]:
                    count+=1
            return count
        
        visited.add(startGene)
        dq.append((startGene,0)) #(start node, mutation underwent so far)
        while dq:
            start,step=dq.popleft()
            if start==endGene:
                return step
            #identify next gene variant from bank, this way all intermediate gene mutations are valid
            for gene in bank:
                #length of all genes are same
                #identify no of diff chars
                count=identifyChangeInChars(start,gene)
                if count==1 and gene not in visited:
                    dq.append((gene,step+1))
                    visited.add(gene)
        return -1


                


