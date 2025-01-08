from typing import List
class TrieNode:
    def __init__(self):
        self.children={}
        self.isEndOfWord=False

class WordFilter:

    def __init__(self, words: List[str]):
        self.root=TrieNode()
        self.words=words

        #constructing Trie of given words
        def insertIntoTrie(word):
            curr=self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.isEndOfWord=True

        for word in self.words:
            insertIntoTrie(word)
    
    def f(self, pref: str, suff: str) -> int:
        #1.search for a prefix
        #2.if the prefix is right, form the word alongside using dfs backtracking
        #3.once iteration over prefix is completed,form all possible words with the given prefix
        #4.loop over all those words and see if the suffix matches
        #5.return the largest index else return -1.
        wordFormed=[]
        res=set()
        curr=self.root
        for c in pref:
            if c not in curr.children:
                return -1 #no word with such prefix
            curr=curr.children[c]
        #prefix found successfully
        wordFormed.append(pref)

        def dfs(curr,wordFormed):
            if curr.isEndOfWord==True:
                stringConvertion="".join(wordFormed)
                res.add(stringConvertion) #dont return as another word can be inside a given word like app in apple
            if not curr.children:
                return
            for child in curr.children:
                wordFormed.append(child)
                dfs(curr.children[child],wordFormed)
                wordFormed.pop()
            return

        dfs(curr,wordFormed)#call to get all words of specified prefix
        
        index=-1
        for word in res:
            if word.endswith(suff):
                for i in range(len(self.words)-1,-1,-1):
                    if self.words[i]==word:
                        index=max(index,i) 
                        break
        return index

#------------------------approach 2-----------------------------------------
from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.indices = []

class WordFilter:
    def __init__(self, words: List[str]):
        self.rootPref = TrieNode()
        self.rootSuff = TrieNode()
        
        # Construct the prefix and suffix tries
        def insertIntoTrie(index, word, baseRoot):
            curr = baseRoot
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                if not curr.indices or curr.indices[-1] != index:
                    curr.indices.append(index)
            curr.isEndOfWord = True
        
        # Insert word from as it is,strating from lowest index
        for index in range(len(words)):
            word = words[index]
            insertIntoTrie(index, word, self.rootPref)
            insertIntoTrie(index, word[::-1], self.rootSuff)
    
    def f(self, pref: str, suff: str) -> int:
        # Search prefix trie
        curr = self.rootPref
        for c in pref:
            if c not in curr.children:
                return -1
            curr = curr.children[c]
        validPref = curr.indices
        
        # Search suffix trie
        curr = self.rootSuff
        for c in suff[::-1]:
            if c not in curr.children:
                return -1
            curr = curr.children[c]
        validSuff = curr.indices
        
        # Use two-pointer technique to find the largest common index
        #start from last index
        i, j = len(validPref)-1,len(validSuff)-1
        while i > -1 and j > -1:
            if validPref[i] == validSuff[j]:
                return validPref[i]  # Largest common index , array is increasingly monotonic
            elif validPref[i] > validSuff[j]:
                i -= 1 #move towards smaller index
            else:
                j -= 1 #move towards smaller index in validSuff
        return -1
