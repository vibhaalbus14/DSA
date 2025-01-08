#---------------------------------------1st approach------------------------------------
# def identify_winner(list,i,n,k):
#     if(n==1):
#         return list[0]
#     else:
#         remove_index=((i+(k-1))%n)
#         list.pop(remove_index)
#         n-=1
#         return identify_winner(list,remove_index,n,k)

# def overall(n,k):
#     list=[i for i in range(1,n+1)]
#     i=0
#     return identify_winner(list,i,n,k)

# print(overall(5,7))

#---------------------------------------2nd approach------------------------------------
# def overall(n,k):
#     def identify_winner(n):
#         if(n==1):
#             return 0
#         else:
#             return (identify_winner(n-1)+k)%n
            
#     return identify_winner(n)+1#to get value
# print(overall(5,7))

#---------------------------------------3rd approach------------------------------------
def overall(n,k):
    safe_pos=0
    for i in range(2,n+1):
        safe_pos=(safe_pos+k)%i
    return safe_pos+1
print(overall(5,7))