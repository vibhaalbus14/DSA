class Solution(object):
    
    def maxProfit(self, prices):
        max_profit=0
        l=0
        for r in range(1,len(prices)):
            if(prices[r]<prices[l]):
                l=r
            else:
                max_profit=max(max_profit,prices[r]-prices[l])

        return max_profit
object=Solution()
print(object.maxProfit([7,6,4,3,1]))