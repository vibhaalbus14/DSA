#time complexity:O(logm)+O(logn)=O(log(m*n))-> binary search to find both column and row
#space complexity:O(1)
def search_in_matrix(matrix,target):
    #identifying the row in which target is present
    row=-1
    if len(matrix)==0:
        return False
    elif len(matrix)==1:
        row=0
    else:
      #binary serach for row
      high,low=len(matrix)-1,1
      while low<=high:
        mid=(high+low)//2
        if target<matrix[mid][0] and target >=matrix[mid-1][0]:
            row=mid-1
            break
        elif target<matrix[mid][0]:
            high=mid-1
        else:
            low=mid+1

    if row==-1:#target present in last row
        row==len(matrix)-1

    #identify the column using binary search
    if len(matrix[row])==0:#list empty
        return False
        
    low,high=0,len(matrix[row])-1
    while low<=high:
        mid=(low+high)//2
        if target==matrix[row][mid]:
            return True
        elif target<matrix[row][mid]:
            high=mid-1
        else:
            low=mid+1
    return False
print(search_in_matrix([[1,2,3,4],
                        [5,6,7,8],
                        [9,10,100,101]],100))
print(search_in_matrix([[]],100))
print(search_in_matrix([],100))
