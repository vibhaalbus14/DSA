#time complexity=O(n-k)+O(k)=O(n)
#space complexity=O(1)
class Solution(object):
    def findMaxAverage(self, nums, k):
        currSum=sum(nums[:k])#window intialization
        maxSum=currSum

        #window is of size k
        #incoming element is nums[i]
        #outgoing elment is nums[i-k]
        for i in range(k,len(nums)):
            currSum=currSum+nums[i]-nums[i-k]
            maxSum=max(maxSum,currSum)
        return float(maxSum)/k #python conventionally performs integer division,hence one og the numbers must be converted to float
        