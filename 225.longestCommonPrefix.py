from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #trie implementation

        if len(strs)==1:
            return strs[-1]

        class TrieNode:
            def __init__(self):
                self.children={}
                self.isEnd=False

        def insertWords(word):
            nonlocal start
            curr=start
            for char in word:
                if char not in curr.children:
                    curr.children[char]=TrieNode()
                curr=curr.children[char]
            curr.isEnd=True
        
        start=TrieNode()
        for word in strs:
            if word:
                insertWords(word)
            else:
                return ""

        res=[]

        def identifyPrefix(start):
            curr=start
            # print(curr.children)
            # print(len(curr.children))
            while len(curr.children)==1 and curr.isEnd==False:
                
                char=list(curr.children.keys())[0]
                res.append(char)
                #print(res)
                curr=curr.children[char]
        
        identifyPrefix(start)

        return "" if not res else "".join(res)

#----------------------------approach2------------------------------------------------
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #trie implementation

        if len(strs)==1:
            return strs[-1]

        class TrieNode:
            def __init__(self):
                self.children={}
                self.isEnd=False

        def insertWords(word):
            print(word)
            nonlocal start,res,depth
            curr=start
            currDepth=1
            for char in word:
                if not curr.children:
                    curr.children[char]=TrieNode()
                elif  char not in curr.children: #stopping insertion of unnecessary words
                    break
                currDepth+=1
                curr=curr.children[char]

            depth=min(currDepth,depth)
            curr.isEnd=True
        
        depth=float("inf")
        res=[]
        start=TrieNode()

        for word in strs:
            if word:
                insertWords(word)
            else:
                return ""
        
        print(f"depth {depth}")
        def identifyPrefix(start):
            nonlocal res,depth
            curr=start
            i=1
            while i<depth and curr.children:
                char=list(curr.children.keys())[0]
                res.append(char)
                curr=curr.children[char]
                i+=1
            return "".join(res)
        
        if depth==1:
            return ""
        else:
            return identifyPrefix(start)
        
        
    
        
        
