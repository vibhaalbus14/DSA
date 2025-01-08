def fractionalknapsack(W,arr,n):
    def profitByWeight(a):
         return a[0]/a[1]
    arr.sort(reverse=True,key=profitByWeight)
    rem_wt=W
    overall_profit=0
    while(rem_wt>0):
         for item in arr:
              cap=min(rem_wt,item[1])
              overall_profit+=(cap/item[1])*item[0]
              rem_wt-=cap
    return overall_profit
print(fractionalknapsack(25,[[70, 10], [90, 20], [150, 30]],3))
         
         
              
# arr=[[70, 10], [90, 20], [150, 30]]        
# print("arr before sort :", arr)
# def profitByWeight(a):
         
#          return a[0]/a[1]
# arr.sort(reverse=True,key=profitByWeight)
# print("array after sorting :" ,arr)