from typing import List
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
         #approach
         #1.maintain a {team: list of pos present in all votes} hashMap
         #2.sort the teams by comparing the whole list , in case of conflict, ascii chars 


        hashMap={}
        n=len(votes[0])
        for team in votes[0]:
            hashMap[team]=[0]*n

        for vote in votes:
            for i,team in enumerate(vote):
                hashMap[team][i]+=1
        
        res=sorted(votes[0],key =lambda team: (hashMap[team],-ord(team)),reverse=True)

        return "".join(res)


        


        