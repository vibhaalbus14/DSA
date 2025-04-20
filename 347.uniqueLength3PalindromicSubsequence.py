class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count=0
        uniqueChar=set()
        for char in s:
            uniqueChar.add(char)

        for char in uniqueChar:
            firstOccIndex=s.find(char)
            lastOccIndex=s.rfind(char)

            if firstOccIndex!=lastOccIndex: #more than 1 occ
            #count unique chars in bw
                uniqueInBwChars=set(s[firstOccIndex+1:lastOccIndex])
                count+=len(uniqueInBwChars)
        return count

    
        
