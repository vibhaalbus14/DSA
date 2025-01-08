# #---------------------------------brute force----------------------
# #time complexity = O(n^2 *m)
# class Solution(object):
#     def minWindow(self, s, t):
#         if len(s)<len(t):
#             return ""
#         tList={}
#         obtList=[]
#         minLength=float('inf')
#         minStringList=[]
#         for i in range(len(s)):
#             tList.clear()
#             for char in t: #everytime a fresh dict is created
#                 if char in tList:
#                     tList[char]+=1
#                 else:
#                     tList[char]=1
#             print(tList)
#             #empty obtList
#             #obtList.clear()
#             obtList[:]=[]
            
#             for j in range(i,len(s)):
#                 if s[j] in tList and tList[s[j]]!=0:
#                     #its value is not empty
#                     tList[s[j]]-=1
#                 obtList.append(s[j])
#                 values=tList.values()
#                 if sum(values)==0:
#                     #substring is found
#                     print(obtList)
#                     if len(obtList)<minLength:
#                         minLength=len(obtList)
#                         minStringList=obtList[:]
#                     break
#         if minLength==float('inf'):
#             return ''
#         else:
#             return "".join(minStringList)

# obj=Solution()
# #print(obj.minWindow("ADOBECODEBANC","ABC"))
# print(obj.minWindow("bba","ab"))


#--------------------------------2 pointers approach----------------------------
#time complexity = O(n)
#space comp:O(m
#n=len(s) and m=len(t)
#in a sliding window or two-pointer approach, even though there 
#are two loops (or nested loops), the inner loop does not reset for every iteration
#of the outer loop. Instead, it moves in one direction relative to the outer loop variable.
class Solution(object):
    def minWindow(self, s, t):
        if len(s)<len(t) or len(t)==0:
            return ""
        left=0
        right=0
        dictActual={}
        dictNow={}
        minLength=float('inf')
        minString=''

        for char in t:
            if char in dictActual:
                dictActual[char]+=1
            else:
                dictActual[char]=1

        required=len(dictActual) #no of chars whose cond is to be satisfied
        formed=0

        while right<len(s) :
            if s[right] in dictActual :
                dictNow[s[right]]=dictNow.get(s[right],0)+1
                if dictNow[s[right]]==dictActual[s[right]]:#cond is met
                    formed+=1

            while left<=right and formed==required:#passes the min threshold of all chars needed
                #window is obtained
                #try to reduce the window by popping from left
                lenString=right-left+1 #since it is zero indexed
                if lenString<minLength:
                    minLength=lenString
                    minString=s[left:right+1]
                element=s[left]#element to be popped out
                

                if element in dictNow:
                    dictNow[element]-=1
                    if dictNow[element]<dictActual[element]:
                        formed-=1
                left+=1

            right+=1
        return minString

obj=Solution()
print(obj.minWindow("ADOBECODEBANC","ABC"))
print(obj.minWindow("bba","ab"))




            


            
        