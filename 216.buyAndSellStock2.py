from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #approach
        #3 possible things can be done on a day
        #1.buy a stock
        #2.hold a stock and pass/just pass
        #3.if stock already present, sell it
        #4.use a flag to check if we are holding a stock or not
        memo={}
        def helper(index,stock):
            nonlocal memo
            if (index,stock) in memo:
                return memo[(index,stock)]

            if index>=len(prices):
                return 0
            
            
            #if stock=1=>holding
            #if holding, we can only sell or pass the day

            sell=0
            sellAndBuyOnSameDay=0
            buy=0

            if stock==1:
                #sell
                sell= prices[index] +helper(index+1,0) #sell on the same day and go to next day without any stock
                sellAndBuyOnSameDay=prices[index]+helper(index+1,1)-prices[index]#selling the stock and buying on the same day as its allowed
                #pass to next day regradless of holding or not
                skip=helper(index+1,stock)
            
            if stock==0:
                #buy
                buy=helper(index+1,1)-prices[index] #sell price-buy price
                #pass to next day regradless of holding or not
                skip=helper(index+1,stock)
                
            
            memo[(index,stock)]=max(sell,buy,sellAndBuyOnSameDay,skip)

            return memo[(index,stock)]
            
        return helper(0,0)#index,stock
        #stock=0 => not holding any stock
        