from typing import List
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #build adj list
        #no need to check prerequisite transitivity
        #dfs will handle
        #but if using topological sorting,since no unique sorting is present
        #using topological sorting wont be ideal to solve this

        adjList={}
        for i in range(numCourses):
            adjList[i]=[]

        for must,take in prerequisites:
            adjList[must].append(take)

        def dfs(start,end):
            visited=set()
            visited.add(start)
            def helper(node):
                flag=False
                if node==end:
                    return True
                for neighbour in adjList[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        flag=flag or helper(neighbour)
                        #why or? even if end is found in one of the branches,its found .Hence, OR
                    
                return flag
            return helper(start)
        
        res=[]
        for start,end in queries:
            res.append(dfs(start,end))
        return res

        