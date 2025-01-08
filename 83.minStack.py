from collections import deque
class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.dq=deque() #increasing deque, it stores indices
        self.ptr=-1

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        #check if the val is to be added into deque
        #1.check if deque is empty, if so ,insert top
        if self.ptr==-1:
            self.ptr+=1
            self.dq.append(self.ptr)
            return
        self.ptr+=1
        #2.if if the element to be inserted is less than element stack[dq[0]],appendleft to dq
        if self.stack[self.ptr]<self.stack[self.dq[0]]:
            self.dq.appendleft(self.ptr)

    def pop(self):
        if self.ptr==-1:#stack is empty
            return None
        if self.dq[0]==self.ptr:#element to be popped is the minimum element
            self.dq.popleft()
        poppedElement=self.stack.pop()
        self.ptr-=1
        return None

        

    def top(self):
        if self.ptr==-1:
            return None
        return self.stack[self.ptr]
        

    def getMin(self):
        if self.ptr==-1:
            return None
        return self.stack[self.dq[0]]#first element in dq is the minimum element
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.ptr()
# param_4 = obj.getMin()