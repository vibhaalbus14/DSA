class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        #approach
        #1.store the prefix sum of ever row from given matrix into correspondinfg row of prefixSum matrix
        #2.do necessary subtractions to get answers like 1d sum range immutable
        
        self.rows=len(matrix)
        self.cols=len(matrix[0])
        self.prefixSum=[[0 for _ in range(self.cols+1)] for _ in range(self.rows) ]
        #populate prefixSum matrix
        for i in range(self.rows):
            for j in range(1,self.cols+1):#1 extra col 
                self.prefixSum[i][j]=self.prefixSum[i][j-1]+matrix[i][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum=0
        for i in range(row1,row2+1):
            sum+=self.prefixSum[i][col2+1]-self.prefixSum[i][col1]
        return sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)