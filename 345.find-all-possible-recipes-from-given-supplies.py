from typing import List
from collections import defaultdict
import deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        adjList=defaultdict(list)
        indegree=defaultdict(int)
        recipeSet=set(recipes)
        supplySet=set(supplies)
        #go over every index
        #make ingredients point to recipe

        for i in range(len(ingredients)):
            for stuff in ingredients[i]:
                adjList[stuff].append(recipes[i])
                if stuff not in indegree:
                    indegree[stuff]=0
                indegree[recipes[i]]+=1
        dq=deque()
        res=[]
        
        for ing,val in indegree.items():
            if val==0 and ing in supplySet:
                #add the core ingredients only if found in supply set
                #this will prevent unecessary visit to recipe if all the ingredients are not there by not making recipe's indgree 0
                dq.append(ing)
                
        while dq:
            ing=dq.pop()
            if ing in recipeSet:
                res.append(ing)
            if ing in adjList:
                for neighbour in adjList[ing]:
                    indegree[neighbour]-=1
                    if indegree[neighbour]==0:
                        dq.append(neighbour)

        return res



        


        