
# #time complexity:O(n*m)
# #space complexity:O(m)
# class Solution(object):
#     def nextGreaterElement(self, nums1, nums2):
#         indexList=[]
#         greaterList=[]
#         count=0
#         for num in nums1:
#             if num in nums2:
#                 indexList.append(nums2.index(num))
#         for j in indexList:
#             i=j+1
#             count=0
#             while(i<len(nums2)):
#                 if nums2[i]>nums2[j]:
#                     greaterList.append(nums2[i])
#                     count=1
#                     break
#                 i+=1
#             if count==0:
#                 greaterList.append(-1)
#         return greaterList

# obj=Solution()
# print(obj.nextGreaterElement([4,1,2],[1,3,4,2]))

#time complexity:O(n+m)
#space complexity:O(m)
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        #stack is used to keep track of elements whose greater part is to be found out
        #hashmap is used to add the greatest element of a number in nums1 to its respective location
        hashmap={}
        stack=[]
        res=[-1]*len(nums1)#if greater element is not found, it has to be populated with -1
        for i,num in enumerate(nums1):
            hashmap[num]=i
        #loop through nums2
        for i in range (len(nums2)):
            currElement=nums2[i]
            while len(stack)!=0 and currElement>stack[-1]:
                #it means the next greater element currElement is found
                #hence pop stack[-1] value from stack
                #identify that numbers's index from hashmap and map into res
                numCompleted=stack.pop()
                index=hashmap[numCompleted]
                res[index]=currElement
            #all the numbers's greater elmenet need not be found out but 
            #only those which are in num1
            if currElement in nums1:
                stack.append(currElement)#this eventually creates a monotonic array
        return res

obj=Solution()
print(obj.nextGreaterElement([4,1,2],[1,3,4,2]))


