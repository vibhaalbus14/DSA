#--------------------------recursion---------------------------
class Solution(object):
    def findTargetSumWays(self, nums, target):
        self.nums=nums
        self.n=len(nums)
        self.res=0
        self.target=target
        return self.recFunc(0,0)
        
    
    def recFunc(self,index,curr_sum):
        
        if(index==self.n and curr_sum==self.target):
            #self.res+=1
            res+=1
        elif(index>self.n-1):
            return 0
        else:
            #minus step/exclude step
            self.recFunc(index+1,curr_sum-self.nums[index])
            #addition step/ inclusion step
            self.recFunc(index+1,curr_sum+self.nums[index])
            return self.res

    
object=Solution()
print(object.findTargetSumWays([1], 1))

#using dictionary for memoization as the number of
# column values are not known since curr_sum can be negative too

#-------------------------------memoization----------------------------------
class Solution(object):
    def findTargetSumWays(self, nums, target):
        self.nums=nums
        self.n=len(nums)
        #self.res=0
        self.target=target
        self.ht={}
        return self.recFunc(0,0)
        
    
    def recFunc(self,index,curr_sum):
        
        if(index==self.n and curr_sum==self.target):
            #self.res+=1
            return 1
        elif(index>self.n-1):
            return 0
        else:
            if (index,curr_sum) in self.ht:
                return self.ht[(index,curr_sum)]
            
            else:
                #minus step/exclude step
                sub=self.recFunc(index+1,curr_sum-self.nums[index])
                #addition step/ inclusion step
                add=self.recFunc(index+1,curr_sum+self.nums[index])
                self.ht[(index,curr_sum)]=sub+add
                return self.ht[(index,curr_sum)]

    
object=Solution()
print(object.findTargetSumWays([1], 1))

