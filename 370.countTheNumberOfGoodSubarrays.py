from collections import defaultdict
from math import comb
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        hashMap=defaultdict(int)
        l=0
        r=0
        n=len(nums)
        pairs=0
        count=0

        while l<=r and r<n:
            currNum=nums[r]
            if hashMap[currNum]>1:
                prevContrib=comb(hashMap[currNum],2)
            else:
                prevContrib=0
            hashMap[currNum]+=1

            #calc diff pairs now
            if hashMap[currNum]>1:
                currContrib=comb(hashMap[currNum],2)
                #possibility of pairs
                #pairs=combinations
                pairs-=prevContrib #erase prev contrib , cause new ones are built over prev occ
                pairs+=currContrib
                #from n indices, need to choose 1 pair=> 2 indices
                if pairs>=k:
                    #count all sub arrays
                    #remove the Lth num
                    #identify nums[l]'s initial contribution to pairs
                    while pairs>=k:
                        count+=(n-r)
                        numToRemove=nums[l]
                        if hashMap[numToRemove]==1:
                            hashMap[numToRemove]-=1
                        else:

                            initialContrib=comb(hashMap[numToRemove],2)
                            hashMap[nums[l]]-=1
                            if hashMap[numToRemove]>1:
                                finalContrib=comb(hashMap[numToRemove],2)
                            else:
                                finalContrib=0
                            pairs-=initialContrib
                            pairs+=finalContrib
                            
                        l+=1
            r+=1
            
        return count
    

        