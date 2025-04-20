class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # sliding window with hashMap
        #use consonant as the checker
        #approach: atleast(k)-atleast(k+1)=exactly k
        
        def trace(threshold):
            count=0
            l=0
            r=0
            consonants=0
            vowels=[0]*5
            hashMap={'a':0,
                    'e':1,
                    "i":2,
                    "o":3,
                    "u":4}

            #increase the window size
            while r<len(word):#increasing the window
                if word[r] in hashMap:
                    vowels[hashMap[word[r]]]+=1
                else:
                    consonants+=1
                #try to reduce the window by abiding to conditions
                while  (all(vowels[i] for i in range(5)) and consonants>=threshold):
                    
                    count+=(len(word)-r)
                    #reduce the window
                    if word[l] in hashMap:
                        vowels[hashMap[word[l]]]-=1
                    else:
                        consonants-=1
                    l+=1
                    
                r+=1
            
            return count
        
        return trace(k)-trace(k+1)
    
        


        