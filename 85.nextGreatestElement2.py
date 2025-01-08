#----------------------------approach1 nested loops----------------------------
#  class Solution(object):
#     def nextGreaterElements(self, nums):
#         maxList=[]
#         for i in range(len(nums)):
#             count=0
#             j=(i+1)%len(nums)
            
#             while(j!=i):#one full circle
#                 if nums[j]>nums[i]:
#                     maxList.append(nums[j])
#                     count=1
#                     break
#                 j=(j+1)%len(nums)
#             if count!=1:
#                 maxList.append(-1)
#         return maxList        
# obj=Solution()
# print(obj.nextGreaterElements([1,2,3,4,3]))

#----------------------------approach2 using stack----------------------------
class Solution(object):
    def nextGreaterElements(self, nums):
        numsAdd=nums+nums #circular search
        n=len(nums)
        res=[-1]*len(nums)
        stack=[] #it is a list of tuples i.e  tuples=(val,index)

        for i,num in enumerate(numsAdd):
            while stack and num>stack[-1][0]:
                #one circle is done and the element is being reached again
                #it has no greater element and is harming other elements in stack to find their greater elements
                #so pop without mapping into result
                # if stack[-1][1]+n>=i:
                #     break
                #tuple=stack.pop()     
                # #the above isnt needed as it doesnt matter even if elments are left out in stack                     
                res[tuple[1]]=num #to pop and add to result
            if i<n:
                stack.append((num,i))
        return res
obj=Solution()
print(obj.nextGreaterElements([1,2,3,4,3]))
