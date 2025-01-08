class Solution(object):
    def distributeCookies(self, cookies, k):
        dist=[0]*k
        min_unfairness=float('inf')#initializing to a large value
        def helper(index,dist):
            #base case
            nonlocal min_unfairness
            if(index==len(cookies)):
                min_unfairness=min(min_unfairness,max(dist))
                return
            else:
                for i in range(0,k):#k represents the child
                    dist[i]+=cookies[index]
                    if dist[i]<min_unfairness:#else the value cannot change min_unfairness
                        helper(index+1,dist)
                    dist[i]-=cookies[index]#backtract step
            
        helper(0,dist)
        return min_unfairness

obj=Solution()
print(obj.distributeCookies([6,1,3,2,2,4,1,2], 3))
