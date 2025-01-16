class Solution:
    def minimumLength(self, s: str) -> int:
        n=len(s)
        hashMap={}
        for i in range(len(s)):
            if s[i]  in hashMap:
                hashMap[s[i]].append(i)
            else:
                hashMap[s[i]]=[i]
        print(hashMap)
        visited=set()
        for subList in hashMap.values():
            if len(subList)>2:
                i=1
                prev=None
                prev=subList[i-1]
                while i<len(subList)-1:
                    print(subList)
                    if subList[i] in visited:
                        i+=1
                        continue
                    
                    if prev not in visited and subList[i+1] not in visited:
                        print("bef, aft",prev,subList[i+1])
                        visited.add(prev)
                        visited.add(subList[i+1])
                        prev=subList[i]
                        print(visited)
                        i+=2
                
                    
            else:
                continue
        return n-len(visited)
print(Solution().minimumLength("ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj"))
#------------------------------------approach2------------------------------------------
class Solution:
    def minimumLength(self, s: str) -> int:
        hashMap=Counter(s)
        finalLength=0
        for values in hashMap.values():
            rem=values
            while rem>=3:
                rem-=2
            finalLength+=rem
        return finalLength