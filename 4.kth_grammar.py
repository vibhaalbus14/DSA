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




print(kth_grammar(2,3))
