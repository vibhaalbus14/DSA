from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #approach
        #if the numbers are the same, they could be referring to each other
        #if res==0 => unique, add one
        #if i=0 or count=0 or i!=i-1=> start of new group,add k+1

        answers.sort()
        res=0
        count=0
        curr=0

        for i,num in enumerate(answers):
            if num==0: #unique colr
                count+=1
            elif i==0 or curr==0 or num!=answers[i-1]: #start of newgrp
                count+=num+1
                curr=num
            else:
                curr-=1
        
        return count




