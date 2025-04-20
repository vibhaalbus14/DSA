class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #monotonic inc stack
        #before checking with stack check if char is already in stack
        #while pooping ensure the char on top is not the last occurence with highest index mapping

        #map all the chars to its highest index
        hashMap={}
        for i,char in enumerate(s):
            hashMap[char]=i
        seen=set()

        stack=[]

        for i,char in enumerate(s):
            if char in seen:
                continue
            
            while stack and char<=stack[-1] and i<hashMap[stack[-1]]:
                seen.remove(stack.pop())
                
            
            stack.append(char)
            seen.add(char)
        
        return "".join(stack)
