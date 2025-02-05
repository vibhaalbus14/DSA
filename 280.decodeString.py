class Solution:
    def decodeString(self, s: str) -> str:
        #when u encounter number, add into new cell
        #loop over till u find a closing bracket/a number
        #if closing bracket, evaluate and opening==0, push to res
        #else, eval and push into stack
        #if a number, use a new cell

        openB=0
        closeB=0
        numberStack=[]
        alphabetStack=[]
        numbers=[str(i) for i in range(10)]
        res=[]

        i=0
        while i<len(s):
            #number
            if s[i] in numbers:
                numberStack.append("")
                while s[i] in numbers:
                    numberStack[-1]+=s[i]
                    i+=1
            if s[i]!=']':
                if s[i]=='[':
                    openB+=1
                if openB==closeB:
                    res.append(s[i])
                alphabetStack.append(s[i])
                
            elif s[i]==']':
                closeB+=1
                number=int(numberStack.pop())
                #till we encounter "[",pop from alphaStack
                currString=""
                while alphabetStack[-1]!="[":
                    currString=alphabetStack.pop()+currString
                alphabetStack.pop()
                concatenateString=""
                for _ in range(number):
                    concatenateString+=currString
                if openB==closeB:
                    res.append(concatenateString)
                else:
                    alphabetStack.append(concatenateString)
            i+=1

        return "".join(res)




           

       