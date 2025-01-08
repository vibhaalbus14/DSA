# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """


        def helper(low,high):
            mid=int((low+high)/2)
            if mid==low and isBadVersion(mid):
                return mid
                
            if isBadVersion(mid):
                #check if its the first
                return helper(low,mid)
            else:
                return helper(mid+1,high)

        return helper(1,n)