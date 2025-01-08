# #-----------------------------------dfs bactracking-----------------------------------
# from typing import List
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         rows=len(board)
#         cols=len(board[0])
#         adjList={}
                               
#         #create adjacency list
#         for i in range(rows):
#             for j in range(cols):
#                 adjList[(board[i][j],i,j)]=[] #since the values can be repeated, rows and cols are also used

#         #populate the adjacency list
#         for val,row,col in adjList:
#             #left,right,top , bottom
#             directions=[(0,-1),(0,1),(-1,0),(1,0)]
#             for r,c in directions:
#                 nr=row+r
#                 nc=col+c
#                 if 0<=nr<rows and 0<=nc <cols:
#                     adjList[(val,row,col)].append((board[nr][nc],nr,nc))

#         #identifying the first value in given word from board
#         finalList=[]
#         visited=set()#to add used up nodes
#         def helper(i,val,row,col,word):
#             #check if word[i] char is present in neighbours of (val,row,col)
#             if i>=len(word):
#                 return True
#             for value,r,c in adjList[(val,row,col)]:
#                 if word[i]==value and (value,r,c) not in visited:
#                     #second  letter found
#                     visited.add((value,r,c))
#                     if helper(i+1,value,r,c,word):
#                         return True
#                     visited.remove((value,r,c))
#             return False

#         for word in words:
#             visited.clear()
#             for val,row,col in adjList:
#                 if word[0]==val:
#                     visited.add((val,row,col))
#                     ans=helper(1,val,row,col,word)
#                     if ans:
#                         finalList.append(word)
#                         break
#                     if not ans:
#                         visited.remove((val,row,col))#because all other will be removed already

#         return finalList
# #eg: "aaa"=> can cause infinite usage, so keep track of visted nodes

#-----------------------approach:trie and dfs bactracking-------------------------
#here rather than looping through words and then dfs the board
#we create a trie of words to be searched
#then we compare the nodes and r,c
from typing import List
class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root=TrieNode()

        def insertWords(word):
            curr=root
            for c in word:
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.endOfWord=True

        #creating a prefix tree
        for word in words:
            insertWords(word)
        
        #dfs through loop 
        #store the words so formed in res
        #mark the board[r,c] visited
        #compare the value on board to the children of the node passed
        #go to that node
        #backtrack and make the node unvisited
        def dfs(row,col,node,currWord):
            if board[row][col] not in node.children:
                return
            visited.add((row,col))
            #navigate to that child of the node that matches the value of r,c on board
            node=node.children[board[row][col]]
            #concatenate the word formed so far
            currWord+=board[row][col]
            if node.endOfWord==True:
                res.add(currWord)
            #now navigate through adjacent 4's only if valid and not visited
            #left,right,top , bottom
            directions=[(0,-1),(0,1),(-1,0),(1,0)]
            for r,c in directions:
                nr=row+r
                nc=col+c
                if 0<=nr<rows and 0<=nc <cols and (nr,nc) not in visited:
                    dfs(nr,nc,node,currWord)
            visited.remove((row,col))
            

        #loop through every row and col
        rows=len(board)
        cols=len(board[0])
        visited=set()
        res=set()
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        
        return list(res)

#-------------------------------trie,backtrack,adj list-------------------------
from typing import List
class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root=TrieNode()

        def insertWords(word):
            curr=root
            for c in word:
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.endOfWord=True

        #creating a prefix tree
        for word in words:
            insertWords(word)
        
        adjList={}
        rows=len(board)
        cols=len(board[0])
        res=set()
        visited=set()                    
                        
        #create adjacency list
        for i in range(rows):
            for j in range(cols):
                adjList[(board[i][j],i,j)]=[] #since the values can be repeated, rows and cols are also used

        #populate the adjacency list
        for val,row,col in adjList:
            #left,right,top , bottom
            directions=[(0,-1),(0,1),(-1,0),(1,0)]
            for r,c in directions:
                nr=row+r
                nc=col+c
                if 0<=nr<rows and 0<=nc <cols:
                    adjList[(val,row,col)].append((board[nr][nc],nr,nc))
        
        def dfs(key,currWord,node):
            val,r,c =key
            if val not in node.children:
                return
            visited.add(key)
            currWord+=val
            node=node.children[val]
            if node.endOfWord:
                res.add(currWord)
            #go through the neighbours
            for neighbour in adjList[key]:
                if neighbour not in visited:
                    dfs(neighbour,currWord,node)
            visited.remove(key)#backtrack

        
        for key in adjList:
            dfs(key,"",root)

        return list(res)