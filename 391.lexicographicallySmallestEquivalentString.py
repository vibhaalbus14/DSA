class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        #identify the eqyuivalence
        #switch the chars in baseStr with the smallest char of that grp
        #only smallest matters

        #list of sets
        storage=[]
        all_=set()

        for i in range(len(s1)):
            if s1[i] in all_ and s2[i] in all_:
                first,second=None,None
                for j in range(len(storage)):
                    if s1[i] in storage[j] and s2[i] in storage[j]:
                        first,second=j,j
                        pass
                    elif s1[i] in storage[j]:
                        if first==None:
                            first=j
                        
                    elif s2[i] in storage[j]:
                        if second==None:
                            second=j

                    if first!=None and second!=None:
                        break
                if first!=second:

                    storage[first].update(storage[second])
                    storage[second].update(storage[first])
                    
            elif s1[i] in all_:
                for currSet in storage:
                    if s1[i] in currSet:
                        currSet.add(s2[i])
                        all_.add(s2[i])
            elif s2[i] in all_:
                for currSet in storage:
                    if s2[i] in currSet:
                        currSet.add(s1[i])
                        all_.add(s1[i])
            else:
                all_.add(s1[i])
                all_.add(s2[i])
                storage.append({s1[i],s2[i]})

        res=[]        
        hashMap=defaultdict(int)
        for i,currSet in enumerate(storage):
            newList=list(currSet)
            newList.sort()

            hashMap[i]=newList[0]

        for char in baseStr:
            flag=False
            for i,currSet in enumerate(storage):
                if char in currSet:
                    res.append(hashMap[i])
                    flag=True
                    break
            if not flag:
                res.append(char)
            
        
        res="".join(res)
        return res


        