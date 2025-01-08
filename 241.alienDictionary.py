from typing import List
from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #understanding
        #1.what does the question tell?
        #arrange the letters as they appear in alien dictionary
        #=> all the unique letters are to be noted
        #2. when does a letter come first before the other?
        #this is inferred from the way strings are arranged in words list
        #3.what does the conds mean?

        #3.1=>the difference in 2 strings , the letters that cause the difference tells the order
        #in which they appear eg: "hfg" and "hfl" => g->l.Inthis case, no length restriction.

        #3.2=> consider the similarity bw letters of different words as 
        #long as the length criteria is satisfied
        #consider a="pq" and b="pqr".Here similarity bw p and bw q is considered since a.length<b.length
        #consider a="pq" and b="pq". here similarity is considered since a.length ==b.length
        #consider a="pqr" and b="pq". here eben though p and q are similar, it is not considered
        #as a.length>b.length.This leads to invalid order , and thus even if one pair eads to such kind
        #arrangement of letters become invalid => return ""


        #approach
        #1.map all unique letters add them to indegree and adjList
        #2.traverse through words ,compare pairs of words,add them to adj list and indegree acc
        #3.topological sort

        adjList={}
        indegree={}
        uniqueLetters=set()

        for word in words:
            for char in word:
                if char not in uniqueLetters:
                    uniqueLetters.add(char)
                    adjList[char]=[]
                    indegree[char]=0
        

        for i in range(len(words)-1):
            #if letters are different=> no length restriction
            #if letters are equal, hen length restriction has to be considered
            a=words[i]
            b=words[i+1]

            #minimum length if not will however be a.length
            ptr=0
            while ptr<len(a):
                if a[ptr]==b[ptr]: #all valid length comparisions
                    if len(a)>len(b):
                        return "" #cannot infer order if chars are equal
                    ptr+=1
                
                else:
                    #add to adjlist
                    adjList[a[ptr]].append(b[ptr])
                    indegree[b[ptr]]+=1
                    break
                    #why break?
                    #once first point of indifference is found, order is inferred, others presence
                    #doesnt not matter, as the first point of difference determines the order

        #topological sort
        res=[]
        dq=deque()
        for key,val in indegree.items():
            if val==0:
                dq.append(key)
        
        while dq:
            char=dq.popleft()
            res.append(char)
            for nextChar in adjList[char]:
                indegree[nextChar]-=1
                if indegree[nextChar]==0:
                    dq.append(nextChar)
        
        if len(res)==len(uniqueLetters): #all letters are ordered
            return "".join(res)
        else:
            return ""



