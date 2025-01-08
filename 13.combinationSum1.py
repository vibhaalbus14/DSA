def total(array):
    total=0
    for i in range(len(array)):
        total+=array[i]
    return total

def outer(combination,target):
    res=[]
    def combinationtotal(subset,combination,target,startIndex):
        nonlocal res
        if(total(subset)==target):
            res.append(subset.copy())
            return
        elif(total(subset)>target):#to avoid unnecessary computation
            return
        else:
            for index in range(startIndex,len(combination)):
                subset.append(combination[index])
                combinationtotal(subset,combination,target,index)
                subset.pop()
    combinationtotal([],combination,target,0)
    return res

print(outer([2,3,8,9],9))
        