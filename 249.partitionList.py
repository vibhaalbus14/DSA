from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #all occurences of a letter must only be in one part
        #when all the parts are concatenated, it must bufferult in s
        #=> same order/ substring partition
        #create max partitions

        hashMap={}
        buffer=[]
        ptrList=[]

        l=0
        r=0

        while l<=r and r<len(s):
            if s[r] not in hashMap:
                #can lead to new partition
                hashMap[s[r]]=1
                ptrList.append([l,r])
                buffer.append(s[r])
                r=r+1
                l=r
            else:
                hashMap[s[r]]+=1
                #check for the existence of curr char in recent list
                if s[r] not in buffer[-1]:
                    while buffer:
                        if s[r] not in buffer[-1]:
                            buffer.pop()
                            ptrList.pop()
                        else:
                            break
                            #buffertore start position to the start of already
                            #included list
                prevL,prevR=ptrList[-1]
                l=prevL
                buffer[-1]+=s[prevR+1:r+1]
                ptrList[-1][1]=r
                r+=1
                
            
        finalbuffer=[]
        for strList in buffer:
            finalbuffer.append(len(strList))
        return finalbuffer
                
                

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
print(Solution().partitionLabels("eccbbbbdec"))

            


        