import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #choose the char with max occurences first,one at a time
        #if it leads to 3 consecutive,pop the next highest and push this char
        #use maxHeap

        maxHeap=[]
        if a!=0:
            heapq.heappush(maxHeap,(-a,'a'))
        if b!=0:
            heapq.heappush(maxHeap,(-b,'b'))
        if c!=0:
            heapq.heappush(maxHeap,(-c,'c'))

        currChar=""
        currCharCount=0
        maxLength=0
        finalString=""

        while maxHeap :
            freq,char=heapq.heappop(maxHeap)
            freq=-freq
            if char!=currChar:  #valid
                if freq!=1:#push back into heap
                    freq-=1
                    heapq.heappush(maxHeap,(-freq,char))
                maxLength+=1
                currChar=char
                finalString+=char
                currCharCount=1
            elif char==currChar and currCharCount<2:
                if freq!=1:#push back into heap
                    freq-=1
                    heapq.heappush(maxHeap,(-freq,char))
                maxLength+=1
                finalString+=char
                currCharCount+=1
            elif currCharCount==2 : #cannot have three consecutive
                #heappop again
                if not maxHeap:
                    break
                freqNext,charNext=heapq.heappop(maxHeap)
                freqNext=-freqNext
                if freqNext!=1:#push back into heap
                    freqNext-=1
                    heapq.heappush(maxHeap,(-freqNext,charNext))#second char popped
                heapq.heappush(maxHeap,(-freq,char))#first inalid char popped
                maxLength+=1
                currChar=charNext
                finalString+=charNext
                currCharCount=1
                #also push the prev number
        return finalString