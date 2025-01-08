from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.hashStorage={}
        self.hashFreq=OrderedDict()
        self.capacity=capacity
        

    def get(self, key: int) -> int:
        if key not in self.hashStorage:
            return -1
        #increment the freq of the key in hashFreq
        self.hashFreq[key]+=1
        self.hashFreq.move_to_end(key)#in case of conflict,least recently used must be deleted
        return self.hashStorage[key]
        

    def put(self, key: int, value: int) -> None:
            #update
            if key in self.hashStorage:
                self.hashStorage[key]=value
                #update in hashFreq
                self.hashFreq[key]+=1 #increment the count,
                #not reset it!
                self.hashFreq.move_to_end(key)
            #add new
            elif self.capacity>0:
                self.hashStorage[key]=value
                self.hashFreq[key]=1
                self.capacity-=1
                
            else:
                #delete the least frequently used to make space
                #1.identify the min freq
                #2.incase of tie,least recently used=>
                #this is present at the start , so only if val<
                #is chosen
                minVal=float("inf")
                for k,v in self.hashFreq.items():
                    
                    if v<minVal:
                        minVal=v
                        LFUkey,LFUval=k,v
                #delete the key from hashStorage and hashFreq
                del self.hashStorage[LFUkey]
                del self.hashFreq[LFUkey]
                #insert
                self.hashStorage[key]=value
                self.hashFreq[key]=1
                



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)