#bisect is a module used for:
#1.identify insertion position for a given value in iterable
#2.keep the iterable sorted

#sets, dictionaries are not indexable
#In tuple,it is used to identigy position but not insert any element as it is immutable
#best applicable for lists
import bisect

#bisect_left
#eg: if list=[2,3,4,5], we need to insert 3
#then 3 is inserted before any other occurences, if they exist in list
#bisect_left  gives this new 3  a position after 2=> [1,2,3(new),3,4,5]
#it only returns the position of placement of new number
#time comp:O(logn)
a=[1,2,3,4]
index_left=bisect.bisect_left(a,3,lo=0,hi=len(a)-1)
print(index_left)

#bisect_right
#eg: if list=[2,3,4,5], we need to insert 3
#then 3 is inserted after all other occurences, if they exist in list
#bisect_right gives this new 3 a position before 4=> [1,2,3,3(new),4,5]
#it only returns the position of placement of new number
#time comp:O(logn)
b=[1,2,3,4]
index_right=bisect.bisect_right(b,3)
print(index_right)

#insort_left
#inserts the number at given index by bisect_left
#time comp:O(n)
#it internally calls bisect.bisect_left
bisect.insort_left(a,3)
print(a)
#insort_right
#inserts the number at given index by bisect_right
#time comp:O(n)
#it internally calls bisect.bisect_right
bisect.insort_right(b,4)
print(b)

#for list of lists, if they have to be sorted acc to first value
c=[[1,5],[6,8],[12,18]]
startValues=[subList[0] for subList in c]
newValue=[7,10]
index=bisect.bisect_left(startValues,newValue[0])#first indetify the index
c.insert(index,newValue)#insert noramlly at that index
print(c)
