from typing import List
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        visited=set()
        stack=[-1]*((2*n)-1)

        def backtrack(index):#passing index along the stack
            if index==len(stack):
                return True
            
            #check if index is available else go for next index
            if stack[index]!=-1:
                return backtrack(index+1)
            
            for num in range(n,0,-1):
                #check if num is already visited
                if num in visited:
                    continue
                
                if num!=1:
                    #check for index+num position 
                    if index+num<len(stack) and stack[index+num]==-1:
                        stack[index]=num
                        stack[index+num]=num
                        visited.add(num)
                        if backtrack(index+1):
                            return True
                        #backtrack
                        stack[index]=stack[index+num]=-1
                        visited.remove(num)
                else:
                    stack[index]=num
                    visited.add(num)
                    if backtrack(index+1):
                        return True
                    stack[index]=-1
                    visited.remove(num)
        backtrack(0)
        return stack
                
