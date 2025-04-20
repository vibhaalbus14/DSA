class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #sliding window

        #map char to index
        st="abc"
        hashMap={}
        for i,char in enumerate(st):
            hashMap[char]=i
        #use list to trace occ of chars
        alpha=[0]*3
        l=0
        count=0
        for r in range(len(s)):
            alpha[hashMap[s[r]]]+=1
            #print(alpha)
            while l<len(s) and all(alpha[i] for i in range(3)):
                count+=(len(s)-r) #all possible substrings starting from lth pos
                alpha[hashMap[s[l]]]-=1
                l+=1
        return count



        