#import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #approach
        #1.pass the number on loop till count==n  to a func that idetifies if  2/3/5 is its prime factor
        #2.rather than storing all nums in  alist, use a minheap to store the highest one
        #3.since the desired num is always the highest,itll work as all the small numbers are popped
        array=[1]
        if n==1:
            return 1
        
        def checkPrime(num):
            while num%2==0:
                num=num//2
            while num%3==0:
                num=num//3
            while num%5==0:
                num=num//5
            if num==1:
                return True
            else:
                return False            
            
        #maxHeap=[1]
        count=1 #since 1 is already appended
        num=2
        while count<n:
            #only after including the next num, increment count
            val=checkPrime(num)
            if val:
                count+=1
                array.append(num)
                #heapq.heappush(maxHeap,-num)    
            num+=1
        #print(array)
        return array[n-1]
obj=Solution()
print(obj.nthUglyNumber(11))

#------------------------approach2----------------------------------------------------------
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #approach
        #1.ugly numbers can be obtained by multiplying the min with 2,3 and 5
        #2.the above is an efficient way rather than generating all ugly nums,adding to array and popping n-1th
        #3.let the min heap have 1 initially
        #4.pop the root , mutltiply it with 2,3,5 and append them
        #5.pop it again and repeat the same
        #6.the no of pops =the nth ugly number
        #7.do not add duplicates
        #8.once nth ugly number is found,return that
        #now, why min heap? cause say 1 is multiplied by 2,3,5 => 4 is skipped
        #similarly, if 2 is multiplied by 2,3,5 10 is obtained first before getting 6,8 and 9
        #hence, min heap assures we go in increasing order of ugly numbers
        if n==1:
            return 1
        count=0
        minHeap=[1]
        #when popped,increment count
        while True:
            uglyNum=heapq.heappop(minHeap)
            count+=1
            if count==n:
                return uglyNum
            if uglyNum*2 not in minHeap:# to remove duplicates as 2*3 =6 and 3*2=6
                heapq.heappush(minHeap,uglyNum*2)
            if uglyNum*3 not in minHeap:
                heapq.heappush(minHeap,uglyNum*3)
            if uglyNum*5 not in minHeap:
                heapq.heappush(minHeap,uglyNum*5)
