# def calc_powerset(array):
#     complete_list=[[]]#appending an empty list since its always present regardless the given array
#     for num in array:
#         new_complete_list=complete_list.copy()
#         for lists in new_complete_list:
#             new_list=lists.copy()
#             new_list.append(num)
#             complete_list.append(new_list)
#     return complete_list

# print(calc_powerset([1,2,3,4]))

# array=[1,2,3]
# for num in array:
#     print("num is",num)

# complete_lists=[[]]
# for lists in complete_lists:
#     print("list is :",lists)
# print("--------------------------------------")
# for num in array:
#     new_complete_list=complete_lists.copy()
#     for lists in new_complete_list:
#         new_list=lists.copy()
#         new_list.append(num)
#         complete_lists.append(new_list)
    
# print(complete_lists)
    

#-------------------approach 2: BACKTRACKING---------------------------------
result=[]
def subset_calc(index,array,subset):
    global result
    #base cond
    if(index==len(array)):
        result.append(subset[:])
        return
    else:
        subset_calc(index+1,array,subset)#exclude step
        subset.append(array[index])#include step
        subset_calc(index+1,array,subset)
        subset.pop()#backtrack steps
        return
subset_calc(0,[1,2,3],[])
print(result)
print(len(result))