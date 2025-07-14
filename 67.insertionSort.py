#time complexity:O(n^2)
#space complexity:O(1)
#insertion sort is a stable algo as it preserves the order in which the duplicates occur
#say [3,first(one),second(one)]->[first(one),3,second(one)]->[first(one),second(one),3]=>oreder of ones continue to remain
#as they were given initially

def insertion_sort(array):
    #assume first element is sorted
    #get the next element to compare with the sorted elements
     #first element is sorted
    
    for j in range(1,len(array)):
        #check the sorted array elements
            i=j-1
            temp=array[j]
            while array[i]>temp and i>=0:
                array[i+1]=array[i]
                i-=1
            array[i+1]=temp
    return array
print(insertion_sort([7,6,4,3,3]))
print(insertion_sort([]))
print(insertion_sort([7,-6,4,3,-3]))
print(insertion_sort([-1,-5,-4,-2]))