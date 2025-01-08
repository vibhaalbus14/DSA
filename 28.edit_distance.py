#--------------------------------recursion-----------------------
#time complexity:O(3^(m+n))
#space complexity:O(n+m)
#-------------------------------recursion------------------------------
def minDistance(word1, word2):
    l1=len(word1)
    l2=len(word2)
    def helper(i,j):
        if(i==l1 and j==l2):
            return 0
        elif(i==l1):#insert remaining chars
            return l2-j
        elif(j==l2):#delete remaining chars
            return l1-i
        else:
            if(word1[i]==word2[j]):
                return helper(i+1,j+1)
            else:
                return  min(1+helper(i,j+1),#insertion
                        1+helper(i+1,j),#deletion
                        1+helper(i+1,j+1))#replacing

    if(len(word1) ==0 ):
        return len(word2)
    elif(len(word2)==0):
        return len(word1)
    elif(word1==word2):
        return 0
    else:
        return helper(0,0)

    
print(minDistance("hodse","dos"))
#-------------------------------memoization------------------------------
#time complexity:0(m*n)
#space complexity:O(nxm)+O(n+m)=>hast table + rec stack => O(nxm)
def minDistance(word1, word2):
    l1=len(word1)
    l2=len(word2)
    mem={}
    def helper(i,j):
        if (i,j) in mem:
            return mem[(i,j)]
        else:
            if(i==l1 and j==l2):
                return 0
            elif(i==l1):#insert remaining chars
                return l2-j
            elif(j==l2):#delete remaining chars
                return l1-i
            else:
                if(word1[i]==word2[j]):
                    mem[(i,j)]= helper(i+1,j+1)
                else:
                    mem[(i,j)]=  min(1+helper(i,j+1),#insertion
                            1+helper(i+1,j),#deletion
                            1+helper(i+1,j+1))#replacing
        return mem[(i,j)]

    if(len(word1) ==0 or len(word2)==0):
        return max(len(word2),len(word1))
    elif(word1==word2):
        return 0
    else:
        return helper(0,0)

    
print(minDistance("hodse","dos"))