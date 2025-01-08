class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #approach
        #2 pointers
        L,rH,rN=0,0,0
        while rN<len(needle) and rH<len(haystack) and L<=rH:
            if haystack[rH]==needle[rN]:
                rH+=1
                rN+=1
            else:
                L+=1
                rH=L
                rN=0
        
        if rN>=len(needle):
            return L
        else :
            return -1
obj=Solution()
print(obj.strStr("leetcode","leeto"))

