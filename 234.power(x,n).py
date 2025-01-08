class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return x
        if n==1:
            return x
        if n==0:
            return 1

        def helper(x,n):
            if n==1:
                return x
            if n==0:
                return 1
            
            res=helper(x,n//2)
            res=res*res
            if n%2!=0:
                return x*res
            else:
                return res
        
        if n<0:
            x=1/x
            n=-n
        return helper(x,n)