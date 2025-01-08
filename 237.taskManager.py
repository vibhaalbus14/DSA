from collections import defaultdict
from typing import List
import heapq

class TaskManager:

    def _init_(self, tasks: List[List[int]]):
        self.taskDict=defaultdict(tuple)
        self.priorityDict=defaultdict(dict)

        for userid,taskid,prior in tasks:
            self.taskDict[taskid]=(userid,prior)
            if prior not in self.priorityDict:
                self.priorityDict[prior]={taskid:userid}
            else:
                self.priorityDict[prior][taskid]=userid
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskDict[taskId]=(userId,priority)
        #regardless of already presnt or not
        if priority not in self.priorityDict:
            self.priorityDict[priority]={taskId:userId}
        else:
            self.priorityDict[priority][taskId]=userId
        
        

    def edit(self, taskId: int, newPriority: int) -> None:
        userid,priority=self.taskDict[taskId]
        self.taskDict[taskId]=(userid,newPriority)

        del self.priorityDict[priority][taskId]
        if not self.priorityDict[priority]:
            del self.priorityDict[priority]
        
        if newPriority not in self.priorityDict:
            self.priorityDict[newPriority]={taskId:userid}
        else:
            self.priorityDict[newPriority][taskId]=userid

        

    def rmv(self, taskId: int) -> None:
        userid,prior=self.taskDict[taskId]
        del self.taskDict[taskId]

        del self.priorityDict[prior][taskId]

        #check if priority is empty
        if not self.priorityDict[prior]:
            del self.priorityDict[prior]
        

    def execTop(self) -> int:
        #create maxheap for priority
        #for the given priority, if tasks>1
        #create a maxheap for taskid
        #then pop, return userid and del taskid
        #print(self.priorityDict)
        if not self.taskDict:
            return -1
        maxheapPrior=[]
        for key in list(self.priorityDict.keys()):
            heapq.heappush(maxheapPrior,-key)

        maxPrior=-(heapq.heappop(maxheapPrior))

        maxheapTask=[]
        for task in list(self.priorityDict[maxPrior].keys()):
            heapq.heappush(maxheapTask,-task)
        #print(maxheapTask)
        maxTask=-(heapq.heappop(maxheapTask))
        #print(maxTask)


        res= self.priorityDict[maxPrior][maxTask] #userid 

        del self.priorityDict[maxPrior][maxTask]
        if not self.priorityDict[maxPrior]:
            del self.priorityDict[maxPrior]
        #also del from taskDict
        del self.taskDict[maxTask]
        return res

#------------------------------------------approach 2-----------------------------------------------------
from sortedcontainers import SortedDict
from collections import defaultdict
from typing import List
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskDict=defaultdict(tuple)
        self.priorityDict=SortedDict()

        for userid,taskid,prior in tasks:
            self.taskDict[taskid]=(userid,prior)
            if prior not in self.priorityDict:
                self.priorityDict[prior]=SortedDict()
            
            self.priorityDict[prior][taskid]=userid
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskDict[taskId]=(userId,priority)
        #regardless of already presnt or not
        if priority not in self.priorityDict:
            self.priorityDict[priority]=SortedDict()
        
        self.priorityDict[priority][taskId]=userId
        
        

    def edit(self, taskId: int, newPriority: int) -> None:
        userid,priority=self.taskDict[taskId]
        self.taskDict[taskId]=(userid,newPriority)

        del self.priorityDict[priority][taskId]
        if not self.priorityDict[priority]:
            del self.priorityDict[priority]
        
        if newPriority not in self.priorityDict:
            self.priorityDict[newPriority]=SortedDict()
        
        self.priorityDict[newPriority][taskId]=userid

        

    def rmv(self, taskId: int) -> None:
        userid,prior=self.taskDict[taskId]
        del self.taskDict[taskId]

        del self.priorityDict[prior][taskId]

        #check if priority is empty
        if not self.priorityDict[prior]:
            del self.priorityDict[prior]
        

    def execTop(self) -> int:
        #create maxheap for priority
        #for the given priority, if tasks>1
        #create a maxheap for taskid
        #then pop, return userid and del taskid
        #print(self.priorityDict)

        if not self.taskDict:
            return -1
        # maxheapPrior=[]
        # for key in list(self.priorityDict.keys()):
        #     heapq.heappush(maxheapPrior,-key)

        # maxPrior=-(heapq.heappop(maxheapPrior))

        # maxheapTask=[]
        # for task in list(self.priorityDict[maxPrior].keys()):
        #     heapq.heappush(maxheapTask,-task)
        # #print(maxheapTask)
        # maxTask=-(heapq.heappop(maxheapTask))
        # #print(maxTask)


        # res= self.priorityDict[maxPrior][maxTask] #userid 

        # del self.priorityDict[maxPrior][maxTask]
        # if not self.priorityDict[maxPrior]:
        #     del self.priorityDict[maxPrior]
        # #also del from taskDict
        # del self.taskDict[maxTask]
        # return res

        #get max prioriy
        #get max id
        priority,miniDict=self.priorityDict.peekitem()#pop the lowest valued key
        taskid,userid=miniDict.peekitem()

        del self.priorityDict[priority][taskid]
        if not self.priorityDict[priority]:
            del self.priorityDict[priority]
        # also del from taskDict
        del self.taskDict[taskid]
        return userid

