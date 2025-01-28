class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        #approach
        #1.since there are no cycles in prerequisites,all courses are doable
        #2.sort the nodes in topological order
        #3.if index(u)>index(v) return true if not false
        #4.if no prerequisites, return an array of false = len(queries)

        #form an adjacency list from prerequisites

        if not prerequisites:
            return [False for _ in range(len(queries))]
        
        d={ i:[] for i in range(numCourses)}
        for u,v in prerequisites:
            d[u].append(v)

        #since the edges can be indirect
        for key in d:
            for neigh in d[key]:
                d[key].extend(d[neigh])

        #remove duplicates and form indegree
        indegree=[0 for i in range(numCourses)]
        for key in d.keys():
            d[key]=set(d[key])
            for neigh in d[key]:
                indegree[neigh]+=1
        
        #caution: topological sort isnt unique so relying just on indices of one arrangement
        #cannot produce the correct result
        #hence, maintain a list of all nodes taht have the same degree, 
        #indicating they can be flipped
        nodesIndegreeLevel=indegree[:]

        usedUp=set()
        sortedNodes=[]
        #topological sort
        #remove that node which has 0 indegree and reduce the contribution of that node to all
        #connected nodes
        print(indegree)
        count=0
        while count<numCourses:
            for i in range(len(indegree)):
                if indegree[i]==0:
                    if i not in usedUp:
                        usedUp.add(i)
                        sortedNodes.append(i)
                        if d[i]!=[]:
                            for neighbour in d[i]:
                                #decrement its indegree value
                                indegree[neighbour]-=1
            #since one element is added,inc count
            count+=1
            
        print(sortedNodes)
        output=[]
        #checking if u is a prerequisite of v
        for u,v in queries:
            if nodesIndegreeLevel[u]==nodesIndegreeLevel[v]:#if they can be flipped,the order of index in sortedlist doesnt matter
                output.append(False)
            else:
                uIndex=sortedNodes.index(u)
                vIndex=sortedNodes.index(v)
                output.append(uIndex<vIndex)
        return output

#----------------------------approach 2--------------------------------------
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #see if must can reach take, if yes=> true

        adjList=defaultdict(list)
        for must,take in prerequisites:
            adjList[must].append(take)
       
        storedTable={}
        for i in range(numCourses):
            storedTable[i]=set()
        visited=set()
        #run this function once to map all children to parent
        @cache
        def dfs(node):
            currSet=set()
            if node in adjList:
                for neighbour in adjList[node] :
                    #if neighbour not in visited:
                    visited.add(neighbour)
                    currSet.update(dfs(neighbour))
                    currSet.add(neighbour)

            storedTable[node].update(currSet)
            return currSet
        
        for i in range(numCourses):
            if i not in visited:
                visited.add(i)
                dfs(i)
        #print(storedTable)

        ans=[]
        for must,take in queries:
            ans.append(take in storedTable[must])
        return ans
                
        