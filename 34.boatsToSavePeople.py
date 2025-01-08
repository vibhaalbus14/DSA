#time complexity:O(n^2)
#space complexity:O(n)

# class Solution(object):
#     def numRescueBoats(self, people, limit):
#         boats=[]
#         people.sort(reverse=True)
#         boats.append([people[0 ],0,people[0]])
        

#         #logic=[1st person,2nd person,combined weight]
#         for i in range(1,len(people)):
#             for j in range(len(boats)):

#                 if boats[j][2]+people[i]<=limit and boats[j][1]==0:
#                     boats[j][1]=people[i]
#                     boats[j][2]+=people[i]
#                     break
               
#             else:
#                 boats.append([people[i],0,people[i]])
                
                
#         return len(boats)
# object=Solution()
# print(object.numRescueBoats([3,3,2,2,2],10))

#time complexity:O(n)
#space complexity:O(1)

class Solution(object):
    def numRescueBoats(self, people, limit):
        left,right=0,len(people)-1
        people.sort(reverse=True)
        boat=0

        while(left<right):
            #to match the heaviest and lightest
            if(people[left]+people[right]<=limit):
                #both take the same boat
                boat+=1
                #move towards next person
                left+=1
                right-=1
            else:
                #send the heaviest in a boat
                left+=1
                boat+=1
        if(left==right):
            #unmatched person, send this person alone
            boat+=1
        return boat

object=Solution()
print(object.numRescueBoats([2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10],50))

