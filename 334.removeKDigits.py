class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #reduce the value of the integer by removing from highest contributing place
        #but this removal can affect other places

        if len(num)==k:
            return "0"

        res=[]
        pops=0
        #monotonic inc stack
        for char in num:
            while res and int(char)<int(res[-1]) and pops <k:
                res.pop()
                pops+=1

            res.append(char)
            
        #ensure all k digits are removed
        #popping from last is eff as stack is in inc order
        if pops<k:
            while pops<k:
                res.pop()
                pops+=1

        resStr="".join(res)
        final=resStr.lstrip("0")

        return "0" if final=="" else final
           
        

            