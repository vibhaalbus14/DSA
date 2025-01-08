import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        #kth smallest element= largest element of max heap of size k
        #1.create a maxheap of size k
        #2.append the elements from the matrix accordingly
        #3.return the largest of heap
        #4.note: heapq supports minheap, to make a max heap, append negative values and 
        #negate the values before returning

        rows=len(matrix)
        cols=len(matrix[0])
        heap=[]

        for i in range(rows):
            for j in range (cols):
                heap.append(-matrix[i][j])
        heapq.heapify(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        return -heap[0]



        

