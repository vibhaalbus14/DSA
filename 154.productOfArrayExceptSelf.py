class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #approach
        #1.create a prefix product array from first to last
        #2.create a suffix product array from last to first
        #3.map the index of the element accordingly i.e
        #in prefixProduct i=>i+1
        #in suffix prodict i=>i
        #draw the diagram of all arrays up and down
        #this variation happens since we are filling the first place of prefix from first and last place of 
        #suffix from last saying thatb in case of no elements, the prod is one by default

        prefixProduct=[1 for _ in range(len(nums)+1)]
        suffixProduct=[1 for _ in range(len(nums)+1)]

        #populating prefixProduct from beginning
        for i in range(1,len(prefixProduct)):
            prefixProduct[i]=prefixProduct[i-1]*nums[i-1]

        #populating suffixProduct from end
        for i in range(len(suffixProduct)-2,-1,-1):
            suffixProduct[i]=suffixProduct[i+1]*nums[i]
        output=[]
        for i in range(len(nums)):
            #since index i from nums is being considered at i+1
            #we take the index i to be its prefix
            #since index i from nums is being considered at i
            #we take i+1 to be its suffix
            output.append(prefixProduct[i]*suffixProduct[i+1])
        return output