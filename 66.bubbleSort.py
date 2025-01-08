def bubble_sort(array):
    n=len(array)
    count=0
    endIndex=n
    while count!=n: #no of passes len(array)-1 since the element in the beginning is always sorted
        for j in range(1,endIndex):
            if array[j-1]>array[j]:#swap
                temp=array[j-1]
                array[j-1]=array[j]
                array[j]=temp
        endIndex-=1 #since the last element is pushed to its actual position,no need to touch it again
        count+=1

    return array
print(bubble_sort([7,6,4,3]))
print(bubble_sort([6,0,3,5,5]))
print(bubble_sort([]))
