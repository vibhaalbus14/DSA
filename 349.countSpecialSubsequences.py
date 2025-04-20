#Tc : n**2(logn)
#sc : O(n)

from math import gcd
from typing import List
from collections import defaultdict
import bisect

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        '''
        p<q<r<s
        p*r=q*s <==> p/q =s/r
        whenevr we encounter mult/dividion cases => use gcd
        this will prevent floating point errors
        => 
                📌 General Rule of Thumb
        If you're checking:

        Multiplication equality → a * d == b * c

        Division equality → a / b == c / d

        Instead, use:

        g1 = gcd(a, b)
        key1 = (a // g1, b // g1)  # Normalize (a/b)

        g2 = gcd(c, d)
        key2 = (c // g2, d // g2)  # Normalize (c/d)

        if key1 == key2:
        '''

        n=len(nums)
        hashMapSR=defaultdict(list)
        total=0

        #compute the gcd for s,r
        #iterate from end for s, n-1 to 1
        #iterate from s-2,0 for r => this ensures s>r+1

        for s in range(n-1,1,-1):
            for r in range(s-2,-1,-1):
                g=gcd(nums[s],nums[r])
                pair_sr=(nums[s]//g,nums[r]//g)

                #add in hashMapSR, key:val => pair_sr,r
                hashMapSR[pair_sr].append(r)

        for key in hashMapSR.keys():
            hashMapSR[key].sort()
        #print("ahshMap",hashMapSR)

        #identify p,q pairs
        for p in range(n):
            for q in range(p+2,n):
                
                g=gcd(nums[p],nums[q])
                pair_pq=(nums[p]//g,nums[q]//g)

                #serach for pair_pq
                if pair_pq in hashMapSR:
                    #count only the numbers where r val > q+1
                    insertPos=bisect.bisect_left(hashMapSR[pair_pq],q+2)
                    total+=len(hashMapSR[pair_pq])-insertPos

        return total
        
