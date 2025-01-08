import math
class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        #1.create a dict of all bombs
        #2.loop through bombs using 2 pointers
        #3.dist<=sumof radii,=>overlap
        #4.decrement the value in hashmap, if 0, ignore
        #5.return initial sum of values-final sum of values = max bombs detonated
        #6.if diff==0, no chain reaction=>only one bomb detonated
        
        if not bombs:
            return 0
        
        dict={}
        bombs=list(map(tuple,bombs))
        for bomb in bombs:
            if bomb not in dict:
                dict[bomb]=1
            else:
                dict[bomb]+=1
        
        initialSum=sum(dict.values())

        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                #distance bw 2 centers <= sum of those radii
                x1=bombs[i][0]
                x2=bombs[j][0]
                y1=bombs[i][1]
                y2=bombs[j][1]
                xSq=pow((x2-x1),2)
                ySq=pow((y2-y1),2)
                distance=math.sqrt(xSq+ySq)
                if distance <=(bombs[i][2]+bombs[j][2]):
                        if dict[bombs[i]]>0:
                            dict[bombs[i]]-=1
                        if dict[bombs[j]]>0:
                            dict[bombs[j]]-=1 
        
        finalSum=sum(dict.values())
        diff=initialSum-finalSum
        if diff==0:
            return 1
        else:
            return diff

        # i_xRange=(bombs[i][0]-bombs[i][2],bombs[i][0]+bombs[i][2]) #(x-r,x+r)
                # j_xRange=(bombs[j][0]-bombs[j][2],bombs[j][0]+bombs[j][2])
                # if j_xRange[0]<=i_xRange[1] or i_xRange[0]<=j_xRange[1]: #start2<=end1 or end1<=start2 as it is not sorted
                #     #if x range overlaps
                #     #check for y range
                #     i_yRange=(bombs[i][1]-bombs[i][2],bombs[i][1]+bombs[i][2]) #(y-r,y+r)
                #     j_yRange=(bombs[j][1]-bombs[j][2],bombs[j][1]+bombs[j][2])
                #     if j_yRange[0]<=i_yRange[1] or i_yRange[0]<=j_yRange[1]: 
                #         #y range also overlaps
