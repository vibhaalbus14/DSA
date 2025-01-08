def total(subset):
    total=0
    for i in range(len(subset)):
        total+=subset[i]
    return total 
        
def combinationSum2(candidates, target):
    
    candidates.sort()
    res=[]
    def calc_sum(candidates,subset,target,startIndex):
        nonlocal res
        if(total(subset)==target):
            res.append(subset.copy())
            return
        elif(total(subset)>target):#prevents max recursion depth by avoiding unnecessary computation
            return
        else:
            hash={}
            for index in range(startIndex,len(candidates)):
                if(candidates[index] not in hash):
                    subset.append(candidates[index])
                    calc_sum(candidates,subset,target,index+1)#to prevent mutliple repetitions of candidate's #number 
                    subset.pop()
    calc_sum(candidates,[],target,0)
    return res         

print(combinationSum2([3,5,2,1,3],7))
# lists=[]
# total=0
# for i in range (len(lists)):
#     total+=lists[i]
# print(total)
# print(type(total))