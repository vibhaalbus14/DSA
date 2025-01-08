class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.word=True
        

    def search(self, word: str) -> bool:
        curr=self.root
        def helper(i,curr):
            if i>=len(word):
                return curr.word
            
            elif i<len(word):
                if word[i]==".":
                    if not curr.children:
                        return False
                    for key in curr.children:
                        if  helper(i+1,curr.children[key]):
                            return True
                    return False
                        
                elif word[i] not in curr.children:
                    return False
                else:
                    return helper(i+1,curr.children[word[i]])
        return helper(0,curr)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)