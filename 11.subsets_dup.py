#sort the ip array -->this takes O(nlogn)
#time complexity=O(nlogn+n* 2^n)=O(n*2^n)
#choosing the end duplicate rather than the first duplicate
res=[]
def subset_calc_dup(array,i,subset):
    
    if(i==len(array)):
        res.append(subset[:])
        return
    while((i<(len(array)-1)) and (array[i]==array[i+1])):
        i+=1
    subset_calc_dup(array,i+1,subset)
    subset.append(array[i])
    subset_calc_dup(array,i+1,subset)
    subset.pop()
    return
input=[1,2,3,1] #[1,1,2,3]
input.sort()
subset_calc_dup(input,0,[])
print(res)
print(len(res))