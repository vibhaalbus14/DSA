class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        #length of integer must be n
        #digits in integers must have a consecutive difference of k
        #first digit cannot be zero

        #give choices from 1-9 for first digit
        def dfs(currentNum,numLength):
            if numLength==n:
                self.finalList.append(currentNum)
                return
            #nextNumbers are based on currentNum value
            unitsPlace=currentNum/10
            digit1=unitsPlace+k
            digit2=unitsPlace-k

            if digit1 in range(10):#check if its single digit i.e neither negative nor more than 9
                dfs(currentNum*10+digit1,numLength+1)
            
            if digit2 in range(10):
                dfs(currentNum*10+digit2,numLength+1)
             
            
        self.finalList=[]
        for num in range(1,10):
            dfs(num,1)
            
        return self.finalList


