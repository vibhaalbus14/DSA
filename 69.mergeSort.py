#time complexity:  O(no of elements at each level *total no of levels[n+n/2+n/4+n/16....+1])=>O(n*logn)
#space complexity: to store new array=O(n), recursion call stack= logn=> O(n)+O(logn)=O(n)
#divide and conquer algorithm
#stable algo i.e retains the intial ordering of duplicate elements
def merge_sort(array):
    #conquer part
    def merge(array1,array2):
        i,j=0,0
        mergedArray=[]
        #merge 2 arrays via pointers
        while i<len(array1) and j<len(array2):
            if array1[i]<=array2[j]:
                mergedArray.append(array1[i])
                i+=1
            else:
                mergedArray.append(array2[j])
                j+=1
        #when one of the array is exhausted i.e unequal length arrays
        while i<len(array1):
            mergedArray.append(array1[i])
            i+=1
        while j<len(array2):
            mergedArray.append(array2[j])
            j+=1
        return mergedArray

    #divide part
    def divide(array):
        if len(array)<=1:
            return array
        else:
            mid=len(array)//2
            leftSide=divide(array[:mid])
            rightSide=divide(array[mid:])
        return merge(leftSide,rightSide)

    return divide(array)
    
print(merge_sort([1,5,7,0,9,0]))
print(merge_sort([]))