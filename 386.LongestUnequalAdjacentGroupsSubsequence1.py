from typing import List
from functools import lru_cache
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        n=len(words)

        @lru_cache
        def helper(index,curr):
            if index>=n:
                return 0
            
            maxLength=float("-inf")
            if curr==None:
                for i in range(index,n):
                    maxLength=max(maxLength,helper(i+1,groups[i])+1)
            else:
                for i in range(index,n):
                    #choose opp
                    if groups[i]==int(not curr):
                        maxLength=max(maxLength,helper(i+1,int(not curr))+1)
            return maxLength
        
        totalLength= helper(0,None)
        # print("totalLength",totalLength)
        start=0
        currLen=0
        curr=None
        
        while start<n:
            currLen=0
            curr=None
            flag=False
            visited=set()

            for i in range(start,n):
                # print("hello")
                if curr !=None and groups[i]!=int(not curr):
                    # print("exit")
                    continue
                if curr==None:
                    curr=groups[i]
                else:
                    curr=int(not curr)
                currLen+=1
                # print("currLen")
                visited.add(i)
                # print("next",visited)
                if currLen==totalLength:
                    # print("here, viisted, currLen",visited,currLen)
                    flag=True
                    break
            
            if flag:
                break
            start+=1
        
        #print("visited",visited)
        res=[]
        sortList=list(visited)
        sortList.sort()
        for i in sortList:
            res.append(words[i])
        return res
            
    
        


            
            
            








        