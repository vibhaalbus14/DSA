#74.1343NumberOfSub-arraysOfSizeK.py
#time complexity:O((n-k)*k)
#space complexity:O(1)
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        count=0
        threshold*=float(k)
        window=sum(arr[:k])
        
        if window>=threshold:
                count+=1
        #for i in range(len(arr)-k+1):#no of windows=no of different starts
        #    window=arr[i:i+k]
        for i in range(k,len(arr)):
            window=window+arr[i]-arr[i-k]
            
            if window>=threshold:
                count+=1
        return count
obj=Solution()
print(obj.numOfSubarrays([2,2,2,2,5,5,5,8],3,4))
print(obj.numOfSubarrays([11,13,17,23,29,31,7,5,2,3],3,5))
        