class Solution(object):
    def captureForts(self, forts):
        n=len(forts)
        max_count=0
        for index in range(n):
            if(forts[index]==1):
                #check by moving the pointer towards right
                count=0
                for ptr in range(index+1,n):
                    if forts[ptr]==0:
                        count+=1
                    elif forts[ptr]==-1:
                        #stop
                        max_count=max(count,max_count)
                        break
                    else:
                        break

                # check by moving the pointer towards left 
                count=0
                for ptr in range(index-1,-1,-1):
                    if forts[ptr]==0:
                        count+=1
                    elif forts[ptr]==-1:
                        #stop
                        max_count=max(count,max_count)
                        break
                    else:
                        break
        return max_count
object=Solution()
print(object.captureForts([1,0,0,-1,0,0,0,0,1]))
                        
            



        