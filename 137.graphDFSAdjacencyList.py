#there is no one unique soln to dfs travel
#many solns available
#depends on the way we travel through the neighbours
#--------------------------recursively---------------------------
#Time comp=O(v+e)
#space comp=O(v) => rec call stack worst case(like ll) and visited
adjacencyList={
    'A': ['B', 'F'],
    'B': ['A', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'E']
}
output=[]
visited={}
#no need of deque since the order of neighbours is not to be maintained
def DFS(start):
    #add to op
    #add to visited
    output.append(start)
    visited[start]=1
    #go through its neighbour, for every neighbour, call its children
    for neighbour in adjacencyList[start]:
        if neighbour not in visited:
            DFS(neighbour)
    return output
print(DFS('A'))
#--------------------------iteratively---------------------------
#Time comp=O(v+e)
#space comp=O(v) => rec call stack worst case(like ll) and visited
# adjacencyList={
#     'A': ['B', 'F'],
#     'B': ['A', 'C'],
#     'C': ['B', 'E', 'D'],
#     'D': ['C', 'E'],
#     'E': ['D', 'C', 'F'],
#     'F': ['A', 'E']
# }
# def DFS(start):
#     stack=[]
#     visited=[]
#     stack.append(start)
#     visited.append(start)
#     output=[]
#     while stack:
#         node=stack.pop()
#         output.append(node)
#         for neighbour in adjacencyList[node]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 stack.append(neighbour)
#     return output
# print(DFS('A'))

