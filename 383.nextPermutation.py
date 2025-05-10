from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #[[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
        #check from last i and i-1
        #till index 0
        n=len(nums)
        i=n-2

        def nextGreaterElement(num,array):
            array.sort()
            l=0
            r=len(array)-1

            while l<=r:
                mid=(l+r)//2
                if array[mid]>num:
                    r=mid-1
                else:

                    l=mid+1
            return array[l]

        def sortRemElements(num,startIndex):
            newTempArray=[]
            #remove one occ of num  fromo given startIndex till end
            curr=False
            for i in range(startIndex,n):
                if nums[i]==num and not curr:
                    curr=True #removed one occ of num
                else:
                    newTempArray.append(nums[i])
            newTempArray.sort()

            return newTempArray

        while i>=0:
            if nums[i]>=nums[i+1]:
                i-=1

            elif i==n-2:#swapping can be done only at the last 2 pos
                nums[i],nums[i+1]=nums[i+1],nums[i]#swap
                return
            else: #somewhere in bw or start
                #identify the next greater Element of nums[i]
                next=nextGreaterElement(nums[i],nums[i:])
                temp=sortRemElements(next,i)
                # nums[:]=nums[0:i]+[next]+temp
                nums[i]=next
                index=0

                for j in range(i+1,n):
                    nums[j]=temp[index]
                    index+=1
                return

        #since swap didnt occur
        #return the ascending order
        newNums=nums[:]
        newNums.sort()
        for i in range(n):
            nums[i]=newNums[i]






