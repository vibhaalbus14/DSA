class Solution(object):
    def findMinArrowShots(self, points):
        arrows=len(points)
        points.sort(key=lambda x : x[1])
        prev_end=points[0][1]

        #identify no of overlaps=no of arrows reduced
        for item in points:
            if(item[0]<=prev_end):
                arrows-=1
            else:
                prev_end=item[1]

        return arrows+1
object=Solution()
print(object.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))

class Solution(object):
    def findMinArrowShots(self, points):
        arrows=0
        points.sort(key=lambda x : x[1])
        prev_end=float('-inf')
        for start,end in points:
            if start>end:
                arrows+=1
                prev_end=end
        return arrows
object=Solution()
print(object.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    
