# def primeFactor(num):
#     factors=set()
#     n=num
#     if num%2==0:
#         #ensure if its completely divisible by 2
#         #even number
#         while n%2==0:
#             factors.add(2)
#             n=n//2
#     #odd number, check from first odd to root of num
#     for i in range(3,int(num**(0.5))+1,2):#only odd nums 
#         while n%i==0:
#             factors.add(i)
#             n=n//i

#     if n>2:# will become 1 if its composite after divisions
#         #prime factor
#         factors.add(n)
        
#     return factors
# set1=primeFactor(14)
# set2={2,3,5}
# set3=set1-set2
# if set3==set():
#     print(True)
# else:
#     print(False)

# set1={2,3}
# print(set1-{2,3,5})

# list1=[None]
# print(min(list1)+1)
# print(None)
# print(int(None))
# edges=[[1,2],[1,3],[2,3]]
# list1=[1,2,3]
# list2=[4,5,6]
# list1.extend(list2)
# print(list1)
# d={1:[0,4,5],
#    2:[7,8,9]}
# for key in d.keys():
#     d[key]=set(d[key])
# print(d)

# print(d.get(7))

# word="apple"
# print(word[-1:-2:-1])
# indices={0,1,2,3,4,5}
# validPref=list(indices)
# print(validPref)

# setA={1,2,3,4}
# setB={3,4,5}
# setC=setA & setB
# print(setC)

# string1="apple"
# print(string1[-1::-1])
# print(string1[-1:])
# setA=set()
# setA.add(0)
# setA.add(-1)

# setA.add(1)
# print(setA)
# from functools import reduce
# nums=[0,-1]
# nums=set(nums)
# print(nums)
# nums=list(map(str,nums))
# print(nums)
# nums=reduce(lambda a:len(a) if int(a) >=0 else len(a)-1,nums)
# print(nums)
# nums=[1,2,3,4,5]
# parent={num:num for num in nums}
# print(parent)
# set1=(4,5,7,3,1)
# print(set1)
# intermediateSet=[[1,2],[2,1],[4,3],[3,4]]
# intermediateSet=list(map(sorted,intermediateSet))#list of list, make it set of tuples
# intermediateSet=set(map(tuple,intermediateSet))

# print(intermediateSet)
# people=[[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# queue=sorted(people,key=lambda elem:elem[-1])
# print(queue)

# list1=[4,5,6]
# list1.insert(1,8)
# print(list1)

# from functools import cmp_to_key
# people=[[5,1],[5,0],[4,0],[3,2],[2,2],[1,4]]
# def mySort(u,v):
#     if u[0]>v[0]:
#         return -1
#     elif u[0]<v[0]:
#         return 1
#     elif u[0]==v[0]:
#         return u[1]-v[1]


# people=sorted(people,key=cmp_to_key(mySort))
# # print(people)
# def convertToBits(n):
#     stringRep=""
#     while n!=1:
#         num=n
#         n=n//2
#         stringRep+=str(num%2)
#         print(num,n,num%2)
#     stringRep+='1'
#     length=len(stringRep)#ensure its 32 bit
#     diff=32-length
#     newString="0" * diff
#     stringRep=stringRep+newString
#     return stringRep[::-1]
                       
# print(convertToBits(43261596))

#00000010100101000001111010011100
setA=set([4,2,1,4,3,4,5,8,15])
print(setA)