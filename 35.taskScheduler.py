#time complexity:O(n)
#space complexity:O(n)
class Solution(object):
    #to identify the idle slots
    def leastInterval(self, tasks, n):
        #create a dict with the task and its frequency
        dict={}
        for item in tasks:
            if item not in dict:
                dict[item]=1
            else:
                dict[item]+=1
        
        #to identify the max frequency

        max_freq=max(dict.values())
        #to identify no of keys with max count
        no_of_keys=len([key for key,value in dict.items() if value==max_freq])

        #identifying the no of parts
        parts=max_freq-1
        #no of slots in parts
        slots=parts*(n-(no_of_keys-1))
        #identify unscheduled tasks
        unscheduled_tasks=len(tasks)-(no_of_keys*max_freq)

        #identify idle slots
        idle_slots=max(0,slots-unscheduled_tasks)
        #this is done to avoid negative slot value
        #this happens if unique unscheduled tasks are available and do not cool down time 
        #like ["A","C","A","B","D","B"], 1

        return idle_slots+len(tasks)
object=Solution()
print(object.leastInterval(["A","C","A","B","D","B"], 1))