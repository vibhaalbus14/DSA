#from math import sqrt
class Solution:
    def mySqrt(self, x: int) -> int:
        #return int(sqrt(x))
        if x==0 or x==1:
            return x
        
        #if num=4
        #sqrt(4)=2 => sq on bts
        #4=2*2
        #we use this logic to identify nearest sqrt
        #we assume that sqrt of any number cant be greater than num/2
        
        
        l=0
        r=x//2
        while l<=r:
            mid=(l+r)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                r=mid-1
            else:
                l=mid+1
        return r
                    

        