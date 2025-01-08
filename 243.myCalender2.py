class MyCalendarTwo:

    def __init__(self):
        self.overLappingTimings=[]
        self.nonOverLappingTimings=[]

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.nonOverLappingTimings:
            self.nonOverLappingTimings.append((startTime,endTime))
            #print("nonOver lap start",self.nonOverLappingTimings)
            return True

        if  self.checkOverLap(self.overLappingTimings,startTime,endTime):
            return False
        else:
            #to add in overLappingTimings or not
            self.check(self.nonOverLappingTimings,startTime,endTime)    
            self.nonOverLappingTimings.append((startTime,endTime))
            #print("nonOver lap later",self.nonOverLappingTimings)
            return True


    def checkOverLap(self,compareWith,st,et):
        #print("in checkOverlap overlappingTimings",compareWith)
        if not compareWith:
            return False
        for overlapStart,overlapEnd in compareWith:
            if not ((st<overlapStart and et<=overlapStart) or (st>=overlapEnd and et>=overlapEnd)):
                return True
        return False
    
    def check(self,compareWith,st,et):
        
        for overlapStart,overlapEnd in compareWith:
            if not ((st<overlapStart and et<=overlapStart) or (st>=overlapEnd and et>=overlapEnd)):
                start=overlapStart
                end=overlapEnd
                #one interval can overlap with multiple intervals that are already present
                self.overLappingTimings.append((max(start,st),min(end,et)))
                
                
        #add to overlapping intervals
        
        #print("in check OverLapping",self.overLappingTimings)


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)

#----------------------------approach 2-----------------------------------------------------
class MyCalendarTwo:

    def __init__(self):
        self.calender=[]

    def book(self, startTime: int, endTime: int) -> bool:
        #add, check if conflict
        #incase of conflict,remove
        #else keep it like that

        if not self.calender:
            self.calender.append((startTime,1))
            self.calender.append((endTime,-1))
            return True
        else:
            self.calender.append((startTime,1))
            self.calender.append((endTime,-1))
            self.calender.sort()

        schedule=0
        for time,count in self.calender:
            schedule+=count
            if schedule>2:
                self.calender.remove((startTime,1))
                self.calender.remove((endTime,-1))
                return False
        return True
   
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)