from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap=OrderedDict()
        self.capacity=capacity

    def get(self, key: int) -> int:
        res=self.hashMap.get(key)
        #get is also  recent access
        if not res:
            return -1
        #if the key is present, since its recently used
        #del and add it again
        del self.hashMap[key]
        self.hashMap[key]=res
        return res
        
    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            del self.hashMap[key]
            self.hashMap[key]=value
        elif self.capacity>0:
            #can add new keys
            #both put and get means using the elmement
            self.hashMap[key]=value
            self.capacity-=1
        elif self.capacity==0:
            #delete the uppermost key in hashMap
            for k,v in self.hashMap.items():
                LRUkey,LRUval=k,v
                break
            del self.hashMap[LRUkey]
            self.hashMap[key]=value




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)