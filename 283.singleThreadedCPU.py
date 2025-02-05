from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #maintain 2 minheaps
        #one is to identify the process with enqueue <=t and push into buffer
        #other is buffer, to give the cpu min possible time consuming process
        starter=[]
        buffer=[]
        minTime=float("inf")

        for i in range(len(tasks)):
            enqueue,process=tasks[i]
            starter.append((enqueue,process,i))
            if enqueue<minTime:
                minTime=enqueue
        
        currTime=minTime
        heapq.heapify(starter)
        res=[]
        flag=True
        while flag:
            if starter and not buffer and starter[0][0]>currTime:#cpu idle , getit going with available processes at time t
                currTime=starter[0][0]
            while starter and starter[0][0]<=currTime :
                availTime,processTime,index=heapq.heappop(starter)
                #avail time doesn matter anymore
                heapq.heappush(buffer,(processTime,index))
            
            #supply the lowest time consuming process to cpu
            if not buffer and not starter:
                flag=False
            else:
                processTime,index=heapq.heappop(buffer)
                res.append(index)
                currTime+=processTime
        
        return res



        