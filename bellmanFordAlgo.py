
#TC : O(V*E)
#SC: O(V)

class Solution:
    def bellmanFord(self, V, edges, src):
        
        #bellman ford algo
        #similar to distance vector routing
        #dp approach
        #why? similar to dp tabulation but using 1d array
        #multiple edges depend on prev edge value
        #subproblems overlapping 

        #total n-1 iterations to identify final shortest path
        #when a src is given?
        #in the distance table, mark src zero and the rest as inf
        #then perform n-1 iterations
        #if a diff src is given, mark its dist as inf and the rest of the
        #nodes from src are not reachable and thus inf
        
        distTable=[10**8]*V
        
        distTable[src]=0
        n=V
        iterations=1
        
        while iterations <n:
            
            #no need to perfom transitivity
            #if base distTable[u]==inf=> not reachable
            for u,v,w in edges:
                if distTable[u]!=10**8 and distTable[u]+w<distTable[v]:
                    distTable[v]=min(distTable[v],distTable[u]+w)
                    
            iterations+=1
        
        #check if negative edge cycle exists
        #this means the path weight must be <0
        #a cycle with atleast one negative edge exists
        #the distTable after n-1 iterations is not stable and keeps 
        #changing even after n-1  iterations as looping over negative edges
        #continue to redyce the weights infinitely
        #so we check if the distTable at (n-1)th iteration is same as distTable at 
        #(n)th iteration => stability in weights
        #if yes, no neg cycle
        #if no, neg cycle exists
        for u,v,w in edges:
            if distTable[u]!=10**8 and distTable[u]+w<distTable[v]:
                #if true=> unstable
                return [-1]
                    
        return distTable
        
        
        
        
        
        
        
        
        