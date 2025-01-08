def monotonic_array(array):
    #write code here
    length=len(array)
    def check_ascend(array):
        for i in range(length-1):
            if(array[i]<=array[i+1]):#ascending order
                pass
            else:
                return 0
        return 1
           
    def check_descend(array):
        for i in range(length-1):
            if(array[i]>=array[i+1]):#ascending order
                pass
            else:
                return 0
        return 1
                    
    res1=check_ascend(array)
    
    if (res1==0):
        res2=check_descend(array)
    
    if(res1==1 or res2==1):
        return ("array monotonic")
    else:
        return ("array is not monotonic")

print(monotonic_array([-3,-2,-1]))
    