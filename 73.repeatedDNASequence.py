#time complexity: O(n-k) for loop and inside loop O(k) for substring traversal => O((n-k)*k)
#space complexity: how many strings at max in ht?=> n-k ,and length of each string? k, =>O((n-k)*k)
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        ht={} #to store strings:no of occurences in hast table
        k=10
        str=s[:k] #creating a window
        ht[str]=1
        for i in range(k,len(s)):#O(n-k)
            str=s[i-k+1:i+1]#O(k)
            
            if str in ht:
                ht[str]+=1
            else:
                ht[str]=1
        finalList=[]
        for key,value in ht.items():
            if value>1:
                finalList.append(key)
        return finalList
obj=Solution()
print(obj.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(obj.findRepeatedDnaSequences("AAAAAAAAAAAAA"))