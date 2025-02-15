class ProductOfNumbers:

    def __init__(self):
        self.productStorage=[]
        self.zeroStorage=[]
        self.nums=[]
        

    def add(self, num: int) -> None:
        self.nums.append(num)
        if not num:
            self.zeroStorage.append(len(self.productStorage))#since its the recent num being added
            num=1
        if not self.productStorage:
            self.productStorage.append(num)
        else:
            self.productStorage.append(self.productStorage[-1]*num)
        

    def getProduct(self, k: int) -> int:
        if k==1:
            return self.nums[-1]
        elif k==len(self.productStorage):
            if not self.zeroStorage:
                return self.productStorage[-1]
            else:
                return 0
        boundary=len(self.productStorage)-k-1
        #check if this boundary index/not included index is lesser than the most recent 0 index in zeroStorage
        if self.zeroStorage and self.zeroStorage[-1]>boundary:
            return 0
        interestedNumProd=self.productStorage[-1]
        notNeededNumProd=self.productStorage[len(self.productStorage)-k-1]
        return interestedNumProd//notNeededNumProd
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)