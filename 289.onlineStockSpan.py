class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        if not self.stack or price<self.stack[-1][0]:
            self.stack.append((price,1)) #(price,span)
            return 1
        
        ptr=len(self.stack)-1   
        count=1
        while ptr>=0 and self.stack[ptr][0]<=price:
            _,span=self.stack[ptr]
            count+=span
            ptr-=span
        self.stack.append((price,count))
        return count


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)