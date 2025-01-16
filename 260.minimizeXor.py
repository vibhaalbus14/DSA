class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        #1.count no of ones in num2 by right shift and & with 1
        #2.identify where to retain ones in x constructed by oppositeToNum1 such that max contribution is reduced=>retain msb ones from num1
        #3. total 3 cases (addition of ones in lsb or append to msb)
        #a)count>ones(num1)=>add ones in lsb if not, then add ones in msb
        #why? because say count=2 and list=["1"] , obviously length of list is small, so append 1*count + listNum
        #b)count<ones(num1)=> traverse through the end of oppositeToNum1 and make all remaining ones as zeroes

        n=num2
        count=0

        while n!=0:
            if n&1 ==1:
                count+=1
            n=n>>1
        #count=bin(num2).count("1")
        
        oppositeToNum1=list(bin(num1)[2:] )#"0b...""

        i=0
        while i<len(oppositeToNum1) and count:#building x here
            if oppositeToNum1[i]=="1":
                #first reduce the one's at positions that contribute the most
                count-=1
            i+=1
        #more ones in num1 than num2
        while i<len(oppositeToNum1):
            oppositeToNum1[i]="0"
            i+=1

        #identify where to insert 1 such that contribution is min
        i=len(oppositeToNum1)-1
        while i>=0 and count:
            if oppositeToNum1[i]=="0":
                oppositeToNum1[i]="1"
                count-=1
            i-=1
    
        #if despite that ,count is present
        if count:
            #append 1's at MSB positions
            oppositeToNum1=["1"]*count+oppositeToNum1
            

        return int("".join(oppositeToNum1),2)


        



        
        