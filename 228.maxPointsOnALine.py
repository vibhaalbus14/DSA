from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        #slope mapping must be local to every starting point
        #why?
        #consider 1,1 2,2 and 2,3 and 3,2 .they have same slope(1,1)
        #the slopes are same but they dont lie on same line
        #hence, slope mapping is made local
        pointsMapping={}
        for i,coordinates in enumerate(points):
            pointsMapping[tuple(coordinates)]=i

        maxPoint=1

        for j in range(len(points)):
            slopeMapping=defaultdict(set)
            x1,y1=points[j]

            for i in range(j+1,len(points)):
                x2,y2=points[i]

                dx=(x2-x1)
                dy=(y2-y1)
                g=gcd(dx,dy)
                    # Normalize slope to ensure consistency
                 # Normalize slope to ensure consistency
                if g != 0:
                    dx //= g
                    dy //= g
                
                # Normalize negative slopes (flip direction for consistency)
                if dy < 0:
                    dx, dy = -dx, -dy
                elif dy == 0:  # Horizontal line
                    dx = abs(dx)
                angle=(dx,dy)
                
                
                
                slopeMapping[angle].add(pointsMapping[(x1,y1)])
                slopeMapping[angle].add(pointsMapping[(x2,y2)])
            
            for slopePoints in slopeMapping.values():
                maxPoint=max(maxPoint,len(slopePoints))
        return maxPoint