class my_exception(Exception):
    def __init__(self,mssg,val):
        self.message=mssg
        self.value=val
        super().__init__(self.message)

def kth_grammar(n,k):
    length=2**(n-1)
    mid =(2**(n-1))/2
    try:
        if(k>length):
            raise my_exception("k value must be  less than or equal to 2^n-1",k)
        if(n==1):
            return 0
        elif(k>mid):
            return int(not kth_grammar(n-1,k-mid))
        else:
            return  kth_grammar(n-1,k)
    
    except my_exception as e:
        print(f"message: {e.message}  \nvalue: { e.value}")




print(kth_grammar(4,6))

#--------------------------------approach---------------------------
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        #approach
        #we get every index by mapping to prev row's index,if know this, either its the same num or complement of the num
        #(n+1)th row=nth row+complement nth row
        #so if index k >mid of that row, it has to call the prev row, and its a complement of each other
        #if index<=mid, mirror of nth row, so no need to complement, same index map

        def helper(n,k):
            if n==1:
                return 0
            length=2**(n-1)
            mid=length//2

            if k<=mid: #n-th row has same bits, not a complemnet
                return helper(n-1,k)
            else:
                return  int(not(helper(n-1,k-mid)))#why k-mid? because after mid, previous rows and existing rows are complemnet of each other
        return helper(n,k)