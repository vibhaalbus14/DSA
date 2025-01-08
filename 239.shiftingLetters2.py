from typing import List
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alphabets="abcdefghijklmnopqrstuvwxyz"
        hashMap={}
        for i,char in enumerate(alphabets):
            hashMap[char]=i
        #print(hashMap)

        prefixSum=[0 for i in range(len(s)+1)]
        storage=[]
        res=[]
        for char in s:
            storage.append(hashMap[char])
        

        for start,end,direction in shifts:
            if direction==1:
                prefixSum[end+1]+=1
                prefixSum[start]-=1
            elif direction==0:
                prefixSum[end+1]-=1
                prefixSum[start]+=1
        
        #process step
        diff=prefixSum[-1]
        for i in range(len(storage)-1,-1,-1):
            if storage[i]+diff==-1:
                newIndex=25
            else:
                newIndex=(storage[i]+diff)%26
            storage[i]=newIndex
            diff+=prefixSum[i]

        for i in range(len(storage)):
            res.append(alphabets[storage[i]])
        


        return "".join(res)