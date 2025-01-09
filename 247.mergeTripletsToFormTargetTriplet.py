from typing import List
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        minFirst=float("inf")
        maxFirst=float("-inf")

        minSecond=float("inf")
        maxSecond=float("-inf")
        
        minThird=float("inf")
        maxThird=float("-inf")

        for triplet in triplets:
            first,second,third=triplet

            minFirst=min(minFirst,first)
            maxFirst=max(maxFirst,first)

            minSecond=min(minSecond,second)
            maxSecond=max(maxSecond,second)

            minThird=min(minThird,third)
            maxThird=max(maxThird,third)
        
        if target[0]<minFirst and target[0]>maxFirst:
            return False
        
        if target[1]<minSecond and target[1]>maxSecond:
            return False
        
        if target[2]<minThird and target[2]>maxThird:
            return False


        firstList=[]
        secondList=[]
        thirdList=[]
        #identify if first is possible
        flag1=0
        for triplet in triplets:
            first,second,third=triplet

            if first==target[0] and second<=target[1] and third<=target[2]:
                firstList.append(triplet)
                #this is a pass
                flag1=1
        if flag1==0:
            return False
        
        print("first",firstList)
        
        flag2=0
        for triplet in triplets:
            first,second,third=triplet

            if first<=target[0] and second==target[1] and third<=target[2]:
                #this is a pass
                secondList.append(triplet)
                flag2=1
                break
        if flag2==0:
            return False
        print("second",secondList)

        #merge first and second List
        mergedList1=[]
        for triplet1 in firstList:
            first1,second1,third1=triplet1
            for triplet2 in secondList:
                first2,second2,third2=triplet2
                mergedList1.append([max(first1,first2),max(second1,second2),max(third1,third2)])

        print("merged1",mergedList1)
        if target in mergedList1:
            return True
        
        for triplet in mergedList1:
            first,second,third=triplet
            if third>target[2]:
                return False

        thirdList=[]
        flag3=0
        for triplet in triplets:
            first,second,third=triplet
            if first<=target[0] and second<=target[1] and third==target[2]:
                #this is a pass
                flag3=1
                thirdList.append(triplet)
                
        if flag3==0:
            return False
        print("third",thirdList)
        mergedList2=[]
        for triplet1 in mergedList1:
            first1,second1,third1=triplet1
            for triplet2 in thirdList:
                first2,second2,third2=triplet2
                mergedList2.append([max(first1,first2),max(second1,second2),max(third1,third2)])
        
        print("merged2",mergedList2)
        if target in mergedList2:

            return True
        else:
            return False
    
obj=Solution()
print(obj.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]],[2,7,5]))

#------------------------------------eff approach---------------------------------------
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr=[-1,-1,-1]
        for triplet in triplets:
            first,second,third=triplet
            if first<=target[0] and second<=target[1] and third <=target[2]:
                curr=[max(curr[0],first),max(curr[1],second),max(curr[2],third)]
                if curr==target:
                    return True
        return False


        

        

        