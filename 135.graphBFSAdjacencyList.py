from collections import deque
#say A is the start
adjacencyList = {
    'A': ['B', 'F'],
    'B': ['A', 'F', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'B', 'E']
}

#approach:
#note: every node is visited once and hence loop / cyclicity is to be avoided
#1.start from a node
#2.append that node to deque and to visited
#3.ehile the deque is not empty
#4.pop from left in the deque and append it to op array
#5.loop through its neighbours from its key i.e a list
#6.as long as neighbours are not visited, add them to deque and mark them visited
#7.if visited, skip to avoid loops


def BFS(adjacencyList,start):
    dq=deque()
    output=[]
    visited={}

    dq.append(start)
    visited[start]=1 #means visited
    while dq:
        node=dq.popleft() #popping left from deque
        output.append(node) #appending the value to op
        #go through its neighbours from adjacency list
        if node in adjacencyList: #cause sometimes if no edges exist , need not be included in adjacencyList
            for neighbour in adjacencyList[node]:
                if neighbour not in visited:
                    dq.append(neighbour)
                    visited[neighbour]=1
    print("visited :",visited)
    return output

print(BFS(adjacencyList,'C'))