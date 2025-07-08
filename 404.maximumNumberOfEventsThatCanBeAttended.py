from typing import List
import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        #mindblowing approach
        #minHeap, to assign earliest ending currDays the lowest currDay
        #sort the code
        #=> greedy approach + minHeap

        #we add all the end time of days that start at currDay to the minHeap
        #so now, evn though multiple events occur at same satart Time, we will be assigning the event acc to the the one that ends early


        events.sort()
        n=len(events)
        minHeap=[]
        event=0
        currDay=1
        i=0 #currDay count

        for st,end in events:
            currDay=max(st,currDay)

            #add all the end currDays of the events , that start from this curr currDay
            while i<n and events[i][0]<=currDay:
                heapq.heappush(minHeap,events[i][1])
                i+=1


            while minHeap and minHeap[0]<currDay :
                heapq.heappop(minHeap)

            #pop valid end currDay interval top>=currDay
            if minHeap :
                heapq.heappop(minHeap)
                event+=1
                currDay+=1
        
        return event
        