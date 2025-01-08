#time complexity=O(nlogn)=>nlogn+n+n
#sapce complexity=O(1)
# class Solution(object):
#     def twoCitySchedCost(self, costs):

#         #making greedy choice sunch that impact to overall cost is minimum
#         costs.sort(key= lambda item: item[0]-item[1])
#         n=len(costs)
#         overall_cost=0
#         for i in range(n//2):
#             overall_cost+=costs[i][0]
#         for i in range(n//2,n):
#             overall_cost+=costs[i][1]
        
#         return overall_cost
    
# object=Solution()
# print(object.twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))

        
def twoCitySchedCost(costs):
    half=len(costs)//2
    def helper(i,a_count):
        if(i==len(costs)):
            return 0
        
        if(a_count<half):
            a_cost=costs[i][0]+helper(i+1,a_count+1)
        else:
            a_cost=float('inf')

        b_count=i-a_count
        if(b_count<half):
            b_cost=costs[i][1]+helper(i+1,a_count)
        else:
            b_cost=float('inf')

        return min(a_cost,b_cost)

    helper(0,0)
print(twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))