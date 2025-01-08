class Solution(object):
    def simplifyPath(self, path):
        prepList=path.split('/')
        finalList=[]
         
        top=0 #points to prepList
        while(top<len(prepList)):
            if prepList[top]==".":
                pass #no addition to finalList
            elif prepList[top]=="..":
                finalList.append("..")
            elif prepList[top]=="": #indicates multiple slashes
                pass
            else:
                finalList.append(prepList[top])
            top+=1
        
        #now the finalList only has ..
        top=0
        simplifiedList=[]
        while top<len(finalList):
            if finalList[top]=="..":
                if len(simplifiedList)!=0:#as long as it isnt empty
                    simplifiedList.pop()
            else:
                simplifiedList.append(finalList[top])
            top+=1

        str=("/").join(simplifiedList)
        
        return "/"+str #since the path must start with /
        
obj=Solution()
print(obj.simplifyPath("/a/./b/../../c/"))