def climbStairs(n):
    if(n<=2):return n
    else:
        prev=1
        curr=2
        count=3
        while(count<=n):
            next=prev+curr
            prev=curr
            curr=next
            count+=1
    return curr
    
print(climbStairs(4))