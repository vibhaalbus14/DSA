#time comp=O(d*(n+k))
#space comp=O(n+k) resuage of space for every digit place
def radix_sort(array):
    if len(array)==0:
        return array
    greatest_num=max(array)
    #identify the max digit place
    digit_places=len(str(greatest_num))
    #radix sort = d x counting sort
    for i in range(digit_places):
        counting_sort(array,i)

    return array

#time comp=O(n+k)
#space comp=O(n+k)
def counting_sort(array, place):
    #---------------step 1-----------------------------
    #first create temp array that can hold 0-9 values 
    #create output array same size as input array
    i=place
    temp=[0]*10
    output=[0]*len(array)

    #go through the specific digit_place i.e units,tens,hundreds etc 
    #increment the corresponding index in temp array
    for num in array:
        digit=(num//10**i)%10
        temp[digit]+=1

    #---------------step 2-----------------------------
    #take cumulative sum in temp array
    for index in range(1,len(temp)):
        temp[index]+=temp[index-1]


    #---------------step 3-----------------------------
    #traverse through the array in reverse order
    #map the nums' digit_place to the same index in cumulative temp array
    #decrement cumulative sum value in temp
    #this decremented sum value gives the index in op array where the digit in array has to be mapped
    #copy the op array to original array
    for j in range(len(array)-1,-1,-1):
        digit=(array[j]//(10**i))%10
        temp[digit]-=1
        insert_pos=temp[digit]
        output[insert_pos]=array[j]

    array[:]=output[:]


print(radix_sort([384,73,374,183,65,247]))