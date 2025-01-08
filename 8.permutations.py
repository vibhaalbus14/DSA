list_complete=[]
def swap(x,y,array):
    array[x],array[y]=array[y],array[x]

def perm(array,i):
    global list_complete
    if(i==len(array)):
        list_complete.append(array[:])
    else:
        for j in range(i,len(array)):#all choices are valid
            swap(i,j,array)
            perm(array,i+1)
            swap(j,i,array)
    return True
        
perm([1,2,3],0)
print(list_complete)