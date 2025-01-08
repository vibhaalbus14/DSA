from collections import deque
from collections import defaultdict
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # def compareWords(str1,str2):
        #     l=0
        #     r=len(str1)-1
        #     count=0
        #     while l<=r:
        #         if str1[l]!=str2[l]:
        #             count+=1
        #     return count

        if endWord not in wordList:
            return 0
        
        #build adj list using patterns
        adjList=defaultdict(List) #patter:[all words that match the pattern]
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(wordList):
                pattern =word[:i]+"*"+word[i+1:]#any word that creates a pattern obviously satisfies it
                adjList[pattern].append(word)

        dq=deque()
        visited=set()
        visited.append(beginWord)
        dq.append((beginWord,1))
        while dq:
            currWord,steps=dq.popleft()
            if currWord==endWord:
                return steps
            #search for words in wordList that differ by one char
            for i in range(len(currWord)):
                    #identify patterns
                pattern=currWord[:i]+"*"+currWord[i+1:]
                for neighbour in adjList[pattern]:
                    if neighbour not in visited:
                        dq.append((neighbour,steps+1))
                        visited.add(neighbour) #to prevent cycles
        return 0
        
            