def combinationSum(n,k):
    array=[i+1 for i in range(9)]
    res=[]
    def calc_sum(array,subset,startIndex,n,k):
        nonlocal res
        if(sum(subset)==n and len(subset)==k):
            res.append(subset[:])
            return
        elif(sum(subset)>n or len(subset)>k):
            return
        elif(startIndex>=len(array)):
            return
        else:
            #hash={}
            for i in range(startIndex,len(array)):
                #if array[i] not in hash:
                    #hash[array[i]]=True
                subset.append(array[i])
                calc_sum(array,subset,i+1,n,k)
                subset.pop()
    calc_sum(array,[],0,n,k)
    return res

print(combinationSum(7,3))