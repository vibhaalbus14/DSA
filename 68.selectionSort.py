def selection_sort(nums):
    for i in range (len(nums)-1):#to loop through the array
        temp=nums[i]
        minPos=i
        for j in range(i+1,len(nums)): #to update the min element
            if nums[j]<nums[minPos]:
                minElement=nums[j]
                minPos=j
        nums[i],nums[minPos]=nums[minPos],temp
    return nums
print(selection_sort([7,4,5,9,8,2,1]))
print(selection_sort([]))
print(selection_sort([7,4,-5,-2,6,6,9]))
