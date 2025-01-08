
#time complexity:O(n) to loop through tokens
#space complexity:O(n) stack size
from math import trunc
class Solution(object):

    def evalRPN(self, tokens):
        #if num, push into stack
        #if operand, pop 2 upper elements from stack
        #push back the result again
        #push # in , so once we encounter that,we know stack is empty
        #array implementation of stack
        stack=[]
        stack.append("#") # to see if stack is empty
        top=len(stack)-1

        #listOfOperands=['+', '-', '*', '/']
        listOfOperands={'+':lambda a,b: a+b,
                        '-':lambda a,b: a-b,
                        '*':lambda a,b: a*b,
                        '/':lambda a,b: a/b}
        for char in tokens:
            if char in listOfOperands:
                #pop first 2
                if stack[top]!="#":
                    b=stack.pop()
                    a=stack.pop()
                    #res=eval(f"a {char} b")
                    res=listOfOperands[char](a,b)
                    print(res)
                    stack.append(trunc(res))
                    top-=1  #as 2 decrements and one increment
                else:
                    None
            else:
                stack.append(float(char))
                top+=1
        return int(stack[top])

obj=Solution()
print(obj.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

