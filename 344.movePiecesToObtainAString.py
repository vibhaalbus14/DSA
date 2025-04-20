class Solution:
    def canChange(self, start: str, target: str) -> bool:
        #approach
        #1.no need to check for "_" if in the beginning both order of l and r and count of l and r are checked
        #2.this reduces check for "_" and makes it optimised

        #if dest<curr for r => false
        #if dest > curr for L => False
        #if for L => dest:curr all blank => True
        #if for R => curr+1:dest+1 sll blank =.True
        if start==target:
            return start==target
        
        #check if all chars are the same
        #order of chars are the same
        if start.replace("_","")!=target.replace("_",""):
            return False

        #targetList=[]
        #startList=[]
        targetL=[]
        targetR=[]
        startL=[]
        startR=[]

        for i,char in enumerate(target):
            #targetList.append(char)
            if char=='L':
                targetL.append(i)
            elif char=='R':
                targetR.append(i)
            

        for i,char in enumerate(start):
            #startList.append(char)
            if char=='L':
                startL.append(i)
            elif char=='R':
                startR.append(i)


        for index in range(len(startL)):
            curr=startL[index]
            dest=targetL[index]

            if dest>curr:
                return False
            #check if all are blank spaces
            # for char in range(dest,curr):
            #     if startList[char]!="_":
            #         return False
            # #make in place changes to start
            # startList[dest],startList[curr]=startList[curr],startList[dest]

            
        for index in range(len(startR)):
            curr=startR[index]
            dest=targetR[index]

            if dest<curr:
                return False
            #check if all are blank spaces
            # for char in range(curr+1,dest+1):
            #     if startList[char]!="_":
            #         return False
            # startList[dest],startList[curr]=startList[curr],startList[dest]


            
        return True
        



        