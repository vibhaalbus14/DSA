class SegmentTree:
    def __init__(self,L,R):
        self.left=None
        self.right=None
        self.L=L #leftRange
        self.R=R #rightRange
    
    def insertRange(self,node,start,end):
        curr=node
        while True:
            if start>=curr.R:
                if curr.right==None:
                    curr.right=SegmentTree(start,end)
                    return True
                curr=curr.right
            elif end<=curr.L:
                if curr.left==None:
                    curr.left=SegmentTree(start,end)
                    return True
                curr=curr.left
            else:
                return False

class MyCalendar:

    def __init__(self):
        self.root=None 
        #it is a class property to MyCalender
        #and an object to SegmentTree , if non empty

    def book(self, startTime: int, endTime: int) -> bool:
        if self.root==None:
            self.root=SegmentTree(startTime,endTime)
            return True
        else:
            obj=self.root
            return obj.insertRange(self.root,startTime,endTime)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)