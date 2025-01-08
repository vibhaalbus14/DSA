# # Definition for a binary tree node.
# from collections import deque
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution(object):
#     def sortedArrayToBST(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: TreeNode
#         """
#         n=len(nums)
#         if  n==1:
#             root=TreeNode(nums[0])
#             return root

#         #identify the root position
#         mid=int(n/2)
#         root=TreeNode(nums[mid])
#         dq=deque()
#         dq.append((root,"b"))#b indicates both left and right children to be added
#         left=mid-1
#         right=mid+1

#         while dq:
#             print(dq)
#             tup=dq.popleft()
#             node=tup[0]
#             children=tup[1]

#             if children=="b":
#                 if left>-1 and nums[left]:
#                     node.left=TreeNode(nums[left])
#                     dq.append((node.left,"l"))
#                     left-=1
                
#                 if right<n and nums[right]:
#                     node.right=TreeNode(nums[right])
#                     dq.append((node.right,"r"))
#                     right+=1
                
#             elif children=="l": #only left child
#                 if left>-1 and nums[left]:
#                     node.left=TreeNode(nums[left])
#                     dq.append((node.left,"l"))
#                     left-=1
#             else:
#                 if right<n and nums[right]: #only right child
#                     node.right=TreeNode(nums[right])
#                     dq.append((node.right,"r"))
#                     right+=1

#         return root

# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #recursively identify the middle of array and make it the corresponding node
        #since its sorted,bst is verified
        #since the middle element is being considered , height remains balanced
        def helper(array):
            n=len(array)
            #base case
            if n==1:#single node
                node=TreeNode(array[0])
                return node
            mid=int(n/2)
            node=TreeNode(array[mid])
            node.left=helper(array[:mid])
            node.right=helper(array[mid+1:])
            return node
        return helper(nums)