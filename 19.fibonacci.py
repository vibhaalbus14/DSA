#--------------------recursion--------------------
#time complexity:O(2^n)
#space complexity:O(n)(used by rec,call stack)

# def fib(n):
#     if(n<=1):return n
#     else: return fib(n-1)+fib(n-2)
# fib(8)

#------------------------memoization-------------------------
#time complexity:O(n)
#space complexity:O(n)( by rec call stack + hash table)

# def fib(n,ht={0:0,1:1}):
#     if n in  ht:
#         return ht[n]
#     else:
#         ht[n]=fib(n-1,ht)+fib(n-2,ht)
#         return ht[n]
# print(fib(8))

#----------------------tabulation---------------------
#time complexity:O(n)
#space complexity:O(n)

# def fib(n):
#     dp_table=[0]*(n+1)
#     if(n>0):
#         dp_table[1]=1
#     count=2
#     while(count<n+1):
#         dp_table[count]=dp_table[count-1]+dp_table[count-2]
#         count+=1
#     return dp_table[n]
# print(fib(8))

#---------------------space optmised tabulation---------------------
#time complexity:O(n)
#space complexity:O(1)
def fib(n):
    if(n<=1):return n
    else:
    
        prev=0
        curr=1
        count=1
        while(count)<n:
            next=prev +curr
            curr=next
            prev=curr
            count+=1
    return curr
print(fib(3))