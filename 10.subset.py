result=[[]]
def subsets_calc(i,array,subset):
    global result
    if(i==len(array)):
        result.append(subset.copy())
        return True
    subsets_calc(i+1,array, subset)#exclude step
    subset.append(array[i])#include step
    subsets_calc(i+1,array,subset)
    subset.pop()#backtrack step
    return True

subsets_calc(0,[1,2,3],[])
print(result)

# array=[1,2,3]
# res=[]
# res.append(array.copy())
# print("using append : ",res)
# res1=[]
# res1.extend(array.copy())
# print("using extend : ",res1)