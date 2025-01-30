class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList==[] or secondList==[]:
            return []

        res=[]
        newList=firstList+secondList
        currList=[]
        for start,end in newList:
                currList.append((start,1))
                currList.append((end,-1))

        currList.sort(key=lambda x : (x[0],-x[1]))
        #print(currList)
        currCount=0
        prevCount=None
        start=None
        end=None

        for num,count in currList:
            currCount+=count
            #when to set start
            #print("curr,prev",currCount,prevCount)
            if currCount==2 and prevCount==1:
                start=num
                end=num
            if currCount==1 and prevCount==2:
                end=num
                if start!=None:
                    res.append([start,end])
                    start=None
                    end=None

            #print("st,end",start,end)
            prevCount=currCount
        
        
        return res

            


            

        