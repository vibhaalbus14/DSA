from collections import deque
#say A is the start
adjacencyMatrix = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 0]
]

#approach:
#note: every node is visited once and hence loop / cyclicity is to be avoided
#1.start from a node
#2.append that node to deque and to visited
#3.ehile the deque is not empty
#4.pop from left in the deque and append it to op array
#5.loop through its neighbours from its key i.e a list
#6.as long as neighbours are not visited, add them to deque and mark them visited
#7.if visited, skip to avoid loops


def BFS(adjacencyMatrix,start):
    dq=deque()
    output=[]
    visited={}

    dq.append(start)
    visited[start]=1 #means visited
    while dq:
        node=dq.popleft() #popping left from deque
        output.append(node) #appending the value to op
        #go through its neighbours from adjacency list
        for neighbour in range(len(adjacencyMatrix[node])):
                if adjacencyMatrix[node][neighbour]==1 and neighbour not in visited:
                    dq.append(neighbour)
                    visited[neighbour]=1
    print("visited :",visited)
    return output

print(BFS(adjacencyMatrix,0))