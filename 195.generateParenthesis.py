from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesisList=[]
        for _ in range(n):
            parenthesisList.append("(")
            parenthesisList.append(")")
        #parenthesisList="".join(parenthesisList)
        #similar to combinations
        #include and exclude
        
        def helper(i):
            if i==len(parenthesisList)-1:
                return [parenthesisList[i]]
            # if i>len(parenthesisList):
            #     return
            parentList=[]
            childList=helper(i+1)
            for subList in childList:
                #insert at all possible places
                for i in range(len(subList)):
                    copyList=[]
                    for char in subList:
                        copyList.append(char)
                    copyList.insert(i,parenthesisList[i])
                    parentList.append("".join(copyList))
            return parentList
   
        return helper(0)         
