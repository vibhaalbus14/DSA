from sortedcontainers import SortedDict
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        #index hashmap
        #num hashmap=> heap
        self.indexHashmap={}
        self.numHashmap=defaultdict(SortedDict)

    def change(self, index: int, number: int) -> None:
        if index not in self.indexHashmap:
            self.indexHashmap[index]=number
            self.numHashmap[number][index]=0
        else:
            #if already there
            oldNum=self.indexHashmap[index]
            self.indexHashmap[index]=number
            #del this index from oldnum
            del self.numHashmap[oldNum][index]
            #check if old num has no indices
            if not self.numHashmap[oldNum]:
                del self.numHashmap[oldNum]
            self.numHashmap[number][index]=0
        print("indexh",self.indexHashmap)
        print("numsh",self.numHashmap)
        
      
    def find(self, number: int) -> int:
        if number not in self.numHashmap:
            return -1

        return self.numHashmap[number].peekitem(index=0)
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)