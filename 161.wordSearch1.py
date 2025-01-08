from typing import List
class TrieNode:
    def __init__(self):
        self.children={}
        self.isEndOfWord=False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        root=TrieNode()

        def insert(word):
            curr=root
            for c in word:
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.isEndOfWord=True

        insert(word)#here only one word is inserted into trie

        op=set()
        visited=set()
        #dfs func 
        def dfs(row,col,currWord,node):
            if board[row][col] not in node.children:
                return False
            visited.add((row,col))
            currWord+=board[row][col]
            if currWord==word:
                return True
            node=node.children[board[row][col]]
            #go through its adjacent neighbours
            directions=[(0,-1),(0,1),(-1,0),(1,0)]
            for r,c in directions:
                nr=row+r
                nc=col+c
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited:
                    if dfs(nr,nc,currWord,node):
                        return True
            visited.remove((row,col))
            return False
            
        #dfs the entire matrix
        rows=len(board)
        cols=len(board[0])
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,"",root):
                    return True
        return False      