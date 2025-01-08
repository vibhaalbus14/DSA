#time comp:O(n*sqroot(n))=> currSum from 1 to n and sqroot(n) loop
class Solution:
    def numSquares(self, n: int) -> int:
        memo={}
        listOfSquares=[]
        for i in range(1,int(n**0.5)+1):
            listOfSquares.append(i*i)
        

        def helper(index,currSum):
            nonlocal memo,n,listOfSquares
            if (index,currSum) in memo:
                return memo[(index,currSum)]
            if currSum==n:
                return 0#no more numbers are to be added
            if currSum>n or index>=len(listOfSquares):
                return float('inf')

            exclude=helper(index+1,currSum)
            include=helper(index,currSum+listOfSquares[index])+1
            memo[(index,currSum)]=min(include,exclude)
            return memo[(index,currSum)]
        return helper(0,0)

        