class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        #sliding window

        currLength=0
        currCost=maxCost
        l=0
        r=0
        included=set()
        maxLength=0

        while l<=r and r<len(s):
            #same chars
            if s[r]==t[r]:
                currLength+=1
                r+=1 
                
            elif abs(ord(s[r])-ord(t[r]))<=currCost:#diff chars but within cost
                included.add(r)
                currCost-=abs(ord(s[r])-ord(t[r]))
                currLength+=1
                r+=1
            else:
                #not within budget
                maxLength=max(currLength,maxLength)
                #cannot afford  or low on budget
                if l in included:
                    currCost+=abs(ord(s[l])-ord(t[l]))
                    currLength-=1
                    l+=1
                #not included in budget since chars are equal
                elif s[l]==t[l]:
                    currLength-=1
                    l+=1
                else:
                #cannot be considered only
                    l+=1
                    r+=1
                    
        maxLength=max(currLength,maxLength)

        return maxLength
