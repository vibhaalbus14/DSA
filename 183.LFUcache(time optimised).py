from collections import OrderedDict,defaultdict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hashStorage={} #key:(freq,value)
        self.freqTable=defaultdict(OrderedDict)# freq : {key : none}
        self.minFreq=0
        self.trueCapacity=capacity

    def get(self, key: int) -> int:
        if key not in self.hashStorage:
            return -1
        #1.find the freq of key from hashStorage
        #2.locate this freq and key in freqTable
        #3.del from freq table and check if the freq itself has to be deleted
        #4.update the freq
        #5.update in hashStorage==> key :(new_freq,value)
        #6.if this new_freq does not exists in freqTable,create that freq
        #7.insert in freq table
        #8.update the minFreq accordingly
        #9.return the value
        freq,val = self.hashStorage[key]
        del self.freqTable[freq][key]
        if not  self.freqTable[freq]:
            del  self.freqTable[freq]
        newFreq=freq+1
        self.hashStorage[key]=(newFreq,val)
        if newFreq not in self.freqTable:
            self.freqTable[newFreq]=OrderedDict()
        self.freqTable[newFreq][key]=None
        #no need to move_to_end, since every time we access, freq changes,and gets inserted
        #under new key, which will be by default in the end of orderedDict
        if self.minFreq==freq and not self.freqTable[freq]:
            self.minFreq+=1
        return val
        

    def put(self, key: int, value: int) -> None:
        #edge case, if capacity is zero, cannot "put"
        if self.trueCapacity==0:
            return
        #update functions   same as get, but u modify the value
        if key in self.hashStorage:
            freq,val=self.hashStorage[key]
            del self.freqTable[freq][key]
            if not self.freqTable[freq]:
                del self.freqTable[freq]
            newFreq=freq+1 #do not reset counter to 1, only increment
            self.hashStorage[key]=(newFreq,value) #set it to new value
            if newFreq not in self.freqTable:
                self.freqTable[newFreq]=OrderedDict()
            self.freqTable[newFreq][key]=None
            if self.minFreq==freq and not self.freqTable[freq]:
                self.minFreq+=1
        #if cache has leftover space
        elif self.capacity >0:
            #1.add key:(freq,val) where freq =1
            #2.check if this freq exists eles, create
            #3.add this key in freqTable 
            #4.decrement the capacity
            #5.set minFreq=1
            self.hashStorage[key]=(1,value) #hardcore 1, because thats where freq starts
            if 1  not in self.freqTable:
                self.freqTable[1]=OrderedDict()
            self.freqTable[1][key]=None
            self.capacity-=1
            self.minFreq=1
        #if capacity is full
        elif self.capacity<=0:
            #1.get the ordered dict from freqTbale using minFreq and get the first key in
            #3.delete the key from hashStorage
            #4.del from freqTable, if freq becomes none, del the freq
            #5.insert new values similar to self.capacity>0
            LFUfreq=self.minFreq
            LFUorderedDict=self.freqTable[LFUfreq]
            for k,v in LFUorderedDict.items():
                LFUkey,LFUval=k,v
                break
            del self.hashStorage[LFUkey]
            del self.freqTable[LFUfreq][LFUkey]
            if not self.freqTable[LFUfreq]:
                del self.freqTable[LFUfreq]

            self.hashStorage[key]=(1,value)
            if 1  not in self.freqTable:
                self.freqTable[1]=OrderedDict()
            self.freqTable[1][key]=None
            self.minFreq=1

            




        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)