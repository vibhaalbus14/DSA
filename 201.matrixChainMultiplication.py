#time comp= O(n^2 xn) why? for every start,end there are k iterations => if n=no of matrices,
#we iterate through all matrices=>1,4->2,4->3,4 and k operations from start,end for each
#space comp:O(n^2)+O(n) memo + rec call stack
def matrixMultiplication(N, arr):
    #approach
    #1.send valid matrices indices
    #2.partition the arr into two matrices
    #3.opsPerformed=cost of multplying these to matrices
    #4.but if these 2 partiotions arent made upof single matrix, then the partion has to be split
    #again recursively
    #=> partition strategy

    memo={}    
    def helper(start,end):
        nonlocal memo
        if start>=end:
            return 0 #saying only one matrix or invalid matrix, no ops performed
        if (start,end) in memo:
            return memo[(start,end)]
        minCost=float("inf") #set a dummy min for every new start,end
        for k in range(start,end):
            opsPerformed=arr[start-1]*arr[k]*arr[end] #rows1*commonpart*cols2
            leftPartition=helper(start,k)
            rightpartition=helper(k+1,end)
            totalCost=opsPerformed+leftPartition+rightpartition

            minCost=min(minCost,totalCost)#for the same start,end, multiple possibilities,choose min
            memo[(start,end)] = minCost
        return memo[(start,end)]
    
    return helper(1,N-1)

print(matrixMultiplication(4,[2, 4, 6, 7]))