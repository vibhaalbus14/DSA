from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #if in the window length 3,
        #atleast one zero is spotted , change all, if after one pass
        #zero contine to exist, ret -1

        flag=False #false=> no negate, true=> negate
        l=0
        r=2
        zeroes=0
        ones=0
        flips=0

        for i in range(3):#because 3 consecutive nos=> window size=3
            if nums[i]==0:#count the no of zeroes and ones
                zeroes+=1
            else:
                ones+=1
        if nums[0]==0:#make a flip only if zero is at the beginning of the window
            flips+=1
            flag=not flag
            ones,zeroes=zeroes,ones
        
        print("l,r,zeroes,ones",l,r,zeroes,ones)
        
        for r in range(3,len(nums)):
            print(nums[l:r])
            #remove the prev start
            if nums[l]==0:
                zeroes-=1
            else:
                ones-=1
            l+=1
            #include r, add new end
            if nums[r]==0:
                zeroes+=1
            else:
                ones+=1
            #xheck for the start of the window
            #flip only if   zero at the beginning of thw window
            print("l,nums[l]",l,nums[l])
            if nums[l]==0:
                flips+=1
                
                ones,zeroes=zeroes,ones
            print("l,r,zeroes,ones",l,r,zeroes,ones)

        print(flips)
        return -1 if zeroes!=0 else flips
    
#-----------------------------------------------------------------------------------------------
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #approach
        #1. use i , i+1, i+2 to make in place changes
        flips=0

        for i in range(len(nums)-2):
            if nums[i]==0:
                flips+=1
                nums[i],nums[i+1],nums[i+2]=int(not(nums[i])),int(not(nums[i+1])),int(not(nums[i+2]))
            
            
        if nums[-1]!=0 and nums[-2]!=0:
            return flips
        else:
            return -1



        
        