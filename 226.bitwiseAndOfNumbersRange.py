class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # res=left & right
        # if res==0:
        #     return 0

        # l=left+1
        # r=right-1
        # while l<=r:
        #     res=l & r & res
        #     if res==0:
        #         return 0
        #     l+=1
        #     r-=1
        # return res
        
        #---------------------------------approach2-----------------
        
        #differing bits contribute tozero ,
        #rather than and-ing them and eliminating,we do so by right shift
        #this is done until only the common prefix or root is left
        #this is left shifted "k" no of times to restore lsb
        count=0
        while left!=right:
            #since right shift divides the num, looping is achieved
            #efficiently rather than carrying forward the res
            left=left>>1
            right=right>>1
            count+=1
        return left<<count #shift back to original position




        