from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #--------------------------4^n-----------------------------------
        if sum(matchsticks)%4!=0:
            return False
        matchsticks.sort(reverse=True)
        
        overallSum=sum(matchsticks)
        sideLength=overallSum//4
        
       
        def backtrack(index,currLength,visited,count):
            nonlocal sideLength

            if currLength==sideLength:
                if count==3:#already 3 sides completed, this is 4th side
                    return True
                else:
                    #visit the unvisited index
                    #initiating call to identify next side
                    # for i in range(len(matchsticks)):
                    #     if i not in visited:
                    #         return backtrack(i,matchsticks[i],visited,count+1)
                            #try out another start index
                    return backtrack(0,0,visited,count+1)
            if index>=len(matchsticks):
                return False
            #try adding current matchstick
            diff=sideLength-currLength
            # for i in range(index,len(matchsticks)):
            if index not in visited and matchsticks[index]<=diff:
                #use this matchstick
                visited.add(index)
                res=backtrack(index+1,currLength+matchsticks[index],visited,count)
                if res:
                    visited.remove(index)
                    return True
                visited.remove(index)
            
            return backtrack(index+1,currLength,visited,count)
            


        return backtrack(0,0,set(),0)

        #----------------------optimised approach=> 4^n-----------------------------------------------
        #1.use an array of 4 sides 
        #2.take a matchstick and see to which side to can be used for
        #3.if we dont reach the end of matcsticks with all sides equal, it means
        #matchsticks are placed in wrong manner, try placing the same
        #matchstick in different side

        if sum(matchsticks)%4!=0:
            return False
        matchsticks.sort(reverse=True)
        
        overallSum=sum(matchsticks)
        sideLength=overallSum//4

        array=[0]*4 #array of 4 sides

        def dfs(index):
            if index==len(matchsticks):
                if all(side==sideLength for side in array):
                    return True
                else:
                    return False

            #try the same index matchstick in all 4 sides
            for i in range(4):
                if matchsticks[index]+array[i]<=sideLength: #valid addition
                    array[i]+=matchsticks[index]
                    #call next matchstick
                    if dfs(index+1):
                        return True
                    #if not, continue placing in other sides
                    #remove current matchstick added to current side
                    array[i]-=matchsticks[index]
                
            return False

        return dfs(0)
                    
                  





        
