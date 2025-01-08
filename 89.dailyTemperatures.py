class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack=[] #storing tuples i.e (val,index)
        ans=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                #add the difference into respective res position
                tuple=stack.pop()
                ans[tuple[1]]=i-tuple[1]
            #since the temp's greater should also be found, add into stack
            stack.append((temp,i))
        return ans


obj=Solution()
print(obj.dailyTemperatures([73,74,75,71,69,72,76,73]))
#print(obj.dailyTemperatures())