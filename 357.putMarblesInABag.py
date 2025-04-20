from typing import List
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n=len(weights)
        if n==k or k==1:
            return 0
        
        #for 1 bag=> 2 marbles need to be picked
        #for 2 bags, 4 marbles need to be picked
        #for k bags, 2*k marbles need to be picked
        #=> k bags need k pairs of marbles
        #the first and last marbles are always present in the bag both in min score and max score

        needed=k-1
        initialSum=weights[0]+weights[-1]
        minScore,maxScore=initialSum,initialSum
        #the rem marbles should be picked bw first and last
        #all the marrbles must be adjacent to each other
        pairSumOfMarbles=[]
        for i in range(n-1):
            pairSumOfMarbles.append(weights[i]+weights[i+1])#choose adjacent pair of marbles
            #why pair?
            #each for one adjacent bags

        #after picking all marbles, sort it out
        #so that minimum sum causing pair is in min score and max in maxScore
        pairSumOfMarbles.sort()
        
        minScore+=sum(pairSumOfMarbles[:needed])
        maxScore+=sum(pairSumOfMarbles[-(needed):])
        

        return maxScore-minScore

        