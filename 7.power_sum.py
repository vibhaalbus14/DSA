def container(arr):
    def calc_sum(arr,depth=1):
        sum=0
        for i in range(0,len(arr)):
            if(type(arr[i])==int):
                sum+=arr[i]
            else:
                sum+=calc_sum(arr[i],depth+1)**(depth+1)
        return sum
    return calc_sum(arr)

print(container([1,2,[3,4],[[2]]]))
#print(container([1,2,[3,4]]))
#print(container([[2]]))