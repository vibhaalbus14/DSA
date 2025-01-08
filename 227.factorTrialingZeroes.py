class Solution:
    def trailingZeroes(self, n: int) -> int:
        #every multiple of 5 leads to formation of zero
        #this reduction to quotient cuts down many numbers
        #runs in logarithmic time
        count=0
        while n>=5:
            n=n//5
            count+=n
        return count


            
        


        