class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        finalList=[]
        #function to check if a palindrome
        def checkPalindrome(l,r):
            while(l<r):
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
                
            return True
            #return s==s[::-1]#slice backwards
           

            
            
        #function to pass substrings
        def helper(start,sublist):
            #base
            if(start==len(s)):#end of string reached
                finalList.append(sublist[:])
            for i in range (start,len(s)):
                if checkPalindrome(start,i):
                    sublist.append(s[start:i+1])#pass substring to checkPalindrome
                    helper(i+1,sublist)
                    sublist.pop()
        helper(0,[])
        return finalList
obj=Solution()
print(obj.partition("aab"))
                 
            
                