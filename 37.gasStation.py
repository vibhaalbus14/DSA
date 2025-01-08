#time complexity:O(n^2)
#space complexity:O(1)
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        #2 pointer approach
        n=len(gas)
        for i in range(n):
            if(gas[i]>=cost[i]):#initial assignment of fuel
                ptr1=i 
                tank=gas[ptr1]
                ptr2=(ptr1+1)%n
                while(tank>=cost[ptr2-1]):#if enough fuel is available to travel from one sation to another
                    ptr2=ptr2%n #circular implementation
                    if(ptr1==ptr2):
                        return ptr1
                    else:
                        tank+=gas[ptr2]-cost[ptr2-1]
                        ptr2+=1#reaching next station
        return -1
            
object=Solution()
print(object.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
print(object.canCompleteCircuit([2,3,4],[3,4,3]))


#time complexity:O(n)
#space complexity:O(1)
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost):
             return -1
        start=0 #starting from first index
        tank=0
        total_tank=0

        for i in range(len(gas)):
            tank+=gas[i]-cost[i] #enough fuel to reach next station
            total_tank+=gas[i]-cost[i]

            if(tank<0):
                start=i+1#changing the start position
                #but we continue to check for the entire circuit starting from 0th index
                tank=0

        if(total_tank>=0):
                return start
        else:
                return -1

        #total_tank matches to 0th index to check if complete circuit is possible
        #tank matches with start index, to check if movement bw stations is possible and is updated accordingly
object=Solution()
print(object.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
print(object.canCompleteCircuit([2,3,4],[3,4,3]))

