# class Solution(object):
#     def largestNumber(self, nums):
#         #sort nums acc to highest max place
#         def sortHighest(item):
#             if(item//10!=0):#just one place
#                 quo=item//10
                
#                 while(quo!=0):#min 2 places
#                     q_prev=quo
#                     quo=quo//10
#             else:
#                    q_prev=item# if one place then it is the item itself
#             return q_prev
#         nums.sort(reverse=True)
#         nums.sort(reverse=True,key=sortHighest)
#         print(nums)

#         #join the list
#         string_type=("").join(map(str,nums))
#         return int(string_type)
# object=Solution()
# print(object.largestNumber([1,1,1,1]))


# class Solution(object):
#     def largestNumber(self, nums):
#         list1=[]
#         string1=("").join(map(str,nums))
#         for i in range(len(string1)):
#               list1.append(int(string1[i]))
#         list1.sort(reverse=True)

#         string2=("").join(map(str,list1))

#         return string2
# object=Solution()
# print(object.largestNumber([3,30,34,5,9]))

from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        #convert list of int to list of string
        string_list=list(map(str,nums))

        #sort the string elements based on concatenation
        #since a key can accept a function with only one arg 
        #to compare , this function needs 2 arg
        #hence from func tools,cmp_to_key is used to wrap multi arg accepting funct to key
        def compareTwo(a,b):
            if(a+b==b+a):#arrange in any order
                return 0
            elif(a+b>b+a):#comes first
                return -1
            else:
                return 1
            
        string_list.sort(key=cmp_to_key(compareTwo))
        print(string_list)

        #join to form a string
        final_string=("").join(string_list)

        if(final_string[0]=='0'):#to avoid printing '000..'
            final_string="0"

        return final_string

object=Solution()
print(object.largestNumber([3,30,34,5,9]))


