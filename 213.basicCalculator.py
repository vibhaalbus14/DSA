from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        #create a global deque, in case of same precedence, left->right priority
        #whenever an open bracket is encountered, do rec,
        #during rec,pass pointers, and work on global stack

        dq=deque()
        s=s.replace(" ","")#remove spaces
        n=len(s)
        #make globalStack
        l=0
        r=0
        while l<=r  and  r<n:
            if s[r]=="+" or s[r]=="-" or s[r]==")" or s[r]=="(":
                res=s[l:r]
                if res:
                    dq.append(int(res))
                dq.append(s[r])
                r=r+1
                l=r
            else:
                r+=1
        res=s[l:r]
        if res:
            dq.append(int(res))
        
        if len(dq)==1: #which means only numbers
            return dq[0]

        def helper():
            a=None
            b=None
            op=None
            currStack=deque() #maintain a currStack for every call
            while dq:
                val=dq.popleft()
                if val=="(":
                    val=helper()
                    currStack.append(val)
                elif val==")":
                    break
                else:
                    currStack.append(val)
            
            #evaluation
            if currStack[0]=="-":#-2
                currStack.popleft()
                num=currStack.popleft()
                currStack.appendleft(-num)
            
            if len(currStack)==1 :
                return currStack[0]
            
            while currStack:
                ele=currStack.popleft()
                if type(ele) is int:
                    if a is None:
                        a=ele
                    elif b is None:
                        b=ele
                else:
                    if (ele=="+" or ele=="-") and op is None:
                        op=ele
                
                if a!=None and b!=None and op!=None:
                    #evaluate 2 at first
                    if op=="+":
                        if currStack:
                            currStack.appendleft(a+b)
                        else:
                            return a+b
                    else:
                        if currStack:
                            currStack.appendleft(a-b)
                        else:
                            return a-b
                    a=None
                    b=None
                    op=None

        return helper()
        
                




        