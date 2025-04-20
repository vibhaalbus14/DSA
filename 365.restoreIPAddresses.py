from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #partition backtracking question
        #4 integers ,all within [0,255]
        #generate all possibilities such that everything is less than 255, if greater, break
        #consider length also into acc
        n=len(s)
        res=[]

        def backtrack(index,subList):
            nonlocal res
            if index==n and len(subList)==4:
                res.append(".".join(subList[:]))
                return

            #from curr index to n, partition are possible
            for j in range(index,n):
                if int(s[index:j+1])>255 :
                    break
                if s[index]=='0' and len(s[index:j+1])>1:
                    break

                #continue with this partition
                subList.append(s[index:j+1])
                backtrack(j+1,subList)
                subList.pop()
        backtrack(0,[])
        return res
        