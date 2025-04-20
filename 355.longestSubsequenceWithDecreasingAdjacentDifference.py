from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        #smart problem
        #abs brute force is needed with dp hashMap

        #approach
        #1.loop over all num in nums
        #2.store dp[(num,diff)]=longest subseq length
        #3.we know that numbers range from 1,300 => diff can be at max from 300 to 0
        #we make use of this fact and try to identify the prev numbers
        #4.whenever we find a number with same diff already in dp, we extend the subseq length of it
        #5.for every iteration , we store the max val

        hashMap={}
        maxLength=0

        for currNum in nums:
            #for every number, identify possible differences
            #since abs diff is asked we add and subrtract
            #if currNum+- prevNum=diff => currNum-=diff=prevNum
            #we make use of this fact

            currSubSeqLength=1 #the number itself can be a subsequence

            for diff in range(300,-1,-1):
                prevNum1=currNum+diff
                prevNum2=currNum-diff

                #check if prevNum, diff can be found in hhashMap
                #if yes, we extend its length

                if (prevNum1,diff) in hashMap:
                    currSubSeqLength=max(currSubSeqLength,hashMap[(prevNum1,diff)]+1)

                if (prevNum2,diff) in hashMap:
                    currSubSeqLength=max(currSubSeqLength,hashMap[(prevNum2,diff)]+1)
                
                #reset maxSubSeqLength

                hashMap[(currNum,diff)]=currSubSeqLength
                maxLength=max(maxLength,currSubSeqLength)
        
        return maxLength

                



        