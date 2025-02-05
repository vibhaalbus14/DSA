from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #create a stack for all safe asteroids
        #an asteroid can undergo multiple collisions , either it will survive or get destroyed

        stack=[]

        for ast in asteroids:
            #if same direction as top of stack or empty,append
            if not stack or not (stack[-1]>0 and ast<0) :#2 asteroids can meet only if neg comes on top of positive, in case of -1,-2,1,2=> even though opp, they never meet
                stack.append(ast)
            else:
                currDest=False
                while stack and not currDest:
                    #check for signs/directions
                    if (ast<0 and stack[-1]<0) or (ast>0 and stack[-1]>0):#no conflict
                        break
                    #check if the asteroids meet
                    if abs(ast)>abs(stack[-1]) :
                        stack.pop() #curr will destroy others
                    elif abs(stack[-1])==abs(ast):
                        stack.pop()
                        currDest=True
                    else:# abs(ast)<abs(stack[-1]):
                        #curr ast will be destroyed
                        currDest=True
                if not currDest:
                    stack.append(ast)
        return stack 