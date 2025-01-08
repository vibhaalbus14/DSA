#------------------------------list creation methods-------------------------
# # n=int(input("enter the no of queens"))
# board=[["."*n]*n]
# print(board)

# board1=[["."]*n]*n
# print(board1)

# list=[0]*n
# print(list)

#------------------------shallow and deep copy-------------------------------------
# import copy
# list=[[1,2,3],[4,5,6]]
# shallow_copy=copy.copy(list)#stores the outer element and references to nested elements
# print("before changing:")
# print("list is",list)
# print("shallow_copy is",shallow_copy)
# shallow_copy[0][1]=100
# print("after changing:")
# print("list is",list)
# print("shallow_copy is",shallow_copy)

# deep_copy=copy.deepcopy(list)#stores the outer elemnts and also the copy of inner elements
# print("before changing:")
# print("list is",list)
# print("deep_copy is",deep_copy)
# deep_copy[0][1]=200
# print("after changing:")
# print("list is",list)
# print("deep_copy is",deep_copy)

# print("------------------")
# print(list.copy())

array=[9,20,2,3,4,5,6,7,8]
# array[:]=[]
# print(array)

# array.append([1,2,3,4])
# print(array)
# array.append([5,6,7,8])
# print(array)
# array.reverse()
# print(array)
# start=3
# print(array[:start-1:-1])
# dict={3:0,9:-1,20:1,15:0,7:2}
# itemList=sorted(dict.items(),key= lambda item: item[1])
# print(itemList)
# tempList=[(1,0),(6,0),(5,0)]
# itemList=sorted(tempList,key= lambda item: item[1])
# print(itemList)
# array1=[1,2,3,4,5]
# array2=[1,3,2,4,5]
# print(array1==array2)
# for num in array2[::-1]:
#     print(num)
# list1=[]
# list1.append(str(1))
# list1.append(str(2))
# list1.append(str(3))
# list1.append(str(4))
# list1.append(str(5))
# list1.append(str(6))
# string2="-".join(list1)
# print(string2)

# print(string2.split("-"))

# array=[1,2,3,4,5]
# print(array[-3])

# a=([1,1],2)
# print(a)

# bombs=[[1,2,3],[3,4,5],[3,4,5]]
# bombs=list(map(tuple,bombs))
# print(bombs)

# import math
# print(math.sqrt(80))
# n=5
# matrix=[[0]*n]*n
# print(matrix)

# dict={'a':['b','c','d']}
# print(dict['a'])

# n=12
# dp=[float('inf')*(n+1)]
# print(dp)
# dp1=[float('inf')]*(n+1)
# print(dp1)

# dict1={1:1,2:2,3:5}
# dict2={4:4}
# dict2=dict1
# print(dict2)
# res=dict2.get(3)
# print(res)
# if not res:
#     print("yes its not there!")
# else:
#     print("its there!")
# n=4
# dp=[[-1 for i in range(n)]for _ in range (n)]
# print(dp)
# dp[1][2]=0
# print(dp)

# visited=set()
# visited .add(1)
# print(visited)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = [Counter(s) for s in strs]

        seen = set()

        res = []

        for i in range(len(l)):
            if i in seen:
                continue

            res.append([])

            for j in range(i, len(l)):
                if j not in seen:
                    if l[i] == l[j]:
                        seen.add(j)
                        res[-1].append(strs[j])

        return res

