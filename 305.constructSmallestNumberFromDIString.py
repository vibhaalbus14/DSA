class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res=[]
        nums=[i+1 for i in range(10)]
        visited=set()

        def backtrack(index):
            nonlocal res,visited
            if len(visited)>len(pattern)+1:
                return False
            if len(visited)==len(pattern)+1:
                return True
            
             
            for num in nums:
                if num in visited: 
                    continue
                
                if pattern[index]=='I':
                    #choose curr num such that it is greater than the top
                    #char of res
                    if int(res[-1])<num:
                        res.append(str(num))
                        visited.add(num)
                        if backtrack(index+1):
                            return True
                        visited.remove(num)
                        res.pop()
                else:
                    #choose the curr num such that it is less that top of res
                    if int(res[-1])<num:
                        return False#all further elements will be greater onlt
                    else:
                        res.append(str(num))
                        visited.add(num)
                        if backtrack(index+1):
                            return True
                        visited.remove(num)
                        res.pop()
                
        for num in nums:
            res.append(str(num))
            visited.add(num)
            if backtrack(0):
                return "".join(res)
            res.pop()
            visited.remove(num)
                    
            
        