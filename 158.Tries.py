#every node of trie doesnt have a value
#rather the parent stores the value in hashmap as key and will contain the address of the node as value
class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False
#how are redudant nodes  avoided?
#i.e apple begins with a ans so does ape
#so rather than making the root point to 2 a's all a's are stored as one node
#and they further point to the next character

#now why is self.word needed?
#self. word is used to mark the ending word (of node) that we have inserted
#say we have inserted apple
#once its done , we mark e node's word to be true saying that apple is inserted and its end is e node
#we need to check if ap is inserted
#we traverse through the trie
#since ap is a part of apple,it obviously exists
#but ap is not inserted as a separate word, its part of someother word
#hence when we return p nodes's word, it is false cause it was never inserted in the first place

#so, to distinguish bw actual inserted words and words that just exist but not inserted,
#we mark the end node as true or false
class Trie:
    def __init__(self):
        self.root=TrieNode() #the root is always an empty node in trie
    
    #time comp=O(n)
    def insert(self,word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.word=True #saying that the word is inserted by us and marking its end

    #time comp=O(n)
    def search(self,word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return curr.word
    
    #time comp=O(n)
    def searchPrefix(self,prefix):
        curr=self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return True #here its true and not curr.word as we are only checking if prefix exists
    #be it a whole word or a part of a word

#hashmaps over search?
#prefix search means in hashmap iterate through prefix of say length m and iterate through word in 
#hashmap of length n=>time comp=O(n*m)
#in trie it is only O(m) since all nodes are present only once