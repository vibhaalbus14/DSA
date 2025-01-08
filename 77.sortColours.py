class Solution(object):
    def sortColors(self, nums):
        #quick sort
        def swap(a,b,nums):
            nums[a],nums[b]=nums[b],nums[a]

        def helper(start,end,nums):
            if start>=end or end<start:
                return 
            pivot=start
            i=pivot+1
            j=end

            while i<=j:
                if nums[i]>nums[pivot] and nums[j]<=nums[pivot]:
                    swap(i,j,nums)
                elif nums[i]>nums[pivot]:
                    j-=1
                elif nums[j]<=nums[pivot]:
                    i+=1
                else:
                    i+=1
                    j-=1
            swap(j,pivot,nums)
            pivot=j
            helper(start,pivot-1,nums)
            helper(pivot+1,end,nums)
        helper(0,len(nums)-1,nums)
        return nums

obj=Solution()
print(obj.sortColors([0,2,2,2,0,2,1,1]))
            