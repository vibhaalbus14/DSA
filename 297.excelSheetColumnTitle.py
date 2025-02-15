class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #approach
        #1.use mappings / ord to get alpha
        #2. since colNum is 1 indexed , make it 0 indexed
        #3.compute the rightmost char using %26 
        #4.move to the left char by //26
        letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res=""
        while columnNumber>0:
            columnNumber-=1#convert 1 indexed to 0 indexed
            charVal=columnNumber%26#identifying the char
            s=letters[charVal]#chr(charVal+ord("A"))#generate the char using ascii values
            res=s+res
            #go to next left char
            columnNumber//=26
        return res