from collections import defaultdict
from typing import List

class TimeMap:

    def __init__(self):
        self.time=defaultdict(list)#key=> list of timestamps mapping
        self.hashMap=defaultdict(dict)#key->timestamp->value mapping

    def set(self, key: str, value: str, timestamp: int) -> None:
       
        self.time[key].append(timestamp)
        self.hashMap[key][timestamp]=value
        
    def get(self, key: str, timestamp: int) -> str:
        #get the closest timestamp if not , ""
        #timestamp is in increasing order=> binary search for closest timestamp
        nums=self.time[key]
        if key not in self.hashMap or timestamp<nums[0] :
            return ""

        def binarySearch(l,r):
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==timestamp:
                    return self.hashMap[key][nums[mid]]
                elif nums[mid]>timestamp:
                    r=mid-1
                else:
                    l=mid+1
            return self.hashMap[key][nums[l-1]]
        return binarySearch(0,len(nums)-1)
                        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)