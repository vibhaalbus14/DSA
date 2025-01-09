#any function that has a "yield" keyword is called a generator funct
#diff bw yield and return?
#return gives a value, stop func execution and does not store state
#yield gives a value/generator obj, pauses func execution and stores func's state

def paginator(nums,pageSize):#generator function
    for i in range(0,len(nums),pageSize):
        yield nums[i:i+pageSize] #everytime a yield is encountered, it stops iteration, stores the
        #yielded val in generator obj then resumes
        #once it has completed this loop and the func encounters end of func, if finally returns
        #the generator obj with all yielded values to calling function

print(paginator([1,24,5,6,8,9],2)) #generator obj
#need to loop, list conversion / use next() to see values in generator obj
print(list(paginator([1,24,5,6,8,9],2))) #looping over generator obj to yield values