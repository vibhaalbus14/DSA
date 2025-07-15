'''
question Link:https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

'''
import heapq
#------------------------------------brute force-------------------------
# #TC=O(nlogn) +O(n*[logn+n])=>O(n**2)
# class Solution:
#     def jobSequencing(self, deadline, profit):
#         # code here
        
#         n=len(deadline)
#         usedDay=set()
#         maxHeap=[]
#         for i in range(n):
#             maxHeap.append((-profit[i],deadline[i]))
        
#         #sort the list in descending order, so that max profit is chosen first
#         heapq.heapify(maxHeap)
#         maxProfit=0
#         jobDone=0
        
#         while maxHeap:
            
#             profit,endtime=heapq.heappop(maxHeap)
            
#             #loop over the available days in descending order
#             #assign a day only if that day is available and not in used
            
#             for i in range(endtime,0,-1):
#                 if i not in usedDay:
#                     usedDay.add(i)
#                     maxProfit+=(-profit)
#                     jobDone+=1
#                     break
                
#         return [jobDone,maxProfit]
            
#-------------------------------------optimised approach------------------------------
#Tc=O(nlogn)
class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        
        n=len(deadline)
        newList=[]
        for i in range(n):
            newList.append((deadline[i],profit[i]))
        
        newList.sort()
        minHeap=[]
        
        
        for deadline,profit in newList:
            
            if len(minHeap)>=deadline:
                #pop teh one that has least profit 
                heapq.heappushpop(minHeap,profit)
            else:
                heapq.heappush(minHeap,profit)
            
            
        return [len(minHeap),sum(minHeap)]
            
            