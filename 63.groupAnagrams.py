#time complexity:O(nlogn to sort s strings)=>O(s x nlogn)
#space complexity:to hold s trings of max length n =>O(s x n)
class Solution(object):
    def groupAnagrams(self, strs):
        def sortFunc(a):
            return ''.join(sorted(a))
        #sort the strings in strs
        #this makes the anagrams to  have same order
        
        sortedStrs=list(map(sortFunc,strs))
        print(sortedStrs)

        #creating hashmap
        #key:value where key is the value from sortedStrs and value is a list from strs
        hm={}
        for i in range(len(sortedStrs)):
            if sortedStrs[i] not in hm:
                hm[sortedStrs[i]]=[strs[i]]
            else:
                hm[sortedStrs[i]].append(strs[i])
        finalList=[]
        for key in hm:
            finalList.append(hm[key])
        return finalList
obj=Solution()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
