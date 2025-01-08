#if pivot is chosen as min or max element at evey step=> worst case time and space
#if its chosen randomly or as the middle element=> best and avg case
#time complexity = O(nlogn) BEST AND AVG CASE
#space complexity =O(logn) BEST AND AVG CASE
#time complexity = O(n^2) Worst Case
#space complexity =O(n) Worst Case

def overall(array):
    def swap(array, i, j):
        array[i],array[j]=array[j],array[i]
        

    def quickSort(array, start=0, end=None):
        if start>=end or end<start:
            return 
        else:
            
            pivot=start#can make pivot as middle element too
            i=pivot+1
            j=end

            while i<=j:
                if array[i]>=array[pivot] and array[j]<array[pivot]:
                    swap(array,i,j)
                    
                elif array[i]>array[pivot]:
                    j-=1
                elif array[j]<array[pivot]:
                    i+=1
                else:
                    i+=1
                    j-=1
                #once we find j<i=>j pointing at element less than pivot position element,so swap
            swap(array,pivot,j)
            pivot=j
            quickSort(array,start,pivot-1)#left side
            quickSort(array,pivot+1,end)#right side

    quickSort(array,0,len(array)-1)
    return array
print(overall([11,9,12,13,8]))
print(overall([0,2,2,2,0,2,1,1]))