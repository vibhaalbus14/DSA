#sliding window wont work as when u increase the size of the window, it doesnt necessarily mean ur increasing
#the sum value of the window and like wise ,when decreasing doesnt necessarily mean decreasing
#eg: [-1 -1 1] and k=0
#--------------------prefix sum and hashmap---------------------
#time comp:O(n)
#space Comp:O(n) #for hashmap
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #approach
        #why prefix sum?

        #since prefix sum is always computed from subarray
        #maintain a hashmap of key,value: prefixSum,occurence of prefix sum
        #1.initially populate it with 0,1 saying with 0 elements added, we get a prefixsum 0 and occurenec of 
        #prefix sum 0 is one
        #2.loop through the given array
        #3.add to the currSum
        #4.check if currSum-k exists in hashmap
        #now what does that mean?
        #it means uptill n numbers , if we can find a prefixsum diff=currSum-k ,then the count of diff will tell us 
        #the no of ways in which we can get sum k  from a subarray of n numbers
        #5.if it exists,add to the res
        #if it does or not, despite that , increment the count of currenet prefixSum obtained into hashmap

        hashMap={0:1}
        currSum=0
        res=0

        for num in nums:
            currSum+=num
            if currSum-k in hashMap:
                res+=hashMap[currSum-k]
            if currSum in hashMap:
                hashMap[currSum]+=1
            else:
                hashMap[currSum]=1
        return res


