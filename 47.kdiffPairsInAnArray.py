class Solution(object):
    def findPairs(self, nums, k):
        dict={}
        count=0
        #map all the elements with their freq in dictionary
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        #add the diff to element in dict,if this element is found , inc count that is equal to saying
        #the original num and its counterpart, the pair is present
        for num in dict:
            if k>0 and num+k in dict:
                count+=1
            else:
                # if k==0 this means this pair is possible only if the same nos are subtracted
                #this means purely counting the elements with freq greater than 1
                if k==0 and dict[num]>1:
                    count+=1
        return count
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if abs(nums[i]-nums[j])==k:
        #             if [nums[i],nums[j]]  not in final_list and [nums[j],nums[i]] not in final_list:
        #                 final_list.append([nums[i],nums[j]])
        
        # print(final_list)
        # return len(final_list)
object=Solution()
print(object.findPairs([3,1,4,1,5],2))


        