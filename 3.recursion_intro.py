def number_palin(t):
    n=t

    def dec(n):
        if(n==1):
            print(1,end="")
            inc(n)
        else:
            print(n,end="")
            return dec(n-1)

    def inc(n):
        if(n==t):
            print(t,end="")
            return
        else:
            print(n,end="")
            return inc(n+1)
    dec(n)
        
number_palin(4)