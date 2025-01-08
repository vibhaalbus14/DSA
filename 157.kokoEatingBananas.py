import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        #one pile per hour only
        piles.sort()
        low=1
        high=piles[-1]
        #to identify the minVal where koko can eat all the bananas
        def findKValue(currK):
            hrs=0
            for num in piles:
                # if hrs>=h:
                #     return False
                # remainder=num-currK
                # hrs+=1
                # if remainder<=0:
                #     continue
                # else:
                #     while remainder>0:
                #         if hrs>=h:
                #             #time alloted is done before the piles get over
                #             return False
                #         remainder-=currK
                #         hrs+=1
                hrs+=math.ceil((num/currK))#only int part is considered
                #calculate left over bananas
                # if num%currK!=0:
                #     hrs+=1
                if hrs>h:
                    return False
                        

            return True
        
        #now upperBound of k is found out
        #lets identify the minimum using binary search
        #binary search
        while low<high:
            mid=(low+high)//2
            if findKValue(mid):
                high=mid
            else:
                low=mid+1
        
        return low
                


