from typing import List
class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        #approach
        #1.flatten the cells acrosss rows and cols
        #2.loop through the respective arrays to find the pattern
        #4.if pattern is found, add the cell nos to respective sets, and take intersections
        m=len(grid)
        n=len(grid[0])
        p=len(pattern)
        if p>m*n: #len pattern is greater than available cells
            return 0

        horzSet=set()
        vertSet=set()

        horz,vert=[],[]
        horzName,vertName=[],[]

        #mark the cells and append them to rows first
        k=0
        for i in range(m):
            for j in range(n):
                grid[i][j]=(grid[i][j],k)#naming cells in place=> (val,name)
                horz.append(grid[i][j][0])
                horzName.append(grid[i][j][1])
                # print("changed cell,", grid[i][j])
                k+=1

        for j in range(n):
            for i in range(m):
                vert.append(grid[i][j][0])
                vertName.append(grid[i][j][1])
        
        # print("vert array",vert)
        # print("horz array",horz)
        # print("vertName array",vertName)
        # print("horzName array",horzName)
        #sliding window to compare
        horz="".join(horz)
        vert="".join(vert)
        def slidingWindow(currSet,array,arrayName):
                l=0
                r=p-1
                windowHash=0
                # print()
                # print("inside")


                #compute the hash of the current window
                for i in range(l,r+1):
                    windowHash=((windowHash*base)+ord(array[i]))%prime
                    #print("winHash",windowHash)
                
                #print("array, pattern",windowHash,pHash)
                if windowHash==pHash:
                    for k in range(l,r+1):
                        currSet.add(arrayName[k])

                power=pow(base,p-1,prime)
                for r in range(p,len(array)):
                    windowHash=(windowHash-(ord(array[l])*power))%prime #remove the effect of left most char
                    l+=1
                    windowHash=(windowHash*base+ord(array[r]))%prime #add the effect of rightmost char
                    #print("array, pattern",windowHash,pHash)
                    if windowHash==pHash:
                        #append all the cells into respective set
                        for k in range(l,r+1):
                            currSet.add(arrayName[k]) #add the name of the cell
    
        #compute the pattern hash
        pHash=0
        base=256
        prime=10**9+7 #some prime number
        for char in pattern:
            pHash=((pHash*base)+ord(char))%prime #this keeps in mind the sum but not the order of chars
        slidingWindow(horzSet,horz,horzName)
        slidingWindow(vertSet,vert,vertName)

        # print()
        # print("horz set",horzSet)
        # print("vert set",vertSet)
        count=0
        for num in horzSet:
            if num in vertSet:
                count+=1
        return count







        