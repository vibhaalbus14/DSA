class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #fix a position
        #move left and right away from it
        #comman access to changes
        n=len(s)
        maxLength=float("-inf")

        for fixed in range(n):
            l=fixed-1
            r=fixed+1

            char=s[fixed]
            changes=k
            
            while l>-1 or r<n :
                if l>=0:
                    if s[l]!=char:
                        if changes>0:
                            changes-=1
                            l-=1
                            
                    else:
                        l-=1
                
                if r<n:
                    if s[r]!=char:
                        if changes>0:
                            changes-=1
                            r+=1
                    else:
                        r+=1
                #invalid where l and r are not out of range,but no more changes
                #can be made and s[l] and s[r]!=char
                
                if l>=0 and r<n:
                    #print("l,r",l,r)
                    if s[l]!=char and s[r]!=char and changes==0:
                        
                        break
                elif l<0 and r<n:
                    if s[r]!=char and changes==0:
                        break
                elif r>=n and l>=0:
                    if s[l]!=char and changes==0:
                        break 
            maxLength=max(maxLength,(r-1)-(l+1)+1)
        return maxLength


print(Solution().characterReplacement("AABABBA",1))