#given a graph(can be directed or unidirected) as list
# to form an adjacency list using dict
# to form an adjacency matrix using 2d array

#consider this given
graph=[[0,1],[0,3],[1,2],[3,4],[3,6],[3,7],[4,5],[4,2],[5,2]] #directional
n=8 #0-7

#to form an adjacency matrix
#adjacencyMatrix=[[0]*n]*n #creates list of references, hence all the values remain the same
adjacencyMatrix=[[0 for _ in range(n)] for _ in range(n)]

for start,end in graph:
    adjacencyMatrix[start][end]=1 #saying edge exists bw start->end
    #if it is non directional, both ways
    #adjacencyMatrix[end][start]=1
print(adjacencyMatrix)

#to form an adjacencyList
from collections import defaultdict
adjacencyList=defaultdict(list) #dict values are in the form of list

for start,end in graph:
    adjacencyList[start].append(end)
print(adjacencyList)

#adv of adjacencyList over adjacencyMatrix is looping over zeroes can be avoided