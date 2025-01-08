# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
# #--------------brute force approach-------------------------
#         def getLength(a):
#             return len(a)
#         if len(s)==0:
#             return 0
#         val=""
#         finalList=set()
#         for j in range(len(s)):
#             for i in range(j,len(s)):
#                 if s[i] in val:
#                     finalList.add(val)
#                     val=s[i]
                    
#                 else:
#                     val+=s[i]
                    
#                 if i==len(s)-1:
#                         finalList.add(val)
#                         val=""
#         print(finalList)
#         finalList=list(map(getLength,finalList))
#         print(finalList)
#         return max(finalList)
# obj=Solution()

# # print(obj.lengthOfLongestSubstring("dvdf"))
# # print(obj.lengthOfLongestSubstring("abcabcbb"))
# print(obj.lengthOfLongestSubstring("asjrgapa"))

#----------------------------approach2--------------------------
from collections import deque
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n==0 or n==1:
            return n
        right=left=0
        maxLength=0
        window=deque()

        while right<n and left<=right:
            if s[right] not in window:
                window.append(s[right])
                maxLength=max(maxLength,right-left+1)
                print(maxLength)
                right+=1
                print("right :", right)
            else:
                while window:
                    window.popleft()
                    left+=1
                    print("left :", left)
                    if s[right] not in window:
                        break
                
        return maxLength

obj=Solution()

print(obj.lengthOfLongestSubstring("dvdf"))
#print(obj.lengthOfLongestSubstring("abcabcbb"))
