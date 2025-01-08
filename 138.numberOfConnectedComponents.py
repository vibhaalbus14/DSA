# time comp:O(v+e)=>dfs
# #space comp: O(v+e)=> adjacency list

#approach
#1.form the adjacency list from given list
#2.loop through every node
#3.as long as the node is not visited inc components  count and call dfs
#4.the number of times dfs is called on nodes=no of components as one traversal can cover all nodes if
#all are connected
from collections import defaultdict

def createAdjList(d,n,edges):
    for start,end in edges:
        d[start].append(end)
    return d

def dfsTrav(node,visited,d):#rec
    visited.append(node) #make the node visited
    #visit its children
    if node in d:
        for neighbour in d[node]:
            if neighbour not in visited:
                dfsTrav(neighbour,visited,d)

def countComponents(n,edges):
    d=defaultdict(list)
    visited=[]
    compCount=0
    createAdjList(d,n,edges)
    for i in range(n):
        if i not in visited:
            compCount+=1
            dfsTrav(i,visited,d)
    return compCount
print(countComponents(7,[[0,1],[1,2],[3,4],[5,6],[3,5],[3,6],[1,3]]))