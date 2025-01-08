# #time complexity:O(n^2)
# #space complexity:O(1)
# class Solution(object):
#     def maxArea(self, height):
#         max_area=0
#         for i in range(len(height)):
#             for j in range(i+1,len(height)):
#                 if height[i]<=height[j]:
#                     depth=height[i]
#                 else:
#                     depth=height[j]
#                 area=(j-i)*depth
#                 max_area=max(max_area,area)
#         return max_area
# object=Solution()
# print(object.maxArea([1,8,6,2,5,4,8,3,7]))

#-----------------------------------------------------------------------------------------------------
# #time complexity:O(n)
# #space complexity:O(1)
class Solution(object):
    def maxArea(self, height):
        left,right,max_area=0,len(height)-1,0

        while(left<right):
            area=min(height[left],height[right])*(right-left)
            max_area=max(max_area,area)

            #since the depth of the water is determined by the lowest height,to maximise this,surpass the
            #current lowest height

            if(height[left]<=height[right]):
                left+=1
            else:
                right-=1
            #if left==right, considering same line twice=>no valid container and area is zero.Hence stop
        return max_area
object=Solution()
print(object.maxArea([1,8,6,2,5,4,8,3,7]))



