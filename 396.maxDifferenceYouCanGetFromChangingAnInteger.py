from collections import defaultdict
class Solution:
    def maxDiff(self, num: int) -> int:
        hashMap=defaultdict(list)
        strNum=str(num)
        minStart,maxStart=None,None
        minList,maxList=[],[]

        for i,char in enumerate(strNum):
            if minStart==None and char!='0':
                minStart=char
            if maxStart==None and char!='9':
                maxStart=char
            
            hashMap[char].append(i)
            minList.append(char)
            maxList.append(char)
        
        def checkMin(minStart,repValue):
            #replace all minStart occ with '0'
            for i in hashMap[minStart]:
                minList[i]=repValue
            
            #join and check if the list is 0 or has any leading zeroes
            newS="".join(minList)
            
            if int(newS)=='0' or  minList[0]=='0':
                #change the occ of minStart to  '1' instead of '0'
                return checkMin(minStart,'1')
            
            elif newS==strNum:
                minStart=None
                #identify minStart  that is not equal to minNum[0]th char
                for char in minList:
                    if char!=minList[0] and char!='0':
                        minStart=char
                        break
                if minStart!=None:
                    return checkMin(minStart,'0')
            #making in place changes
            return int(newS)
        
        #only finding min is complicated since it involves '0'
        if minStart!=None:
            minS=checkMin(minStart,'0')
        else:
            minS=int("".join(minList))

        #find max
        if maxStart!=None:
            for i in hashMap[maxStart]:
                maxList[i]='9'
        
        maxS=int("".join(maxList))
        return maxS-minS





            

        