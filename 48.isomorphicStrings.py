class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        ht={}
        for i,char in enumerate(s):
            if char not in ht: #check if the char in s is not added to ht
                if t[i] not in ht.values(): #check if the new character is not being mapped to an already 
                    #existing value
                    ht[char]=t[i] #if so,let its value be corresponding char of t at same index i
                else:
                    return False
            elif t[i]!=ht[char]: #if character exist in ht, but is being mapped to a diff value
                return False
            else:
                #ht[char]==t[i] #no action needed
                pass
        return True
object=Solution()
print(object.isIsomorphic("egg","add"))
print(object.isIsomorphic("foo","bar"))






























































































        