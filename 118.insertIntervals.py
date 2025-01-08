class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        n=len(intervals)
        if n==1:
            return intervals
        intervals.sort(key= lambda item:item[0])
        newList=[]
        newList.append(intervals[0]) #one pointer points to the last elemnet in newList
        #other pointer points to the element in intervals
        right=1

        while right<n:
            end=newList[-1][1]
            start=intervals[right][0]
            if start<=end: #merge
                #new end is the end of right
                newList[-1][1]=max(intervals[right][1],newList[-1][1])
                
            else:
                newList.append(intervals[right])
            right+=1
        return newList