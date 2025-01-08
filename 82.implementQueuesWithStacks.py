class MyQueue(object):

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.top=-1
        self.usedIndex=-1

        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #push everything to stack1
        self.stack1.append(x)
        if self.usedIndex==-1:#nothing is popped
            self.top=0
            self.usedIndex=-1
        else:
            self.top=self.usedIndex+1
        
        

    def pop(self):
        """
        :rtype: int
        """
        #copy paste the last element from stack1 to stack2 and pop from stack2
        if self.top==-1:
            return None
        if self.top<len(self.stack1):
            self.stack2.append(self.stack1[self.top])
            self.top+=1
            self.usedIndex+=1
            if self.top>=len(self.stack1):
                self.top=-1
            return self.stack2.pop()

        

    def peek(self):
        if self.top==-1:
            return None
        return self.stack1[self.top]
        

    def empty(self):
        if self.top==-1:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()