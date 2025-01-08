# from typing import List
# from functools import lru_cache
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
# #         approach
# #         1.cant use index,stock , transactions => too much mem space
# #         2.use variable "transactions" to trac no of transactions and if stock
# #         is bought or not
# #         3.if transaction is even=> eligible to buy, odd=> can sell
# #         4.0=> buy 1=>sell 2=> buy 3=>sell 4=> transaction limit breached as 
# #         2 transactions are performed
# #         5.skip comes into picture at all steps

#         k=2 #no of transactions to be performed at max

#         @lru_cache
#         def helper(index,transactions):
            
#             if index>=len(prices) or transactions>=2*k:
#                 return 0
            
#             skip=helper(index+1,transactions)

#             buy=0
#             sell=0

#             if transactions%2==0: #eligible to buy, no stock bought
#                 buy=helper(index+1,transactions+1)-prices[index]
#             else:
#                 can sell, already holding stock
#                 sell=prices[index]+helper(index+1,transactions+1)
            
#             return max(sell,buy,skip)

#         return helper(0,0)
#-----------------------------------------------------------------------------------------
from typing import List
from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #approach
        #1.cant use index,stock , transactions => too much mem space
        #2.use variable "transactions" to trac no of transactions and if stock
        #is bought or not
        #3.if transaction is even=> eligible to buy, odd=> can sell
        #4.0=> buy 1=>sell 2=> buy 3=>sell 4=> transaction limit breached as 
        #2 transactions are performed
        #5.skip comes into picture at all steps

        k=2 #no of transactions to be performed at max

        @lru_cache
        def helper(index,bought,transactions):
                    
            if index>=len(prices) or transactions>=2*k:
                return 0
            
            skip=helper(index+1,bought,transactions)

            buy=0
            sell=0

            if not bought: #eligible to buy, no stock bought
                buy=helper(index+1,1,transactions+1)-prices[index]
            else:
                #can sell, already holding stock
                sell=prices[index]+helper(index+1,0,transactions+1)
            
            return max(sell,buy,skip)

        return helper(0,0,0)
            


        