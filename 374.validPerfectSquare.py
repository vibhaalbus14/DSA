class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #binary search
        if num==1:
            return True
        l=1
        r=num//2

        while l<=r:
            mid=(l+r)//2
            if mid*mid==num:
                return True
            elif mid*mid>num:
                r=mid-1
            else:
                l=mid+1
        return False
        
            
            