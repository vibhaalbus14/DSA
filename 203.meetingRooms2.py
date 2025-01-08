from typing import List
"""
Definition of Interval:
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #form a new list of tuples (starttime,endtime)
        #sort the endtime in ascending order
        #in case of conflict, solve the startime in descending order
        #identify minimum num of overlapping intervals
        #do this recursively cause days are to be assigned to overlapping-intervals too
        #why?
        #because overlapping intervals contribute to each day and since non overlapping intervals
        #are continuous, they contribute to a single day

        if not intervals:
            return 0

        newList=[]
        for obj in intervals:
            newList.append((obj.start,obj.end))
        newList.sort(key=lambda x:(x[1],-x[0]))
        
        def helper(tempList):
            if not tempList:
                return 0
            finalEnd=float("-inf")
            subList=[]
            for start,end in tempList:
                if start<finalEnd:#overlap
                    subList.append((start,end))
                else:
                    finalEnd=end
            return helper(subList)+1 #one because all non-overlapping times can be
            #scheduled in one day
        return helper(newList)
                


        