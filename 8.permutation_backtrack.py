def swap(arr,x,y):
    arr[x],arr[y]=arr[y],arr[x]

def outer(arr):
    i=0
    length=len(arr)
    arr_seq=[]
    def perm(i,arr):
        nonlocal arr_seq
        if(i==(length-1)):
            arr_seq.append(arr[:])
            return
        else:
            for j in range (i,length):
                swap(arr,i,j)
                perm(i+1,arr)
                swap(arr,j,i)
    perm(i,arr)
    return arr_seq

print(outer([1,2,3]))
# def swap(x, y, arr):
#     arr[x], arr[y] = arr[y], arr[x]

# def outer(arr):
#     length = len(arr)
#     arr_seq = []
    
#     def perm(i, arr):
#         nonlocal arr_seq
#         if i == length - 1:
#             arr_seq.append(arr[:])  # Append a copy of arr
#             return
#         else:
#             for j in range(i, length):
#                 swap(i, j, arr)  # Corrected the swap call
#                 perm(i + 1, arr)
#                 swap(i, j, arr)  # Swap back for backtracking

#     perm(0, arr)
#     return arr_seq

# print(outer([1, 2, 3]))
#-----------------------------------------------approach-----------------------
#time comp:O(n!*n*n)
#n! because we loop through n! permutations
#n, because we loop through the list range
#another n, cause we insert and that involves shifting
#space comp:O(n!*n)
#to store n! permutations each of length n
def permutations(arr):
    if not arr:
        return [[]]

    def helper(i):
        nonlocal arr
        #base case
        if i==len(arr)-1:
            return [[arr[i]]]
        permList=[]
        currPerm=helper(i+1)
        for list in currPerm:
            for pos in range(len(currPerm)+1):
                copyList=list[:]
                copyList.insert(pos,arr[i])
                copyList.append(permList)
        return permList
    
    return helper(0)
