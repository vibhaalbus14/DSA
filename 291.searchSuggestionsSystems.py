from typing import List

class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
        self.words=[]#add to all the letters

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        def insertWords(word):
            nonlocal root
            curr=root    
            for c in word:   
                #add to word to curr node
                curr.words.append(word)
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.words.append(word)
            curr.end=True

        def searchPrefix(word):
            nonlocal root
            curr=root
            for c in word:
                if c not in curr.children:
                    return []
                curr=curr.children[c]
            #lexicographical order
            curr.words.sort()
            if len(curr.words)<=3:
                return curr.words
            else:
                return curr.words[:3]

        #create a trie
        root=TrieNode()
        for word in products:
            insertWords(word)

        #search from searchWord
        res=[]
        window=""
        for i in range(len(searchWord)):
            window+=searchWord[i]
            res.append(searchPrefix(window))
        return res





        
        