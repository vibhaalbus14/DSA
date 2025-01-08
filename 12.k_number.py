def outer(k,n): 
    array=[i+1 for i in range(n)]   
    res=[]
    
    def k_number(subset,start_index):
        nonlocal k,res,array
        
        if(len(subset)==k):
            res.append(subset.copy())
            return
        for index in range(start_index,len(array)):
            subset.append(array[index])
            k_number(subset,index+1)
            subset.pop()
            
    
    k_number([],0)
    return res

print(outer(4,4))
        

        