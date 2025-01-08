# a= input("enter book quantity and its price").strip(" ")
# print(a)
# list1=a.split(" ")#splittng for white space
# print(list1)
# list1=list(map(int,list1))
# x=list1[0]
# y=list1[1]
# print(x,y)
# print(type(x))

# if x>5:
#     y=y-y*(50/100)
# elif x==5:
#     y=y-y*(20/100)
# elif x>=2 and x<=4:
#     y=y-y*(10/100)
# else:
#     y=y

# print("final cost is :", int(y))

#digit sum-----------------------------------------------
# s=input("enter a number")
# def helper(s):#split("") is invalid seperator and split() makes the entire string to occupy one index arther than splitting into individual chars
#     list1=[char for char in s]
#     list1=list(map(int,list1))
#     #current_sum=sum(int(char) for char in s) #sum adds up all int values obtained from iterable
#     current_sum=sum(list1)
#     if current_sum>=10:
#         return helper(str(current_sum))
#     else:
#         return current_sum
# print(helper(s))

# a="banana"
# list1=a.split()
# #list2=a.split("")#invalid seperator
# print(list1)

#character occurence---------------------------------------
hash={}
s=input("enter a string")
for char in s:
    if char in hash:
        hash[char]+=1
    else:
        hash[char]=1
print(hash.items())