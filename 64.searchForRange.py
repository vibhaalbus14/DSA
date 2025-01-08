def search_for_range(array,target):
    def binarySearch(low,high,array):
        if (low>high):
            return -1
        else:
            mid=(low+high)//2
            if array[mid]==target:
                return mid
            elif target<array[mid]:
                return binarySearch(low,mid-1,array)
            else:
                return binarySearch(mid+1,high,array)

    res=binarySearch(0,len(array)-1,array)
    if res==-1:
        return [-1,-1]
    else:
        l,r=res,res
        while(l>-1):
            if l!=0:
                if array[l]==array[l-1]:
                    l-=1
                else:
                    break
            else:
                break
        while(r<len(array)):
            if r!=len(array)-1:
                if array[r]==array[r+1]:
                    r+=1
                else:
                    break
            else:
                break
        return [l,r]
print(search_for_range([1,2,2,2,3,4],2))
print(search_for_range([1,2,3,4,5,6],2))
print(search_for_range([1,2,2,2,3,4],5))
print(search_for_range([1,1,1,1,1,1],1))