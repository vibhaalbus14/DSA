#--------------------------------------- TC :O(n**2)------------------------------------------------
class Solution:
    def minFlips(self, s: str) -> int:
        #approach
        #1.given the string s of len n say 1110 of len 4
        #target can be t1=1010 or t2=0101
        #2.we need to count the min no of flips and can append any no of times
        #3.for every append , till start s!=end s,
        #comapare the differences of currS with t1 and t2, store the minimum one

        n=len(s)
        target1=""
        target2=""
        
        num=True
        #form the target strings
        for _ in range(n):
            target1+=str(int(num))
            target2+=str(int(not num))
            num=not num #alternate num
        count1=0
        count2=0
        minCount=float("inf")
        for i in range(n):
            s=s[1:]+s[0]#append the first char to end
            #count the no of flips 
            for i in range(len(s)):
                if s[i]!=target1[i]: #count the differences=> flips
                    count1+=1
                if s[i]!=target2[i]:
                    count2+=1
            minCount=min(minCount,count1,count2)
            count1=0
            count2=0
        return minCount
        
#-------------------------- TC:O(n)-------------------------------------------------------------
class Solution:
    def minFlips(self, s: str) -> int:
        #approach
        #1.double the length of string, identify targets of given len s and 
        #double them as well
        #2.rather than appending every first char to the end and then comparing
        #we use sliding window
        #3.intially the differences are counted, and for every
        #decrement in window from left, we reduce the count if char 
        #was diff else not do anything
        #4.for every expansion on the right, we add to count if it causes difference
        #5.identify minimum for every window

        n=len(s)
        target1=""
        target2=""
        
        num=True
        #form the target strings of double length
        for _ in range(2*n):
            target1+=str(int(num))
            target2+=str(int(not num))
            num=not num #alternate num

        #double the size
        s=s*2
        count1=0
        count2=0
        minCount=float("inf")

        #fixed sliding window of size = original length
        #count the initial differences
        for i in range(n):
            if s[i]!=target1[i]:
                count1+=1
            if s[i]!=target2[i]:
                count2+=1
        minCount=min(minCount,count1,count2)

        for r in range(n,2*n):
            l=r-n
            #kicked out char from beginning => r-len(window)
            if target1[l]!=s[l]:
                count1-=1#since the difference is removed, dec count
            #after expanding , see if the difference is caused
            if target1[r]!=s[r]:
                count1+=1
            #do the same for target 2 and s
            if target2[l]!=s[l]:
                count2-=1
            if target2[r]!=s[r]:
                count2+=1
            
            #calculate the min for every window
            minCount=min(minCount,count1,count2)
    
        return minCount




        

        