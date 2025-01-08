# def accept(arr):
#     length=len(arr)
#     new_arr=[0]*length
#     for i in range(0,length):
#         new_arr[i]=(arr[i]**2)
#     new_arr.sort()
#     return new_arr

# print(accept([-1,-3,-3,4]))

def sorted_square(array):
    length=len(array)
    new_arr=[0]*length
    i,j=0,length-1
    for k in range(length-1,-1,-1):
        if(array[i]**2>array[j]**2):
            new_arr[k]=array[i]**2
            i+=1
        else:
            new_arr[k]=array[j]**2
            j-=1
        new_arr.sort()
    return new_arr
print(sorted_square([-1,-3,-1]))




