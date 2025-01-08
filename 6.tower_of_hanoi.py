def toh(n,start,end,intermediary):
    count=0
    def move_discs(n,start,end,intermediary):
        nonlocal count#to use localbound count in nested function
        if(n==1):
            print(f"move disc {n} from rod {start} to rod {end}")
            count+=1
            return
        else:
            move_discs(n-1,start,intermediary,end)
            print(f"move disc {n} from rod {start} to rod {end}")
            count+=1
            move_discs(n-1,intermediary,end,start)
    move_discs(n,start,end,intermediary)
    return count

movements=toh(4,"r1","r3","r2")
print(f"no of movements : {movements}")

        
        
