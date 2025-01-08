from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        l=0
        r=0
        remaining=maxWidth
        noOfWords=0
        res=[]
        while l<=r and r<len(words):
            #can consider the word
            if remaining-len(words[r])>=0:
                remaining-=(len(words[r])+1) #extra one space to separate words
                r+=1
                noOfWords+=1
                print("consider remaining",remaining)
            else:
                #cannot consider the current word
                #from l to r-1, all words are to be placed in string
                #calculate amount of space required
                spaces=[]
                 #excluding the gap used to separate the words
                leftOutSpace=remaining+noOfWords
                #space is to be evenly spread out
                noOfSpaceSlots=noOfWords-1
                if noOfSpaceSlots:
                    #check if it can be even
                    if leftOutSpace%noOfSpaceSlots==0:
                        #even space
                        for _ in range(noOfSpaceSlots):
                            spaces.append(leftOutSpace//noOfSpaceSlots )
                    else:
                        extra=0
                        while leftOutSpace%noOfSpaceSlots!=0:
                            extra+=1
                            leftOutSpace-=1
                        for i in range(noOfSpaceSlots):
                            if extra:
                                addition=1
                                extra-=1
                                spaces.append((leftOutSpace//noOfSpaceSlots)+addition)
                            else:
                                spaces.append((leftOutSpace//noOfSpaceSlots))
                            
                else:
                    #left justified
                    #onlyone word
                    spaces.append(leftOutSpace)

                i=0
                s=[]
                #create res string
                while l<=r-1 or i<len(spaces):
                    s.append(words[l])
                    #now space
                    if i<len(spaces):
                        spaceList=[" " for _ in range(spaces[i])]
                        s.append("".join(spaceList))
                        #s.append(" "*spaces[i])
                        i+=1

                    l+=1
                
                res.append("".join(s))

                #reintialize all parameters
                remaining=maxWidth
                noOfWords=0
                l=r
        
        #when we come out of loop=> last word is included=> this forms last line
        #spaces for last line is one gap bw all worrds and rest of the space on right side

        spaces=[]
        #spaceUsedUp=remaining-noOfWords #one extra space after the last word is taken
        leftOutSpace=remaining+noOfWords
        #space is to be evenly spread out
        noOfSpaceSlots=noOfWords-1+1 #extra space for left justification

        for i in range(noOfSpaceSlots-1):
            spaces.append(1)
            leftOutSpace-=1
        spaces.append(leftOutSpace)
        
        i=0
        s=[]
        #create res string
        #create res string
        while l<=r-1 or i<len(spaces):
            s.append(words[l])
            #now space
            if i<len(spaces):
                spaceList=[" " for _ in range(spaces[i])]
                s.append("".join(spaceList))
                i+=1

            l+=1
        
        res.append("".join(s))

        return res



        