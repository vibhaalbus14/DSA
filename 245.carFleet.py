from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #approach
        #if a car behind cannot catch a car in front before it reaches,
        #then the car at front forms a new fleet
        carList=[]
        #sort acc to positions nearest to target
        for i in range(len(speed)):
            carList.append((position[i],speed[i]))
        
        carList.sort(key=lambda x: -x[0])
        catchTime=0
        fleet=0
        for i in range(len(carList)):
            distA,speedA=carList[i]

            timeA=(target-distA)/speedA
            if timeA>catchTime: #a goes separately
                #form a fleet for a
                fleet+=1
                catchTime=timeA
        return fleet
            
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #approach
        #1. convert 2d-> 1d
        #2.calculate time taken by each car to reach the target (x2-x1)/speed
        #3.sort the time acc to positions in descending order. why?
        #easier to compare overtaking times

        time=[]
        for i in range(len(position)):
            time.append((position[i],(target-position[i])/speed[i])) #position,time taken to reach target

        time.sort(key=lambda x:-x[0])

        fleet=0
        currTime=None

        for pos,reachTime in time:
            if currTime==None:
                currTime=reachTime
                fleet+=1
            # else:
            #     if reachTime<=currTime:#belongs to same fleet
            #         pass
            elif reachTime>currTime: #different fleet
                currTime=reachTime
                fleet+=1

        return fleet
                    

