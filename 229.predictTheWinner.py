class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo={}
        def helper(l,r):
            nonlocal memo
            if (l,r) in memo:
                return memo[(l,r)]
            if l==r:
                return nums[r]
            if l>r:
                return 0

            #dont play turns, both players will have both the choices
            #return the val such that the score is always max
            #minimax principle
            chooseLeft=nums[l]-helper(l+1,r)
            chooseRight=nums[r]-helper(l,r-1)
            memo[(l,r)]=max(chooseLeft,chooseRight)

            return memo[(l,r)]
        #print(winner)
        ans=helper(0,len(nums)-1)

        return True if ans>=0 else False