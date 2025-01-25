from typing import List
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        currCapacity=capacity
        steps=0

        for i in range(len(plants)):
            if plants[i]>currCapacity:
                
                steps+=2*i #walk back
                currCapacity=capacity
            steps+=1   #to reach current index
            currCapacity-=plants[i]
            
        return steps

