class Solution(object):
    def isValid(self, s):
        stack=["#"]#to check if stack is empty
        top=0
        strPush=['(','[','{']#pushing all opening braces
        for char in s:
            if char in strPush:
                stack.append(char)
                top+=1
            else:
                if (char==')' and stack[top]==strPush[0])or (char==']' and stack[top]==strPush[1]) or (char=='}' and stack[top]==strPush[2]):
                    stack.pop()#popping from stack if closing braces are encountered
                    top-=1
                else:
                    return False
        if stack[top]=="#": #stack empty
            return True
obj=Solution()
print(obj.isValid("()[]{}"))
        