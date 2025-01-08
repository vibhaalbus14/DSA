class Solution(object):
    def intersection(self, nums1, nums2):
        
        intersection_list=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    intersection_list.append(nums1[i])
                    nums2[j]==1001
                    break
        return  list(set(intersection_list))
object=Solution()
print(object.intersection([1,2,2,1],[2,2]))

# set1=set(nums1)
# set2=set(nums2)
# return list(set1 & set2)

        