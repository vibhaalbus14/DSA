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
            