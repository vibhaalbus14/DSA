from collections import deque

class Solution:
    def intToRoman(self, num: int) -> str:
        hashMap={1:"I",
                5:"V",
                10:"X",
                50:"L",
                100:"C",
                500:"D",
                1000:"M"}
      
        res=[]
        valStore=deque()

        n=num
        i=0 #digit place value
        while n!=0:
            valStore.appendleft(((n%10)*(10**i),10**i))
            i+=1
            n=n//10
        #print(valStore)
        for num,currPlace in valStore:
            mostSigNum=num//currPlace
            #print(mostSigNum)
            if mostSigNum==4 or mostSigNum==9 :
                 #add the val
                nextPlace=num+currPlace
                if nextPlace in hashMap:
                    diff=currPlace
                    #apppend diff and then nextPLace
                    res.append(hashMap[diff])
                    res.append(hashMap[nextPlace])
                else:
                    
                    for i in range(mostSigNum):
                        #mostSigNum times currplace
                        res.append(hashMap[currPlace])
            
            elif  mostSigNum>=1 and mostSigNum<5:
                for i in range(mostSigNum):
                    #mostSigNum times currplace
                    res.append(hashMap[currPlace])
     
            elif  mostSigNum>=5 and mostSigNum<=9:
                diff=mostSigNum-5
                prevPlace=num-(diff*currPlace)
                if prevPlace in hashMap:
                    #successive additives
                    res.append(hashMap[prevPlace])
                    for i in range(diff):
                        res.append(hashMap[currPlace])

        return "".join(res)


            


        


